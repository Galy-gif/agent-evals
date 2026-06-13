def format_price(amount, currency="USD"):
    """Format a price as '{currency} {amount:.2f}', e.g. 'USD 10.00'."""
    return f"{currency} {amount:.2f}"


def format_list(amounts, currency="USD"):
    """Format a list of amounts into price strings."""
    return [format_price(a, currency) for a in amounts]


def parse_price(price_str):
    """Parse a price string back to float.

    Assumes format: '{currency} {amount}', e.g. 'USD 10.00'.
    """
    parts = price_str.split()
    return float(parts[1])
