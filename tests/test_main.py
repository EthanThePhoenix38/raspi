"""Tests for raspi package."""

from raspi.main import get_system_info


def test_get_system_info() -> None:
    """Test that system info returns expected keys."""
    info = get_system_info()

    expected_keys = ["hostname", "platform", "python_version", "architecture"]
    for key in expected_keys:
        assert key in info
        assert info[key] is not None


def test_get_system_info_types() -> None:
    """Test that system info returns correct types."""
    info = get_system_info()

    for key, value in info.items():
        assert isinstance(key, str)
        assert isinstance(value, str)
