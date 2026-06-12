from report import render


def run(rows):
    """Entry point used by the CLI."""
    return "REPORT: " + render(rows)
