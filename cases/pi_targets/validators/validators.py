import re


def validate_username(name):
    """Return True for 3-16 chars of lowercase letters, digits, underscore."""
    return bool(re.fullmatch(r"[a-z0-9_]{3,16}", name))
