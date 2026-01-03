"""Tests for Crunchbase platform."""
import pytest


class TestCrunchbase:
    """Test Crunchbase platform"""

    def test_crunchbase_organization(self, sl):
        """Test Crunchbase organization profile"""
        profile_id = "slack"
        assert sl.detect_platform(f"https://www.crunchbase.com/organization/{profile_id}") == "crunchbase"
        assert sl.is_valid("crunchbase", f"https://www.crunchbase.com/organization/{profile_id}") is True
        assert sl.sanitize("crunchbase", f"https://www.crunchbase.com/organization/{profile_id}") == f"https://www.crunchbase.com/organization/{profile_id}"

    def test_crunchbase_company(self, sl):
        """Test Crunchbase company profile"""
        profile_id = "tiny-speck"
        assert sl.detect_platform(f"https://www.crunchbase.com/company/{profile_id}") == "crunchbase"
        assert sl.is_valid("crunchbase", f"https://www.crunchbase.com/company/{profile_id}") is True
        assert sl.sanitize("crunchbase", f"https://www.crunchbase.com/company/{profile_id}") == f"https://www.crunchbase.com/organization/{profile_id}"

    def test_crunchbase_person(self, sl):
        """Test Crunchbase person profile"""
        profile_id = "elon-musk"
        assert sl.detect_platform(f"https://www.crunchbase.com/person/{profile_id}") == "crunchbase"
        assert sl.is_valid("crunchbase", f"https://www.crunchbase.com/person/{profile_id}") is True
        assert sl.sanitize("crunchbase", f"https://www.crunchbase.com/person/{profile_id}") == f"https://www.crunchbase.com/person/{profile_id}"

    def test_crunchbase_without_www(self, sl):
        """Test Crunchbase without www subdomain"""
        profile_id = "slack"
        assert sl.detect_platform(f"https://crunchbase.com/organization/{profile_id}") == "crunchbase"
        assert sl.is_valid("crunchbase", f"https://crunchbase.com/organization/{profile_id}") is True
        assert sl.sanitize("crunchbase", f"https://crunchbase.com/organization/{profile_id}") == f"https://www.crunchbase.com/organization/{profile_id}"

    def test_crunchbase_with_http(self, sl):
        """Test Crunchbase with http protocol"""
        profile_id = "slack"
        assert sl.detect_platform(f"http://www.crunchbase.com/organization/{profile_id}") == "crunchbase"
        assert sl.is_valid("crunchbase", f"http://www.crunchbase.com/organization/{profile_id}") is True
        assert sl.sanitize("crunchbase", f"http://www.crunchbase.com/organization/{profile_id}") == f"https://www.crunchbase.com/organization/{profile_id}"

    def test_crunchbase_with_trailing_slash(self, sl):
        """Test Crunchbase with trailing slash"""
        profile_id = "slack"
        assert sl.is_valid("crunchbase", f"https://www.crunchbase.com/organization/{profile_id}/") is True
        assert sl.sanitize("crunchbase", f"https://www.crunchbase.com/organization/{profile_id}/") == f"https://www.crunchbase.com/organization/{profile_id}"

