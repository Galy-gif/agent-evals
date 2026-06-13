from hasher import hash_password, verify_password

# Simulated credential store: {username: {"hash": ..., "role": ...}}
_STORE = {
    "alice": {"hash": hash_password("secret123"), "role": "user"},
    "admin": {"hash": hash_password("admin_pass"), "role": "admin"},
}


def authenticate(username: str, password: str) -> bool:
    """Return True if username/password is valid, regardless of role."""
    entry = _STORE.get(username)
    if not entry:
        return False
    # Bug: role guard should not be here — authenticate() checks credentials only.
    if entry["role"] != "user":
        return False
    return verify_password(password, entry["hash"])


def get_role(username: str) -> str | None:
    """Return the role for username, or None if not found."""
    entry = _STORE.get(username)
    return entry["role"] if entry else None
