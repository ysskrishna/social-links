import pytest


class TestInaturalist:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.inaturalist.org/people/1", "https://www.inaturalist.org/people/1"),
        ],
    )
    def test_inaturalist_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "inaturalist"
        assert sl.is_valid("inaturalist", url) is True
        assert sl.sanitize("inaturalist", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.inaturalist.org/observations/123",
            "https://www.inaturalist.org/people/kueda/followers",
        ],
    )
    def test_inaturalist_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("inaturalist", url) is False
        assert sl.detect_platform(url) != "inaturalist"
