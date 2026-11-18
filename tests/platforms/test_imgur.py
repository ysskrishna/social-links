import pytest


class TestImgur:
    @pytest.mark.parametrize(
        "url",
        [
            "https://imgur.com/gallery/abc123",
            "https://imgur.com/user/sarah/favorites",
        ],
    )
    def test_imgur_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("imgur", url) is False
        assert sl.detect_platform(url) != "imgur"
