"""Tests for SlideShare platform."""
import pytest


class TestSlideshare:
    """Test SlideShare platform"""

    def test_slideshare(self, sl):
        """Test SlideShare platform"""
        profile_id = "michaelyublosky"
        assert sl.detect_platform(f"https://www.slideshare.net/{profile_id}") == "slideshare"
        assert sl.is_valid("slideshare", f"https://www.slideshare.net/{profile_id}") is True
        assert sl.sanitize("slideshare", f"https://www.slideshare.net/{profile_id}") == f"https://www.slideshare.net/{profile_id}"
        # Test direct username
        assert sl.is_valid("slideshare", profile_id) is True
        assert sl.sanitize("slideshare", profile_id) == f"https://www.slideshare.net/{profile_id}"

    def test_slideshare_without_www(self, sl):
        """Test SlideShare without www subdomain"""
        profile_id = "michaelyublosky"
        assert sl.detect_platform(f"https://slideshare.net/{profile_id}") == "slideshare"
        assert sl.is_valid("slideshare", f"https://slideshare.net/{profile_id}") is True
        assert sl.sanitize("slideshare", f"https://slideshare.net/{profile_id}") == f"https://www.slideshare.net/{profile_id}"

    def test_slideshare_with_http(self, sl):
        """Test SlideShare with http protocol"""
        profile_id = "michaelyublosky"
        assert sl.detect_platform(f"http://www.slideshare.net/{profile_id}") == "slideshare"
        assert sl.is_valid("slideshare", f"http://www.slideshare.net/{profile_id}") is True
        assert sl.sanitize("slideshare", f"http://www.slideshare.net/{profile_id}") == f"https://www.slideshare.net/{profile_id}"

    def test_slideshare_with_trailing_slash(self, sl):
        """Test SlideShare with trailing slash"""
        profile_id = "michaelyublosky"
        assert sl.is_valid("slideshare", f"https://www.slideshare.net/{profile_id}/") is True
        assert sl.sanitize("slideshare", f"https://www.slideshare.net/{profile_id}/") == f"https://www.slideshare.net/{profile_id}"

