import pytest

from worker import MAX_RETRIES, process


def test_success_first_try():
    assert process(2, lambda job: job * 10) == 20


def test_retries_then_succeeds():
    calls = []

    def flaky(job):
        calls.append(job)
        if len(calls) < 3:
            raise ValueError("transient")
        return "ok"

    assert process("j", flaky) == "ok"
    assert len(calls) == MAX_RETRIES


def test_gives_up_after_max_retries():
    def always_fails(job):
        raise ValueError("boom")

    with pytest.raises(RuntimeError):
        process("j", always_fails)
