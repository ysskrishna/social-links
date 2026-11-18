"""Tests for Gravatar platform."""


class TestGravatar:
    """Test Gravatar platform"""

    def test_gravatar_with_language(self, sl):
        """Test Gravatar with language subdomain"""
        profile_id = "ysskrishna"
        # Test with en subdomain
        assert sl.detect_platform(f"https://en.gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"https://en.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://en.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"
        # Test with other language codes
        assert sl.is_valid("gravatar", f"https://fr.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://fr.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"
