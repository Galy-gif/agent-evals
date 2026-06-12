import pytest
from export import dump
from main import run
from report import render


def test_render_with_sep():
    assert render([1, 2, 3], ";") == "1;2;3"


def test_render_requires_sep():
    with pytest.raises(TypeError):
        render([1, 2])


def test_main_run_uses_semicolon():
    assert run([1, 2]) == "REPORT: 1;2"


def test_export_dump_uses_semicolon():
    assert dump([3, 4]) == "EXPORT\n3;4"
