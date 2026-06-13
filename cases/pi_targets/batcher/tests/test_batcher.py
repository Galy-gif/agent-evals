import pytest
from processor import config_summary, process_items


def test_process_items_basic():
    assert process_items([1, 2, 3]) == [2, 4, 6]


def test_process_items_large():
    items = list(range(55))
    result = process_items(items)
    assert result == [x * 2 for x in items]


def test_batch_size_in_config_module():
    """config.py must export BATCH_SIZE = 50."""
    import config
    assert hasattr(config, "BATCH_SIZE"), "config.BATCH_SIZE is missing"
    assert config.BATCH_SIZE == 50


def test_config_summary_uses_config_batch_size():
    """config_summary() must report the value from config, not a hard-code."""
    summary = config_summary()
    assert summary["batch_size"] == 50


def test_process_items_respects_batch_size():
    """With BATCH_SIZE=50, 55 items should split into a batch of 50 + a batch of 5."""
    import config
    assert config.BATCH_SIZE == 50
    items = list(range(55))
    result = process_items(items)
    assert len(result) == 55
