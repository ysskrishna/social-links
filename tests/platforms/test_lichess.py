"""Tests for Lichess platform."""
import pytest


class TestLichess:
    """Test Lichess platform"""

    def test_lichess(self, sl):
        """Test Lichess platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://lichess.org/@/{profile_id}") == "lichess"
        assert sl.is_valid("lichess", f"https://lichess.org/@/{profile_id}") is True
        assert sl.sanitize("lichess", f"https://lichess.org/@/{profile_id}") == f"https://lichess.org/@/{profile_id}"
        # Test direct username with @
        assert sl.is_valid("lichess", f"@{profile_id}") is True
        assert sl.sanitize("lichess", f"@{profile_id}") == f"https://lichess.org/@/{profile_id}"
        # Test direct username without @
        assert sl.is_valid("lichess", profile_id) is True
        assert sl.sanitize("lichess", profile_id) == f"https://lichess.org/@/{profile_id}"

