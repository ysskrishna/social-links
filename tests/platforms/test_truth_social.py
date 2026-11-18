import pytest


class TestTruthSocial:
    @pytest.mark.parametrize(
        "url",
        [
            "https://truthsocial.com/@realDonaldTrump/posts/1",
            "https://truthsocial.com/realDonaldTrump",
        ],
    )
    def test_truth_social_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("truth_social", url) is False
        assert sl.detect_platform(url) != "truth_social"
