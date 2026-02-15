"""Tests for Chess.com platform."""
import pytest


class TestChessCom:
    """Test Chess.com platform"""

    def test_chess_com(self, sl):
        """Test Chess.com platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.chess.com/member/{profile_id}") == "chess_com"
        assert sl.is_valid("chess_com", f"https://www.chess.com/member/{profile_id}") is True
        assert sl.sanitize("chess_com", f"https://www.chess.com/member/{profile_id}") == f"https://www.chess.com/member/{profile_id}"
        # Test direct username
        assert sl.is_valid("chess_com", profile_id) is True
        assert sl.sanitize("chess_com", profile_id) == f"https://www.chess.com/member/{profile_id}"

