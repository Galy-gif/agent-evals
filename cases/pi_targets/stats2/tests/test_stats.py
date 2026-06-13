import pytest
from stats import mean, median, range_summary


def test_mean_basic():
    assert mean([1, 2, 3]) == pytest.approx(2.0)


def test_mean_floats():
    assert mean([1.5, 2.5]) == pytest.approx(2.0)


def test_median_odd():
    assert median([3, 1, 4, 1, 5]) == pytest.approx(3.0)


def test_median_even():
    assert median([1, 2, 3, 4]) == pytest.approx(2.5)


def test_range_summary_basic():
    assert range_summary([1, 5, 3]) == (1, 5, 4)


def test_range_summary_single_element():
    assert range_summary([42]) == (42, 42, 0)


def test_range_summary_empty_returns_none():
    assert range_summary([]) is None


def test_range_summary_negative():
    assert range_summary([-3, -1, -5]) == (-5, -1, 4)
