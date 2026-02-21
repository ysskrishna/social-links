"""Tests for Unsplash platform."""
import pytest


class TestUnsplash:
    """Test Unsplash platform"""

    def test_unsplash(self, sl):
        """Test Unsplash platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://unsplash.com/@{profile_id}") == "unsplash"
        assert sl.is_valid("unsplash", f"https://unsplash.com/@{profile_id}") is True
        assert sl.sanitize("unsplash", f"https://unsplash.com/@{profile_id}") == f"https://unsplash.com/@{profile_id}"
        # Test direct username with @
        assert sl.is_valid("unsplash", f"@{profile_id}") is True
        assert sl.sanitize("unsplash", f"@{profile_id}") == f"https://unsplash.com/@{profile_id}"
        # Test direct username without @
        assert sl.is_valid("unsplash", profile_id) is True
        assert sl.sanitize("unsplash", profile_id) == f"https://unsplash.com/@{profile_id}"

