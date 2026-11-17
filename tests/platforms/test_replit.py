"""Tests for Replit platform."""


class TestReplit:
    """Test Replit platform"""

    def test_replit(self, sl):
        """Test Replit platform"""
        profile_id = "ysskrishna"
        # Test direct username with @
        assert sl.is_valid("replit", f"@{profile_id}") is True
        assert sl.sanitize("replit", f"@{profile_id}") == f"https://replit.com/@{profile_id}"
