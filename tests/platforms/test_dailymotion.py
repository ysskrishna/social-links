"""Tests for Dailymotion platform."""
import pytest


class TestDailymotion:
    """Test Dailymotion platform"""

    def test_dailymotion(self, sl):
        """Test Dailymotion platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.dailymotion.com/{profile_id}") == "dailymotion"
        assert sl.is_valid("dailymotion", f"https://www.dailymotion.com/{profile_id}") is True
        assert sl.sanitize("dailymotion", f"https://www.dailymotion.com/{profile_id}") == f"https://www.dailymotion.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("dailymotion", profile_id) is True
        assert sl.sanitize("dailymotion", profile_id) == f"https://www.dailymotion.com/{profile_id}"

