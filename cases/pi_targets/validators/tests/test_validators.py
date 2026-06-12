from validators import validate_username


def test_valid_username():
    assert validate_username("alice_01")


def test_too_short():
    assert not validate_username("ab")


def test_bad_characters():
    assert not validate_username("Alice!")
