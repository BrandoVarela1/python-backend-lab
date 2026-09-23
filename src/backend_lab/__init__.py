from backend_lab.health import is_ready


def test_is_ready() -> None:
    assert is_ready() is True
