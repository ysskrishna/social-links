"""Tests for Rumble platform."""


class TestRumble:
    """Test Rumble platform"""

    def test_rumble(self, sl):
        """Test Rumble platform"""
        profile_id = "ysskrishna"
        # Test /c/ format
        assert sl.is_valid("rumble", f"https://rumble.com/c/{profile_id}") is True
        assert sl.sanitize("rumble", f"https://rumble.com/c/{profile_id}") == f"https://rumble.com/user/{profile_id}"
