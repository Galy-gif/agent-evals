def render(rows):
    """Render rows as a single delimited line."""
    return ",".join(str(r) for r in rows)
