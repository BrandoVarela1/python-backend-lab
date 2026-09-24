from backend_lab.health import get_health_status, is_ready


def test_is_ready() -> None:
    assert is_ready() is True


def test_get_health_status() -> None:
    assert get_health_status() == {"status": "ok"}
