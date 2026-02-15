"""Tests for Replit platform."""
import pytest


class TestReplit:
    """Test Replit platform"""

    def test_replit(self, sl):
        """Test Replit platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://replit.com/@{profile_id}") == "replit"
        assert sl.is_valid("replit", f"https://replit.com/@{profile_id}") is True
        assert sl.sanitize("replit", f"https://replit.com/@{profile_id}") == f"https://replit.com/@{profile_id}"
        # Test direct username with @
        assert sl.is_valid("replit", f"@{profile_id}") is True
        assert sl.sanitize("replit", f"@{profile_id}") == f"https://replit.com/@{profile_id}"
        # Test direct username without @
        assert sl.is_valid("replit", profile_id) is True
        assert sl.sanitize("replit", profile_id) == f"https://replit.com/@{profile_id}"

