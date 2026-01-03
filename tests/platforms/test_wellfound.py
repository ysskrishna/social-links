"""Tests for Wellfound platform."""
import pytest


class TestWellfound:
    """Test Wellfound platform"""

    def test_wellfound_user(self, sl):
        """Test Wellfound user profile"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://wellfound.com/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://wellfound.com/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://wellfound.com/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"
        # Test direct username
        assert sl.is_valid("wellfound", profile_id) is True
        assert sl.sanitize("wellfound", profile_id) == f"https://wellfound.com/u/{profile_id}"

    def test_wellfound_company(self, sl):
        """Test Wellfound company profile"""
        profile_id = "homelight"
        assert sl.detect_platform(f"https://wellfound.com/company/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://wellfound.com/company/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://wellfound.com/company/{profile_id}") == f"https://wellfound.com/company/{profile_id}"

    def test_wellfound_legacy_angellist_user(self, sl):
        """Test legacy AngelList user profile URLs (angel.co/u/)"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://angel.co/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"

    def test_wellfound_legacy_angellist_company(self, sl):
        """Test legacy AngelList company URLs (angel.co/company/ and angel.co/)"""
        profile_id = "slack"
        # Test angel.co/company/ format
        assert sl.detect_platform(f"https://angel.co/company/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/company/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/company/{profile_id}") == f"https://wellfound.com/company/{profile_id}"
        # Test old angel.co/ format (without /company/)
        assert sl.detect_platform(f"https://angel.co/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/{profile_id}") == f"https://wellfound.com/company/{profile_id}"

    def test_wellfound_with_www(self, sl):
        """Test Wellfound with www subdomain"""
        profile_id = "ysskrishna"
        # Test user profile with www
        assert sl.detect_platform(f"https://www.wellfound.com/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://www.wellfound.com/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://www.wellfound.com/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"
        # Test company profile with www
        company_id = "homelight"
        assert sl.detect_platform(f"https://www.wellfound.com/company/{company_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://www.wellfound.com/company/{company_id}") is True
        assert sl.sanitize("wellfound", f"https://www.wellfound.com/company/{company_id}") == f"https://wellfound.com/company/{company_id}"

    def test_wellfound_with_http(self, sl):
        """Test Wellfound with http protocol"""
        profile_id = "ysskrishna"
        # Test http instead of https
        assert sl.detect_platform(f"http://wellfound.com/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"http://wellfound.com/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"http://wellfound.com/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"

    def test_wellfound_with_trailing_slash(self, sl):
        """Test Wellfound with trailing slash"""
        profile_id = "ysskrishna"
        assert sl.is_valid("wellfound", f"https://wellfound.com/u/{profile_id}/") is True
        assert sl.sanitize("wellfound", f"https://wellfound.com/u/{profile_id}/") == f"https://wellfound.com/u/{profile_id}"

