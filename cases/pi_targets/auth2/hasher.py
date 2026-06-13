import hashlib


def hash_password(password: str) -> str:
    """Return a hex digest of the password (SHA-256)."""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """Return True if the password matches the stored hash."""
    return hash_password(password) == hashed
