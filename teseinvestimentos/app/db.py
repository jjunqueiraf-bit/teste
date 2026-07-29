"""Camada de dados: SQLite (biblioteca padrao), esquema e seed inicial.

O banco guarda metadados, permissoes, pontos de atencao e auditoria.
Os PDFs continuam nas pastas do Windows / OneDrive corporativo.
"""
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
import os

from . import crypto
from .config import settings, ensure_dirs

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    email TEXT,
    role TEXT NOT NULL DEFAULT 'ANALISTA',
    area TEXT,
    password_hash TEXT NOT NULL,
    password_salt TEXT NOT NULL,
    password_iterations INTEGER NOT NULL,
    must_change_password INTEGER NOT NULL DEFAULT 0,
    is_active INTEGER NOT NULL DEFAULT 1,
    failed_attempts INTEGER NOT NULL DEFAULT 0,
    locked_until TEXT,
    last_login_at TEXT,
    created_at TEXT NOT NULL,
    created_by INTEGER
);

CREATE TABLE IF NOT EXISTS opportunities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    sector TEXT,
    geography TEXT,
    thesis TEXT,
    origin_channel TEXT,
    stage_key TEXT NOT NULL DEFAULT 'originacao',
    status TEXT NOT NULL DEFAULT 'ATIVA',
    priority TEXT NOT NULL DEFAULT 'MEDIA',
    deal_size REAL,
    currency TEXT NOT NULL DEFAULT 'BRL',
    lead_user_id INTEGER REFERENCES users(id),
    sponsor TEXT,
    confidentiality TEXT NOT NULL DEFAULT 'RESTRITO',
    docs_folder TEXT,
    next_step TEXT,
    next_step_date TEXT,
    closed_reason TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    created_by INTEGER REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS opportunity_access (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    access_level TEXT NOT NULL DEFAULT 'comment',
    role_in_deal TEXT,
    added_at TEXT NOT NULL,
    added_by INTEGER,
    UNIQUE (opportunity_id, user_id)
);

CREATE TABLE IF NOT EXISTS stage_docs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id) ON DELETE CASCADE,
    stage_key TEXT NOT NULL,
    title TEXT NOT NULL,
    rel_path TEXT NOT NULL,
    version TEXT,
    doc_status TEXT NOT NULL DEFAULT 'VIGENTE',
    is_active INTEGER NOT NULL DEFAULT 1,
    notes TEXT,
    uploaded_by INTEGER REFERENCES users(id),
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS stage_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id) ON DELETE CASCADE,
    stage_key TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'NAO_INICIADO',
    owner_user_id INTEGER REFERENCES users(id),
    due_date TEXT,
    decision TEXT,
    decision_date TEXT,
    decision_by INTEGER REFERENCES users(id),
    decision_notes TEXT,
    updated_at TEXT NOT NULL,
    UNIQUE (opportunity_id, stage_key)
);

CREATE TABLE IF NOT EXISTS note_batches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES users(id),
    author_name TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    fmt TEXT NOT NULL,
    item_count INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    created_at_brt TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id) ON DELETE CASCADE,
    stage_key TEXT NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(id),
    author_name TEXT NOT NULL,
    kind TEXT NOT NULL DEFAULT 'PERGUNTA',
    severity TEXT NOT NULL DEFAULT 'MEDIA',
    text TEXT NOT NULL,
    doc_ref TEXT,
    status TEXT NOT NULL DEFAULT 'RASCUNHO',
    assigned_to INTEGER REFERENCES users(id),
    answer TEXT,
    answered_by INTEGER REFERENCES users(id),
    answered_at TEXT,
    batch_id INTEGER REFERENCES note_batches(id),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    opportunity_id INTEGER REFERENCES opportunities(id) ON DELETE CASCADE,
    contact_name TEXT NOT NULL,
    contact_org TEXT,
    contact_role TEXT,
    channel TEXT NOT NULL DEFAULT 'REUNIAO',
    subject TEXT,
    notes TEXT,
    occurred_at TEXT,
    next_step TEXT,
    next_step_date TEXT,
    owner_user_id INTEGER REFERENCES users(id),
    created_at TEXT NOT NULL,
    created_by INTEGER REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS sessions (
    token TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    csrf TEXT NOT NULL,
    created_at TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    last_seen_at TEXT NOT NULL,
    ip TEXT,
    user_agent TEXT,
    revoked INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT NOT NULL,
    user_id INTEGER,
    username TEXT,
    role TEXT,
    action TEXT NOT NULL,
    entity_type TEXT,
    entity_id TEXT,
    entity_name TEXT,
    severity TEXT NOT NULL DEFAULT 'INFO',
    ip TEXT,
    user_agent TEXT,
    detail TEXT
);

CREATE INDEX IF NOT EXISTS idx_notes_opp ON notes (opportunity_id, stage_key, status);
CREATE INDEX IF NOT EXISTS idx_docs_opp ON stage_docs (opportunity_id, stage_key, is_active);
CREATE INDEX IF NOT EXISTS idx_access_opp ON opportunity_access (opportunity_id, user_id);
CREATE INDEX IF NOT EXISTS idx_audit_created ON audit_log (created_at);
CREATE INDEX IF NOT EXISTS idx_inter_opp ON interactions (opportunity_id, occurred_at);
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def connect() -> sqlite3.Connection:
    ensure_dirs()
    conn = sqlite3.connect(settings.database_path, timeout=20, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn


@contextmanager
def db():
    conn = connect()
    try:
        yield conn
    finally:
        conn.close()


def rows(conn, sql, params=()):
    return [dict(r) for r in conn.execute(sql, params).fetchall()]


def row(conn, sql, params=()):
    found = conn.execute(sql, params).fetchone()
    return dict(found) if found else None


def execute(conn, sql, params=()):
    cur = conn.execute(sql, params)
    return cur.lastrowid


def create_user(conn, username, name, role, password, email=None, area=None,
                must_change=1, created_by=None):
    pwd_hash, salt, iterations = crypto.hash_password(password)
    return execute(
        conn,
        "INSERT INTO users (username, name, email, role, area, password_hash,"
        " password_salt, password_iterations, must_change_password, created_at, created_by)"
        " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (username.strip().lower(), name, email, role, area, pwd_hash, salt,
         iterations, must_change, utc_now(), created_by),
    )


def init_db(verbose: bool = True):
    """Cria o esquema e o usuario administrador inicial."""
    with db() as conn:
        conn.executescript(SCHEMA)
        existing = row(conn, "SELECT COUNT(*) AS total FROM users")
        if existing and existing["total"] == 0:
            first_password = os.environ.get("DEALSTACK_ADMIN_PASSWORD", "Trocar@DealStack2026")
            create_user(
                conn,
                username="admin",
                name="Administrador do Portal",
                role="ADMIN",
                password=first_password,
                email=None,
                area="Tese de Investimentos",
                must_change=1,
            )
            if verbose:
                print("[init] usuario admin criado. Senha inicial:", first_password)
                print("[init] a troca de senha sera exigida no primeiro acesso.")
        if verbose:
            print("[init] banco pronto em", settings.database_path)


if __name__ == "__main__":
    init_db()
