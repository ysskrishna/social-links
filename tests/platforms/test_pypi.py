"""Tests for PyPI platform."""
import pytest


class TestPyPI:
    """Test PyPI platform"""

    def test_pypi(self, sl):
        """Test PyPI platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://pypi.org/user/{profile_id}") == "pypi"
        assert sl.is_valid("pypi", f"https://pypi.org/user/{profile_id}") is True
        assert sl.sanitize("pypi", f"https://pypi.org/user/{profile_id}") == f"https://pypi.org/user/{profile_id}"
        # Test direct username
        assert sl.is_valid("pypi", profile_id) is True
        assert sl.sanitize("pypi", profile_id) == f"https://pypi.org/user/{profile_id}"

