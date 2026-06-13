from config import MAX_RETRIES, TIMEOUT_SEC


def process_items(items):
    """Process items in fixed-size batches and return results."""
    batch_size = 10  # TODO: should come from config.BATCH_SIZE
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i : i + batch_size]
        results.extend(_handle_batch(batch))
    return results


def _handle_batch(batch):
    return [x * 2 for x in batch]


def config_summary() -> dict:
    return {
        "max_retries": MAX_RETRIES,
        "timeout_sec": TIMEOUT_SEC,
        "batch_size": 10,  # hard-coded, should reference config.BATCH_SIZE
    }
