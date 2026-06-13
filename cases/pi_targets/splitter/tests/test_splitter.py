from splitter import split_fields


def test_basic_split():
    assert split_fields("a,b,c") == ["a", "b", "c"]


def test_preserves_empty_fields():
    assert split_fields("a,b,,c") == ["a", "b", "", "c"]


def test_single_field():
    assert split_fields("solo") == ["solo"]
