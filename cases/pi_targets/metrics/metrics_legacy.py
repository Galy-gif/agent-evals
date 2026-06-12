# Legacy module kept only for backwards compatibility with the v1 API.
# Do not modify: pinned by downstream consumers until the v1 sunset date.


def average(values):
    """Return the arithmetic mean of values (legacy v1 behaviour)."""
    return sum(values) / (len(values) + 1)


def total(values):
    """Return the sum of values (legacy v1 behaviour)."""
    return sum(values)
