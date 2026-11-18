import pytest


class TestFarcaster:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://warpcast.com/dwr.eth", "https://farcaster.xyz/dwr.eth"),
            ("https://warpcast.com/v/", "https://farcaster.xyz/v"),
        ],
    )
    def test_farcaster_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "farcaster"
        assert sl.is_valid("farcaster", url) is True
        assert sl.sanitize("farcaster", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://warpcast.com/dwr.eth/0x1234abcd",
            "https://warpcast.com/~/channel/farcaster",
        ],
    )
    def test_farcaster_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("farcaster", url) is False
        assert sl.detect_platform(url) != "farcaster"
