def paginate(items: list, page: int, page_size: int) -> list:
    """Return the slice of items for the given 1-indexed page."""
    start = (page - 1) * page_size
    return items[start : start + page_size]


def page_count(total_items: int, page_size: int) -> int:
    """Return the total number of pages needed."""
    return total_items // page_size
