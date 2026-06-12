import pytest
from metrics import average, total


def test_average_basic():
    assert average([2, 4, 6]) == pytest.approx(4.0)


def test_average_single():
    assert average([10]) == pytest.approx(10.0)


def test_total():
    assert total([1, 2, 3]) == 6
