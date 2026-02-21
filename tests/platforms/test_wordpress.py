"""Tests for WordPress platform."""
import pytest


class TestWordPress:
    """Test WordPress platform"""

    def test_wordpress(self, sl):
        """Test WordPress platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://wordpress.com/people/{profile_id}") == "wordpress"
        assert sl.is_valid("wordpress", f"https://wordpress.com/people/{profile_id}") is True
        assert sl.sanitize("wordpress", f"https://wordpress.com/people/{profile_id}") == f"https://wordpress.com/people/{profile_id}"
        # Test subdomain format
        assert sl.is_valid("wordpress", f"https://{profile_id}.wordpress.com") is True
        assert sl.sanitize("wordpress", f"https://{profile_id}.wordpress.com") == f"https://wordpress.com/people/{profile_id}"
        # Test direct username
        assert sl.is_valid("wordpress", profile_id) is True
        assert sl.sanitize("wordpress", profile_id) == f"https://wordpress.com/people/{profile_id}"

