from prices import final_price


def test_quarter_off():
    assert final_price(100, 25) == 75.0


def test_no_discount():
    assert final_price(19.99, 0) == 19.99


def test_rounding():
    assert final_price(10, 33) == 6.7
