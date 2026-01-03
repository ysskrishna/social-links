"""Tests for GitLab platform."""
import pytest


class TestGitlab:
    """Test GitLab platform"""

    def test_gitlab(self, sl):
        """Test GitLab platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://gitlab.com/{profile_id}") == "gitlab"
        assert sl.is_valid("gitlab", f"https://gitlab.com/{profile_id}") is True
        assert sl.sanitize("gitlab", f"https://gitlab.com/{profile_id}") == f"https://gitlab.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("gitlab", profile_id) is True
        assert sl.sanitize("gitlab", profile_id) == f"https://gitlab.com/{profile_id}"

    def test_gitlab_with_www(self, sl):
        """Test GitLab with www subdomain"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.gitlab.com/{profile_id}") == "gitlab"
        assert sl.is_valid("gitlab", f"https://www.gitlab.com/{profile_id}") is True
        assert sl.sanitize("gitlab", f"https://www.gitlab.com/{profile_id}") == f"https://gitlab.com/{profile_id}"

    def test_gitlab_with_http(self, sl):
        """Test GitLab with http protocol"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"http://gitlab.com/{profile_id}") == "gitlab"
        assert sl.is_valid("gitlab", f"http://gitlab.com/{profile_id}") is True
        assert sl.sanitize("gitlab", f"http://gitlab.com/{profile_id}") == f"https://gitlab.com/{profile_id}"

    def test_gitlab_with_trailing_slash(self, sl):
        """Test GitLab with trailing slash"""
        profile_id = "ysskrishna"
        assert sl.is_valid("gitlab", f"https://gitlab.com/{profile_id}/") is True
        assert sl.sanitize("gitlab", f"https://gitlab.com/{profile_id}/") == f"https://gitlab.com/{profile_id}"

