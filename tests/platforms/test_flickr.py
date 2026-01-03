"""Tests for Flickr platform."""
import pytest


class TestFlickr:
    """Test Flickr platform"""

    def test_flickr(self, sl):
        """Test Flickr platform with /people/ path"""
        profile_id = "dv-hans"
        assert sl.detect_platform(f"https://www.flickr.com/people/{profile_id}") == "flickr"
        assert sl.is_valid("flickr", f"https://www.flickr.com/people/{profile_id}") is True
        assert sl.sanitize("flickr", f"https://www.flickr.com/people/{profile_id}") == f"https://www.flickr.com/people/{profile_id}"
        # Test direct username
        assert sl.is_valid("flickr", profile_id) is True
        assert sl.sanitize("flickr", profile_id) == f"https://www.flickr.com/people/{profile_id}"

    def test_flickr_without_www(self, sl):
        """Test Flickr without www subdomain"""
        profile_id = "dv-hans"
        assert sl.detect_platform(f"https://flickr.com/people/{profile_id}") == "flickr"
        assert sl.is_valid("flickr", f"https://flickr.com/people/{profile_id}") is True
        assert sl.sanitize("flickr", f"https://flickr.com/people/{profile_id}") == f"https://www.flickr.com/people/{profile_id}"

    def test_flickr_with_http(self, sl):
        """Test Flickr with http protocol"""
        profile_id = "dv-hans"
        assert sl.detect_platform(f"http://www.flickr.com/people/{profile_id}") == "flickr"
        assert sl.is_valid("flickr", f"http://www.flickr.com/people/{profile_id}") is True
        assert sl.sanitize("flickr", f"http://www.flickr.com/people/{profile_id}") == f"https://www.flickr.com/people/{profile_id}"

    def test_flickr_with_trailing_slash(self, sl):
        """Test Flickr with trailing slash"""
        profile_id = "dv-hans"
        assert sl.is_valid("flickr", f"https://www.flickr.com/people/{profile_id}/") is True
        assert sl.sanitize("flickr", f"https://www.flickr.com/people/{profile_id}/") == f"https://www.flickr.com/people/{profile_id}"

    def test_flickr_with_at_symbol(self, sl):
        """Test Flickr with @ symbol in username (common for numeric IDs)"""
        profile_id = "123456@N01"
        # Test direct username with @ symbol
        assert sl.is_valid("flickr", profile_id) is True
        assert sl.sanitize("flickr", profile_id) == f"https://www.flickr.com/people/{profile_id}"

