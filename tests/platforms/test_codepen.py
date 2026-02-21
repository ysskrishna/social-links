"""Tests for CodePen platform."""
import pytest


class TestCodePen:
    """Test CodePen platform"""

    def test_codepen(self, sl):
        """Test CodePen platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://codepen.io/{profile_id}") == "codepen"
        assert sl.is_valid("codepen", f"https://codepen.io/{profile_id}") is True
        assert sl.sanitize("codepen", f"https://codepen.io/{profile_id}") == f"https://codepen.io/{profile_id}"
        # Test direct username
        assert sl.is_valid("codepen", profile_id) is True
        assert sl.sanitize("codepen", profile_id) == f"https://codepen.io/{profile_id}"

