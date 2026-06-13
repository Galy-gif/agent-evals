MAX_RETRIES = 3


def process(job, handler):
    """Run handler(job), retrying up to MAX_RETRIES times on failure."""
    last_error = None
    for _ in range(MAX_RETRIES):
        try:
            return handler(job)
        except Exception as exc:  # noqa: BLE001 - workers must survive any handler error
            last_error = exc
    raise RuntimeError(f"job failed after {MAX_RETRIES} attempts") from last_error
