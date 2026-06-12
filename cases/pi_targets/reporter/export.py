from report import render


def dump(rows):
    """Export rows with a header line. Used by the nightly batch job."""
    header = "EXPORT"
    body = render(rows)
    return f"{header}\n{body}"
