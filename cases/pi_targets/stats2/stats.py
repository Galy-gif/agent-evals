def mean(values: list) -> float:
    """Return the arithmetic mean of values."""
    return sum(values) / len(values)


def range_summary(values: list):
    """Return (min, max, spread) for a non-empty list of numbers.

    Returns None for an empty list.
    """
    return min(values), max(values), max(values) - min(values)


def median(values: list) -> float:
    """Return the median of values."""
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2.0
    return float(s[mid])
