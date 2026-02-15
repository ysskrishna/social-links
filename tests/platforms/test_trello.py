"""Tests for Trello platform."""
import pytest


class TestTrello:
    """Test Trello platform"""

    def test_trello(self, sl):
        """Test Trello platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://trello.com/{profile_id}") == "trello"
        assert sl.is_valid("trello", f"https://trello.com/{profile_id}") is True
        assert sl.sanitize("trello", f"https://trello.com/{profile_id}") == f"https://trello.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("trello", profile_id) is True
        assert sl.sanitize("trello", profile_id) == f"https://trello.com/{profile_id}"

