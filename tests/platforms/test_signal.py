"""Tests for Signal platform."""


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

    def test_signal_phone_number(self, sl):
        """Signal phone links contain a leading +"""
        url = "https://signal.me/#p/+15555555555"
        assert sl.detect_platform(url) == "signal"
        assert sl.is_valid("signal", url) is True
        assert sl.sanitize("signal", url) == url
        assert sl.extract_id("signal", url) == "+15555555555"
