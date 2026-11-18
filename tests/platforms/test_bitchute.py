import pytest


class TestBitchute:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.bitchute.com/video/abc123/",
            "https://www.bitchute.com/channel/bitchute/videos",
        ],
    )
    def test_bitchute_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("bitchute", url) is False
        assert sl.detect_platform(url) != "bitchute"
