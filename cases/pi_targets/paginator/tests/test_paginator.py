import pytest
from paginator import page_count, paginate


def test_paginate_first_page():
    assert paginate(list(range(10)), 1, 3) == [0, 1, 2]


def test_paginate_second_page():
    assert paginate(list(range(10)), 2, 3) == [3, 4, 5]


def test_paginate_last_partial_page():
    # 10 items, page_size=3: page 4 has just [9]
    assert paginate(list(range(10)), 4, 3) == [9]


def test_page_count_exact_division():
    assert page_count(9, 3) == 3


def test_page_count_with_remainder():
    # 10 items / page_size 3 → 4 pages (3+3+3+1)
    assert page_count(10, 3) == 4


def test_page_count_single_page():
    assert page_count(5, 10) == 1


def test_page_count_zero_items():
    assert page_count(0, 10) == 0


def test_page_count_one_item():
    assert page_count(1, 10) == 1
