"""Tests for LeetCode platform."""
import pytest


class TestLeetCode:
    """Test LeetCode platform"""

    def test_leetcode(self, sl):
        """Test LeetCode platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://leetcode.com/{profile_id}") == "leetcode"
        assert sl.is_valid("leetcode", f"https://leetcode.com/{profile_id}") is True
        assert sl.sanitize("leetcode", f"https://leetcode.com/{profile_id}") == f"https://leetcode.com/{profile_id}"
        # Test /u/ format
        assert sl.is_valid("leetcode", f"https://leetcode.com/u/{profile_id}") is True
        assert sl.sanitize("leetcode", f"https://leetcode.com/u/{profile_id}") == f"https://leetcode.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("leetcode", profile_id) is True
        assert sl.sanitize("leetcode", profile_id) == f"https://leetcode.com/{profile_id}"

