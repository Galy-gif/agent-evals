import pytest
from formatter import format_list, format_price, parse_price


def test_format_price_usd():
    assert format_price(10.0) == "10.00 USD"


def test_format_price_eur():
    assert format_price(99.99, "EUR") == "99.99 EUR"


def test_format_price_zero():
    assert format_price(0, "GBP") == "0.00 GBP"


def test_format_list_basic():
    assert format_list([10, 20, 30]) == ["10.00 USD", "20.00 USD", "30.00 USD"]


def test_round_trip():
    """parse_price must recover the exact amount that format_price produced."""
    for amount in [1.0, 42.5, 0.99, 100.0]:
        assert parse_price(format_price(amount)) == pytest.approx(amount)


def test_parse_price_direct():
    assert parse_price("10.00 USD") == pytest.approx(10.0)
    assert parse_price("99.99 EUR") == pytest.approx(99.99)
