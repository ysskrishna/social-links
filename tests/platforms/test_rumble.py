"""Tests for Rumble platform."""
import pytest


class TestRumble:
    """Test Rumble platform"""

    def test_rumble(self, sl):
        """Test Rumble platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://rumble.com/user/{profile_id}") == "rumble"
        assert sl.is_valid("rumble", f"https://rumble.com/user/{profile_id}") is True
        assert sl.sanitize("rumble", f"https://rumble.com/user/{profile_id}") == f"https://rumble.com/user/{profile_id}"
        # Test /c/ format
        assert sl.is_valid("rumble", f"https://rumble.com/c/{profile_id}") is True
        assert sl.sanitize("rumble", f"https://rumble.com/c/{profile_id}") == f"https://rumble.com/user/{profile_id}"
        # Test direct username
        assert sl.is_valid("rumble", profile_id) is True
        assert sl.sanitize("rumble", profile_id) == f"https://rumble.com/user/{profile_id}"

