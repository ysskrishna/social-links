import pytest


class TestFuraffinity:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.furaffinity.net/view/123/",
            "https://www.furaffinity.net/gallery/dragoneer/",
        ],
    )
    def test_furaffinity_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("furaffinity", url) is False
        assert sl.detect_platform(url) != "furaffinity"
