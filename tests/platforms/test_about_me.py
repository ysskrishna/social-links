import pytest


class TestAboutMe:
    @pytest.mark.parametrize(
        "url",
        [
            "https://about.me/tonyconrad/contact",
        ],
    )
    def test_about_me_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("about_me", url) is False
        assert sl.detect_platform(url) != "about_me"
