"""Tests for HackerRank platform."""
import pytest


class TestHackerRank:
    """Test HackerRank platform"""

    def test_hackerrank(self, sl):
        """Test HackerRank platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.hackerrank.com/profile/{profile_id}") == "hackerrank"
        assert sl.is_valid("hackerrank", f"https://www.hackerrank.com/profile/{profile_id}") is True
        assert sl.sanitize("hackerrank", f"https://www.hackerrank.com/profile/{profile_id}") == f"https://www.hackerrank.com/profile/{profile_id}"
        # Test direct username
        assert sl.is_valid("hackerrank", profile_id) is True
        assert sl.sanitize("hackerrank", profile_id) == f"https://www.hackerrank.com/profile/{profile_id}"

