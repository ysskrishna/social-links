import pytest


class TestOrcid:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://orcid.org/0000-0002-1694-233X", "https://orcid.org/0000-0002-1694-233X"),
            ("http://orcid.org/0000-0002-1825-0097/", "https://orcid.org/0000-0002-1825-0097"),
        ],
    )
    def test_orcid_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "orcid"
        assert sl.is_valid("orcid", url) is True
        assert sl.sanitize("orcid", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://orcid.org/0000-0002-1825",
            "https://orcid.org/signin",
            "https://orcid.org/0000-0002-1825-0097/print",
        ],
    )
    def test_orcid_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("orcid", url) is False
        assert sl.detect_platform(url) != "orcid"
