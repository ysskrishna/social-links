"""Tests for Hacker News platform."""
import pytest


class TestHackernews:
    """Test Hacker News platform"""

    def test_hackernews(self, sl):
        """Test Hacker News platform"""
        profile_id = "pg"
        assert sl.detect_platform(f"https://news.ycombinator.com/user?id={profile_id}") == "hackernews"
        assert sl.is_valid("hackernews", f"https://news.ycombinator.com/user?id={profile_id}") is True
        assert sl.sanitize("hackernews", f"https://news.ycombinator.com/user?id={profile_id}") == f"https://news.ycombinator.com/user?id={profile_id}"
        # Test direct username
        assert sl.is_valid("hackernews", profile_id) is True
        assert sl.sanitize("hackernews", profile_id) == f"https://news.ycombinator.com/user?id={profile_id}"

    def test_hackernews_with_www(self, sl):
        """Test Hacker News with www subdomain"""
        profile_id = "pg"
        assert sl.detect_platform(f"https://www.news.ycombinator.com/user?id={profile_id}") == "hackernews"
        assert sl.is_valid("hackernews", f"https://www.news.ycombinator.com/user?id={profile_id}") is True
        assert sl.sanitize("hackernews", f"https://www.news.ycombinator.com/user?id={profile_id}") == f"https://news.ycombinator.com/user?id={profile_id}"

    def test_hackernews_with_http(self, sl):
        """Test Hacker News with http protocol"""
        profile_id = "pg"
        assert sl.detect_platform(f"http://news.ycombinator.com/user?id={profile_id}") == "hackernews"
        assert sl.is_valid("hackernews", f"http://news.ycombinator.com/user?id={profile_id}") is True
        assert sl.sanitize("hackernews", f"http://news.ycombinator.com/user?id={profile_id}") == f"https://news.ycombinator.com/user?id={profile_id}"

    def test_hackernews_with_trailing_slash(self, sl):
        """Test Hacker News with trailing slash"""
        profile_id = "pg"
        assert sl.is_valid("hackernews", f"https://news.ycombinator.com/user?id={profile_id}/") is True
        assert sl.sanitize("hackernews", f"https://news.ycombinator.com/user?id={profile_id}/") == f"https://news.ycombinator.com/user?id={profile_id}"

