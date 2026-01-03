"""Tests for ProductHunt platform."""
import pytest


class TestProducthunt:
    """Test ProductHunt platform"""

    def test_producthunt(self, sl):
        """Test ProductHunt platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.producthunt.com/@{profile_id}") == "producthunt"
        assert sl.is_valid("producthunt", f"https://www.producthunt.com/@{profile_id}") is True
        assert sl.sanitize("producthunt", f"https://www.producthunt.com/@{profile_id}") == f"https://www.producthunt.com/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("producthunt", profile_id) is True
        assert sl.is_valid("producthunt", f"@{profile_id}") is True
        assert sl.sanitize("producthunt", profile_id) == f"https://www.producthunt.com/@{profile_id}"
        assert sl.sanitize("producthunt", f"@{profile_id}") == f"https://www.producthunt.com/@{profile_id}"

    def test_producthunt_without_www(self, sl):
        """Test ProductHunt without www subdomain"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://producthunt.com/@{profile_id}") == "producthunt"
        assert sl.is_valid("producthunt", f"https://producthunt.com/@{profile_id}") is True
        assert sl.sanitize("producthunt", f"https://producthunt.com/@{profile_id}") == f"https://www.producthunt.com/@{profile_id}"

    def test_producthunt_with_http(self, sl):
        """Test ProductHunt with http protocol"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"http://www.producthunt.com/@{profile_id}") == "producthunt"
        assert sl.is_valid("producthunt", f"http://www.producthunt.com/@{profile_id}") is True
        assert sl.sanitize("producthunt", f"http://www.producthunt.com/@{profile_id}") == f"https://www.producthunt.com/@{profile_id}"

    def test_producthunt_with_trailing_slash(self, sl):
        """Test ProductHunt with trailing slash"""
        profile_id = "ysskrishna"
        assert sl.is_valid("producthunt", f"https://www.producthunt.com/@{profile_id}/") is True
        assert sl.sanitize("producthunt", f"https://www.producthunt.com/@{profile_id}/") == f"https://www.producthunt.com/@{profile_id}"

