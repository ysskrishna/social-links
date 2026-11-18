import pytest


class TestRoyalRoad:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.royalroad.com/fiction/21220/mother-of-learning",
            "https://www.royalroad.com/profile/1/fictions",
        ],
    )
    def test_royal_road_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("royal_road", url) is False
        assert sl.detect_platform(url) != "royal_road"
