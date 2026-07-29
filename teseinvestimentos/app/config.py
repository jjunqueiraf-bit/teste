"""Configuracao central da aplicacao.

Todos os caminhos de rede/disco ficam concentrados aqui e podem ser
sobrescritos pelo arquivo config.json na raiz do projeto (nao versionado).
"""
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config.json"
WEB_DIR = BASE_DIR / "web"

DEFAULTS = {
    # Identidade
    "org_name": "Votorantim - Tese de Investimentos",
    "banner": "CONFIDENCIAL - uso interno. Nao redistribuir.",

    # Servidor
    "host": "0.0.0.0",
    "port": 8060,

    # Repositorios em disco (rede interna / OneDrive corporativo)
    "documents_root": str(BASE_DIR / "repositorio" / "oportunidades"),
    "comments_root": str(BASE_DIR / "repositorio" / "comentarios"),
    "database_path": str(BASE_DIR / "data" / "dealstack.db"),

    # Comentarios / pontos de atencao
    "notes_format": "docx",           # docx | txt | both
    "notes_subfolders": True,          # cria <oportunidade>/<AAAA>/<MM>

    # Sessao e autenticacao
    "session_hours": 8,
    "idle_minutes": 45,
    "max_login_attempts": 5,
    "lockout_minutes": 15,
    "min_password_length": 12,

    # Controles de documento
    "allow_download": True,
    "download_roles": ["ADMIN", "LIDER", "ANALISTA"],
    "watermark_notes": True,

    # Auditoria
    "audit_retention_days": 3650,

    # Fuso de Brasilia
    "timezone_offset_hours": -3,
    "timezone_label": "BRT",
}


class Settings(dict):
    """Dicionario com acesso por atributo (settings.port)."""

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as exc:  # pragma: no cover
            raise AttributeError(item) from exc


def load() -> Settings:
    data = dict(DEFAULTS)
    if CONFIG_FILE.exists():
        with CONFIG_FILE.open("r", encoding="utf-8") as handle:
            user_data = json.load(handle)
        if not isinstance(user_data, dict):
            raise ValueError("config.json deve conter um objeto JSON")
        data.update(user_data)

    for key in ("documents_root", "comments_root", "database_path"):
        raw = os.path.expandvars(str(data[key]))
        data[key] = str(Path(raw).expanduser())

    if os.environ.get("DEALSTACK_PORT"):
        data["port"] = int(os.environ["DEALSTACK_PORT"])
    if os.environ.get("DEALSTACK_HOST"):
        data["host"] = os.environ["DEALSTACK_HOST"]

    return Settings(data)


settings = load()


def ensure_dirs() -> None:
    """Cria as pastas base se ainda nao existirem."""
    Path(settings.database_path).parent.mkdir(parents=True, exist_ok=True)
    Path(settings.documents_root).mkdir(parents=True, exist_ok=True)
    Path(settings.comments_root).mkdir(parents=True, exist_ok=True)


def reload() -> Settings:
    """Recarrega o config.json em tempo de execucao."""
    global settings
    settings = load()
    return settings
