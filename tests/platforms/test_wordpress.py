"""Tests for WordPress platform."""


class TestWordPress:
    """Test WordPress platform"""

    def test_wordpress(self, sl):
        """Test WordPress platform"""
        profile_id = "ysskrishna"
        # Test subdomain format
        assert sl.is_valid("wordpress", f"https://{profile_id}.wordpress.com") is True
        assert sl.sanitize("wordpress", f"https://{profile_id}.wordpress.com") == f"https://wordpress.com/people/{profile_id}"
