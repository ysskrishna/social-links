"""Tests for Kaggle platform."""
import pytest


class TestKaggle:
    """Test Kaggle platform"""

    def test_kaggle(self, sl):
        """Test Kaggle platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.kaggle.com/{profile_id}") == "kaggle"
        assert sl.is_valid("kaggle", f"https://www.kaggle.com/{profile_id}") is True
        assert sl.sanitize("kaggle", f"https://www.kaggle.com/{profile_id}") == f"https://www.kaggle.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("kaggle", profile_id) is True
        assert sl.sanitize("kaggle", profile_id) == f"https://www.kaggle.com/{profile_id}"

