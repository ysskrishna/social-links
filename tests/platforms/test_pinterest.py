"""Tests for Pinterest platform."""


class TestPinterest:
    """Test Pinterest platform"""

    def test_pinterest_localized(self, sl):
        """Test Pinterest localized subdomains"""
        profile_id = "ysskrishna"
        # Test with country code subdomain (1-3 characters)
        assert sl.is_valid("pinterest", f"https://pl.pinterest.com/{profile_id}") is True
        assert sl.is_valid("pinterest", f"https://www.pinterest.com/{profile_id}") is True
        # Test that subdomains with more than 3 characters are rejected
        assert sl.is_valid("pinterest", f"https://abcd.pinterest.com/{profile_id}") is False
