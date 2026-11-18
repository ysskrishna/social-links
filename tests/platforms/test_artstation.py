"""Tests for ArtStation platform."""


class TestArtStation:
    """Test ArtStation platform"""

    def test_artstation(self, sl):
        """Test ArtStation platform"""
        profile_id = "ysskrishna"
        # Test subdomain format
        assert sl.is_valid("artstation", f"https://{profile_id}.artstation.com") is True
        assert sl.sanitize("artstation", f"https://{profile_id}.artstation.com") == f"https://www.artstation.com/{profile_id}"
