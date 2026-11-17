"""Tests for Unsplash platform."""


class TestUnsplash:
    """Test Unsplash platform"""

    def test_unsplash(self, sl):
        """Test Unsplash platform"""
        profile_id = "ysskrishna"
        # Test direct username with @
        assert sl.is_valid("unsplash", f"@{profile_id}") is True
        assert sl.sanitize("unsplash", f"@{profile_id}") == f"https://unsplash.com/@{profile_id}"
