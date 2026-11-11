"""Tests for Medium platform."""
import pytest


class TestMedium:
    """Test Medium platform"""

    def test_medium(self, sl):
        """Test Medium platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://medium.com/@{profile_id}") == "medium"
        assert sl.is_valid("medium", f"https://medium.com/@{profile_id}") is True
        assert sl.sanitize("medium", f"https://medium.com/@{profile_id}") == f"https://medium.com/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("medium", profile_id) is True
        assert sl.is_valid("medium", f"@{profile_id}") is True
        assert sl.sanitize("medium", profile_id) == f"https://medium.com/@{profile_id}"
        assert sl.sanitize("medium", f"@{profile_id}") == f"https://medium.com/@{profile_id}"

    def test_medium_subdomain(self, sl):
        """Profiles are also served at <name>.medium.com"""
        assert sl.detect_platform("https://ev.medium.com") == "medium"
        assert sl.is_valid("medium", "https://ev.medium.com/") is True
        assert sl.sanitize("medium", "https://ev.medium.com") == "https://medium.com/@ev"
        assert sl.extract_id("medium", "http://ev.medium.com/") == "ev"

    @pytest.mark.parametrize("host", ["www", "help", "blog", "policy", "api", "miro", "cdn-images-1"])
    def test_medium_own_hosts_are_not_profiles(self, sl, host):
        assert sl.is_valid("medium", f"https://{host}.medium.com/") is False
