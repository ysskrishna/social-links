import pytest


class TestResearchgate:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.researchgate.net/publication/123_Title",
            "https://www.researchgate.net/institution/MIT",
        ],
    )
    def test_researchgate_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("researchgate", url) is False
        assert sl.detect_platform(url) != "researchgate"
