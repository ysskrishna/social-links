"""Tests for Kuaishou platform."""
import pytest


class TestKuaishou:
    """Test Kuaishou platform"""

    def test_kuaishou(self, sl):
        """Test Kuaishou platform"""
        profile_id = "3xxdnfw963m6abu"
        assert sl.detect_platform(f"https://www.kuaishou.com/profile/{profile_id}") == "kuaishou"
        assert sl.is_valid("kuaishou", f"https://www.kuaishou.com/profile/{profile_id}") is True
        assert sl.sanitize("kuaishou", f"https://www.kuaishou.com/profile/{profile_id}") == f"https://www.kuaishou.com/profile/{profile_id}"
        # Test direct username
        assert sl.is_valid("kuaishou", profile_id) is True
        assert sl.sanitize("kuaishou", profile_id) == f"https://www.kuaishou.com/profile/{profile_id}"

    def test_kuaishou_without_www(self, sl):
        """Test Kuaishou without www subdomain"""
        profile_id = "3xxdnfw963m6abu"
        assert sl.detect_platform(f"https://kuaishou.com/profile/{profile_id}") == "kuaishou"
        assert sl.is_valid("kuaishou", f"https://kuaishou.com/profile/{profile_id}") is True
        assert sl.sanitize("kuaishou", f"https://kuaishou.com/profile/{profile_id}") == f"https://www.kuaishou.com/profile/{profile_id}"

    def test_kuaishou_with_http(self, sl):
        """Test Kuaishou with http protocol"""
        profile_id = "3xxdnfw963m6abu"
        assert sl.detect_platform(f"http://www.kuaishou.com/profile/{profile_id}") == "kuaishou"
        assert sl.is_valid("kuaishou", f"http://www.kuaishou.com/profile/{profile_id}") is True
        assert sl.sanitize("kuaishou", f"http://www.kuaishou.com/profile/{profile_id}") == f"https://www.kuaishou.com/profile/{profile_id}"

    def test_kuaishou_with_trailing_slash(self, sl):
        """Test Kuaishou with trailing slash"""
        profile_id = "3xxdnfw963m6abu"
        assert sl.is_valid("kuaishou", f"https://www.kuaishou.com/profile/{profile_id}/") is True
        assert sl.sanitize("kuaishou", f"https://www.kuaishou.com/profile/{profile_id}/") == f"https://www.kuaishou.com/profile/{profile_id}"

