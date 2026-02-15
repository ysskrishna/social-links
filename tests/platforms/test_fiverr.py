"""Tests for Fiverr platform."""
import pytest


class TestFiverr:
    """Test Fiverr platform"""

    def test_fiverr(self, sl):
        """Test Fiverr platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.fiverr.com/{profile_id}") == "fiverr"
        assert sl.is_valid("fiverr", f"https://www.fiverr.com/{profile_id}") is True
        assert sl.sanitize("fiverr", f"https://www.fiverr.com/{profile_id}") == f"https://www.fiverr.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("fiverr", profile_id) is True
        assert sl.sanitize("fiverr", profile_id) == f"https://www.fiverr.com/{profile_id}"

