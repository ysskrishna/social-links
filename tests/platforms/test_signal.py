"""Tests for Signal platform."""
import pytest


class TestSignal:
    """Test Signal platform"""

    def test_signal(self, sl):
        """Test Signal platform"""
        profile_id = "abc123xyz"
        assert sl.detect_platform(f"https://signal.me/#p/{profile_id}") == "signal"
        assert sl.is_valid("signal", f"https://signal.me/#p/{profile_id}") is True
        assert sl.sanitize("signal", f"https://signal.me/#p/{profile_id}") == f"https://signal.me/#p/{profile_id}"
        # Test direct profile ID
        assert sl.is_valid("signal", profile_id) is True
        assert sl.sanitize("signal", profile_id) == f"https://signal.me/#p/{profile_id}"

    def test_signal_with_www(self, sl):
        """Test Signal with www subdomain"""
        profile_id = "abc123xyz"
        assert sl.detect_platform(f"https://www.signal.me/#p/{profile_id}") == "signal"
        assert sl.is_valid("signal", f"https://www.signal.me/#p/{profile_id}") is True
        assert sl.sanitize("signal", f"https://www.signal.me/#p/{profile_id}") == f"https://signal.me/#p/{profile_id}"

    def test_signal_with_http(self, sl):
        """Test Signal with http protocol"""
        profile_id = "abc123xyz"
        assert sl.detect_platform(f"http://signal.me/#p/{profile_id}") == "signal"
        assert sl.is_valid("signal", f"http://signal.me/#p/{profile_id}") is True
        assert sl.sanitize("signal", f"http://signal.me/#p/{profile_id}") == f"https://signal.me/#p/{profile_id}"

    def test_signal_with_trailing_slash(self, sl):
        """Test Signal with trailing slash"""
        profile_id = "abc123xyz"
        assert sl.is_valid("signal", f"https://signal.me/#p/{profile_id}/") is True
        assert sl.sanitize("signal", f"https://signal.me/#p/{profile_id}/") == f"https://signal.me/#p/{profile_id}"

