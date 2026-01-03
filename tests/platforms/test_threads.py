"""Tests for Threads platform."""
import pytest


class TestThreads:
    """Test Threads platform"""

    def test_threads(self, sl):
        """Test Threads platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://threads.net/@{profile_id}") == "threads"
        assert sl.is_valid("threads", f"https://threads.net/@{profile_id}") is True
        assert sl.sanitize("threads", f"https://threads.net/@{profile_id}") == f"https://threads.net/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("threads", profile_id) is True
        assert sl.is_valid("threads", f"@{profile_id}") is True
        assert sl.sanitize("threads", profile_id) == f"https://threads.net/@{profile_id}"
        assert sl.sanitize("threads", f"@{profile_id}") == f"https://threads.net/@{profile_id}"

    def test_threads_with_www(self, sl):
        """Test Threads with www subdomain"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.threads.net/@{profile_id}") == "threads"
        assert sl.is_valid("threads", f"https://www.threads.net/@{profile_id}") is True
        assert sl.sanitize("threads", f"https://www.threads.net/@{profile_id}") == f"https://threads.net/@{profile_id}"

    def test_threads_with_http(self, sl):
        """Test Threads with http protocol"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"http://threads.net/@{profile_id}") == "threads"
        assert sl.is_valid("threads", f"http://threads.net/@{profile_id}") is True
        assert sl.sanitize("threads", f"http://threads.net/@{profile_id}") == f"https://threads.net/@{profile_id}"

    def test_threads_with_trailing_slash(self, sl):
        """Test Threads with trailing slash"""
        profile_id = "ysskrishna"
        assert sl.is_valid("threads", f"https://threads.net/@{profile_id}/") is True
        assert sl.sanitize("threads", f"https://threads.net/@{profile_id}/") == f"https://threads.net/@{profile_id}"

