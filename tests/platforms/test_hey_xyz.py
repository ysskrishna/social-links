import pytest


class TestHeyXyz:
    @pytest.mark.parametrize(
        "url",
        [
            "https://hey.xyz/posts/0x01-0x01",
            "https://hey.xyz/explore",
        ],
    )
    def test_hey_xyz_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("hey_xyz", url) is False
        assert sl.detect_platform(url) != "hey_xyz"
