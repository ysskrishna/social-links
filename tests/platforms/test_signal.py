class TestSignal:
    def test_signal_phone_number(self, sl):
        """Signal phone links contain a leading +"""
        url = "https://signal.me/#p/+15555555555"
        assert sl.detect_platform(url) == "signal"
        assert sl.is_valid("signal", url) is True
        assert sl.sanitize("signal", url) == url
        assert sl.extract_id("signal", url) == "+15555555555"
