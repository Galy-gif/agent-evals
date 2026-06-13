import pytest
from lookup import build_table, lookup, preprocess


def test_preprocess_lowercase():
    assert preprocess("Hello") == "hello"


def test_preprocess_strip():
    assert preprocess("  world  ") == "world"


def test_lookup_exact_match():
    table = build_table([("apple", 1), ("banana", 2)])
    assert lookup("apple", table) == 1


def test_lookup_case_insensitive():
    """lookup() must find keys regardless of the case used at build time."""
    table = build_table([("Apple", 1), ("BANANA", 2)])
    assert lookup("apple", table) == 1
    assert lookup("banana", table) == 2
    assert lookup("APPLE", table) == 1


def test_lookup_missing_key():
    table = build_table([("apple", 1)])
    assert lookup("cherry", table) is None


def test_table_keys_are_normalized():
    """After build_table, all stored keys must already be in normalized form."""
    table = build_table([("Apple", 1), ("  Banana  ", 2)])
    assert "apple" in table
    assert "banana" in table
    assert "Apple" not in table
    assert "  Banana  " not in table
