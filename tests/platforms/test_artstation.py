"""Tests for ArtStation platform."""
import pytest


class TestArtStation:
    """Test ArtStation platform"""

    def test_artstation(self, sl):
        """Test ArtStation platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.artstation.com/{profile_id}") == "artstation"
        assert sl.is_valid("artstation", f"https://www.artstation.com/{profile_id}") is True
        assert sl.sanitize("artstation", f"https://www.artstation.com/{profile_id}") == f"https://www.artstation.com/{profile_id}"
        # Test subdomain format
        assert sl.is_valid("artstation", f"https://{profile_id}.artstation.com") is True
        assert sl.sanitize("artstation", f"https://{profile_id}.artstation.com") == f"https://www.artstation.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("artstation", profile_id) is True
        assert sl.sanitize("artstation", profile_id) == f"https://www.artstation.com/{profile_id}"

