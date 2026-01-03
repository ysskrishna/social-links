"""Tests for Hashnode platform."""
import pytest


class TestHashnode:
    """Test Hashnode platform"""

    def test_hashnode(self, sl):
        """Test Hashnode platform with main domain"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://hashnode.com/@{profile_id}") == "hashnode"
        assert sl.is_valid("hashnode", f"https://hashnode.com/@{profile_id}") is True
        assert sl.sanitize("hashnode", f"https://hashnode.com/@{profile_id}") == f"https://hashnode.com/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("hashnode", profile_id) is True
        assert sl.is_valid("hashnode", f"@{profile_id}") is True
        assert sl.sanitize("hashnode", profile_id) == f"https://hashnode.com/@{profile_id}"
        assert sl.sanitize("hashnode", f"@{profile_id}") == f"https://hashnode.com/@{profile_id}"

    def test_hashnode_dev_subdomain(self, sl):
        """Test Hashnode platform with .hashnode.dev subdomain"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://{profile_id}.hashnode.dev") == "hashnode"
        assert sl.is_valid("hashnode", f"https://{profile_id}.hashnode.dev") is True
        assert sl.sanitize("hashnode", f"https://{profile_id}.hashnode.dev") == f"https://hashnode.com/@{profile_id}"

    def test_hashnode_with_www(self, sl):
        """Test Hashnode with www subdomain"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.hashnode.com/@{profile_id}") == "hashnode"
        assert sl.is_valid("hashnode", f"https://www.hashnode.com/@{profile_id}") is True
        assert sl.sanitize("hashnode", f"https://www.hashnode.com/@{profile_id}") == f"https://hashnode.com/@{profile_id}"

    def test_hashnode_with_http(self, sl):
        """Test Hashnode with http protocol"""
        profile_id = "ysskrishna"
        # Test main domain with http
        assert sl.detect_platform(f"http://hashnode.com/@{profile_id}") == "hashnode"
        assert sl.is_valid("hashnode", f"http://hashnode.com/@{profile_id}") is True
        assert sl.sanitize("hashnode", f"http://hashnode.com/@{profile_id}") == f"https://hashnode.com/@{profile_id}"
        # Test .hashnode.dev subdomain with http
        assert sl.detect_platform(f"http://{profile_id}.hashnode.dev") == "hashnode"
        assert sl.is_valid("hashnode", f"http://{profile_id}.hashnode.dev") is True
        assert sl.sanitize("hashnode", f"http://{profile_id}.hashnode.dev") == f"https://hashnode.com/@{profile_id}"

    def test_hashnode_with_trailing_slash(self, sl):
        """Test Hashnode with trailing slash"""
        profile_id = "ysskrishna"
        assert sl.is_valid("hashnode", f"https://hashnode.com/@{profile_id}/") is True
        assert sl.sanitize("hashnode", f"https://hashnode.com/@{profile_id}/") == f"https://hashnode.com/@{profile_id}"
        assert sl.is_valid("hashnode", f"https://{profile_id}.hashnode.dev/") is True
        assert sl.sanitize("hashnode", f"https://{profile_id}.hashnode.dev/") == f"https://hashnode.com/@{profile_id}"

