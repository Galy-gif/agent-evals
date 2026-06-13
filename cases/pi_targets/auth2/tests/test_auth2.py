import pytest
from auth import authenticate, get_role


def test_regular_user_valid_password():
    assert authenticate("alice", "secret123") is True


def test_regular_user_wrong_password():
    assert authenticate("alice", "wrong") is False


def test_unknown_user():
    assert authenticate("nobody", "pass") is False


def test_admin_valid_password():
    # Admin users must also be authenticatable — role should not block login.
    assert authenticate("admin", "admin_pass") is True


def test_admin_wrong_password():
    assert authenticate("admin", "wrong") is False


def test_get_role_user():
    assert get_role("alice") == "user"


def test_get_role_admin():
    assert get_role("admin") == "admin"


def test_get_role_unknown():
    assert get_role("nobody") is None
