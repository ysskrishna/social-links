"""Tests for Gumroad platform."""


class TestGumroad:
    """Test Gumroad platform"""

    def test_gumroad_path_format(self, sl):
        """Test Gumroad platform with path format"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://gumroad.com/{profile_id}") == "gumroad"
        assert sl.is_valid("gumroad", f"https://gumroad.com/{profile_id}") is True
        assert sl.sanitize("gumroad", f"https://gumroad.com/{profile_id}") == f"https://gumroad.com/{profile_id}"
