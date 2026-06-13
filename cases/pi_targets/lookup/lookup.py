def preprocess(text: str) -> str:
    """Normalize text: lowercase and strip whitespace."""
    return text.lower().strip()


def build_table(entries):
    """Build a lookup table from (key, value) pairs.

    Keys are stored as-is; lookup() preprocesses the query key at query time.
    """
    return dict(entries)


def lookup(key: str, table: dict):
    """Return the value for key after preprocessing, or None if not found."""
    return table.get(preprocess(key))
