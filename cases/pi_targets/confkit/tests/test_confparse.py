import pytest

from confparse import load_config


def test_parses_object():
    assert load_config('{"debug": true, "workers": 4}') == {"debug": True, "workers": 4}


def test_rejects_array_root():
    with pytest.raises(ValueError):
        load_config("[1, 2, 3]")


def test_rejects_invalid_json():
    with pytest.raises(Exception):
        load_config("{not json}")
