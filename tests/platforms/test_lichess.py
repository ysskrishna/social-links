"""Tests for Lichess platform."""


class TestLichess:
    """Test Lichess platform"""

    def test_lichess(self, sl):
        """Test Lichess platform"""
        profile_id = "ysskrishna"
        # Test direct username with @
        assert sl.is_valid("lichess", f"@{profile_id}") is True
        assert sl.sanitize("lichess", f"@{profile_id}") == f"https://lichess.org/@/{profile_id}"
