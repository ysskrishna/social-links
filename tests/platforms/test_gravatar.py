"""Tests for Gravatar platform."""
import pytest


class TestGravatar:
    """Test Gravatar platform"""

    def test_gravatar(self, sl):
        """Test Gravatar platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"https://gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("gravatar", profile_id) is True
        assert sl.sanitize("gravatar", profile_id) == f"https://gravatar.com/{profile_id}"

    def test_gravatar_with_language(self, sl):
        """Test Gravatar with language subdomain"""
        profile_id = "ysskrishna"
        # Test with en subdomain
        assert sl.detect_platform(f"https://en.gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"https://en.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://en.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"
        # Test with other language codes
        assert sl.is_valid("gravatar", f"https://fr.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://fr.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"

    def test_gravatar_with_www(self, sl):
        """Test Gravatar with www subdomain"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"https://www.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://www.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"

    def test_gravatar_with_http(self, sl):
        """Test Gravatar with http protocol"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"http://gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"http://gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"http://gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"

    def test_gravatar_with_trailing_slash(self, sl):
        """Test Gravatar with trailing slash"""
        profile_id = "ysskrishna"
        assert sl.is_valid("gravatar", f"https://gravatar.com/{profile_id}/") is True
        assert sl.sanitize("gravatar", f"https://gravatar.com/{profile_id}/") == f"https://gravatar.com/{profile_id}"

