"""Tests for Gumroad platform."""
import pytest


class TestGumroad:
    """Test Gumroad platform"""

    def test_gumroad_subdomain(self, sl):
        """Test Gumroad platform with subdomain format"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://{profile_id}.gumroad.com") == "gumroad"
        assert sl.is_valid("gumroad", f"https://{profile_id}.gumroad.com") is True
        assert sl.sanitize("gumroad", f"https://{profile_id}.gumroad.com") == f"https://gumroad.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("gumroad", profile_id) is True
        assert sl.sanitize("gumroad", profile_id) == f"https://gumroad.com/{profile_id}"

    def test_gumroad_path_format(self, sl):
        """Test Gumroad platform with path format"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://gumroad.com/{profile_id}") == "gumroad"
        assert sl.is_valid("gumroad", f"https://gumroad.com/{profile_id}") is True
        assert sl.sanitize("gumroad", f"https://gumroad.com/{profile_id}") == f"https://gumroad.com/{profile_id}"

    def test_gumroad_with_www(self, sl):
        """Test Gumroad with www subdomain"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.gumroad.com/{profile_id}") == "gumroad"
        assert sl.is_valid("gumroad", f"https://www.gumroad.com/{profile_id}") is True
        assert sl.sanitize("gumroad", f"https://www.gumroad.com/{profile_id}") == f"https://gumroad.com/{profile_id}"

    def test_gumroad_with_http(self, sl):
        """Test Gumroad with http protocol"""
        profile_id = "ysskrishna"
        # Test subdomain format with http
        assert sl.detect_platform(f"http://{profile_id}.gumroad.com") == "gumroad"
        assert sl.is_valid("gumroad", f"http://{profile_id}.gumroad.com") is True
        assert sl.sanitize("gumroad", f"http://{profile_id}.gumroad.com") == f"https://gumroad.com/{profile_id}"
        # Test path format with http
        assert sl.detect_platform(f"http://gumroad.com/{profile_id}") == "gumroad"
        assert sl.is_valid("gumroad", f"http://gumroad.com/{profile_id}") is True
        assert sl.sanitize("gumroad", f"http://gumroad.com/{profile_id}") == f"https://gumroad.com/{profile_id}"

    def test_gumroad_with_trailing_slash(self, sl):
        """Test Gumroad with trailing slash"""
        profile_id = "ysskrishna"
        assert sl.is_valid("gumroad", f"https://{profile_id}.gumroad.com/") is True
        assert sl.sanitize("gumroad", f"https://{profile_id}.gumroad.com/") == f"https://gumroad.com/{profile_id}"
        assert sl.is_valid("gumroad", f"https://gumroad.com/{profile_id}/") is True
        assert sl.sanitize("gumroad", f"https://gumroad.com/{profile_id}/") == f"https://gumroad.com/{profile_id}"

