from billing import total_with_tax


def test_discount_applied_before_tax():
    # (100 - 20) * 1.10 == 88.0; applying tax first would give 90.0
    assert total_with_tax(100, 0.10, 20) == 88.0


def test_no_discount():
    assert total_with_tax(50, 0.08, 0) == 54.0
