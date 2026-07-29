"""Primitivas de seguranca sem dependencias externas.

Hash de senha com PBKDF2-SHA256 (260k iteracoes), comparacao em tempo
constante, geracao de tokens de sessao/CSRF e politica minima de senha.
"""
import hashlib
import hmac
import secrets
import unicodedata

ITERATIONS = 260_000
ALGO = "pbkdf2_sha256"


def hash_password(password: str, salt: str = None, iterations: int = ITERATIONS):
    """Retorna (hash_hex, salt_hex, iteracoes)."""
    if salt is None:
        salt = secrets.token_hex(16)
    derived = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        iterations,
    )
    return derived.hex(), salt, iterations


def verify_password(password: str, stored_hash: str, salt: str, iterations: int) -> bool:
    calculated, _, _ = hash_password(password, salt, int(iterations))
    return hmac.compare_digest(calculated, stored_hash or "")


def new_token(nbytes: int = 32) -> str:
    return secrets.token_urlsafe(nbytes)


def token_fingerprint(token: str) -> str:
    """Identificador curto para logar sessao sem expor o token."""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:12]


def password_policy_error(password: str, minimum: int = 12):
    if password is None or len(password) < minimum:
        return "A senha deve ter ao menos " + str(minimum) + " caracteres."
    classes = 0
    classes += 1 if any(c.islower() for c in password) else 0
    classes += 1 if any(c.isupper() for c in password) else 0
    classes += 1 if any(c.isdigit() for c in password) else 0
    classes += 1 if any(not c.isalnum() for c in password) else 0
    if classes < 3:
        return "Combine maiusculas, minusculas, numeros e simbolos (minimo 3 tipos)."
    lowered = password.lower()
    for weak in ("senha", "password", "123456", "votorantim", "admin", "qwerty"):
        if weak in lowered:
            return "A senha contem um termo previsivel (" + weak + ")."
    return None


def slugify(value: str, keep_case: bool = True) -> str:
    """Normaliza texto para uso em nome de arquivo/pasta (sem acentos)."""
    if not value:
        return "SemNome"
    normalized = unicodedata.normalize("NFKD", str(value))
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    parts = [p for p in ascii_only.replace("-", " ").replace("_", " ").split() if p]
    cleaned = []
    for part in parts:
        safe = "".join(ch for ch in part if ch.isalnum())
        if safe:
            cleaned.append(safe if keep_case else safe.lower())
    result = "".join(word[:1].upper() + word[1:] for word in cleaned) if keep_case else "-".join(cleaned)
    return result[:80] or "SemNome"
