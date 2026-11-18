import pytest


class TestSemanticScholar:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.semanticscholar.org/author/1741101", "https://www.semanticscholar.org/author/1741101"),
        ],
    )
    def test_semantic_scholar_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "semantic_scholar"
        assert sl.is_valid("semantic_scholar", url) is True
        assert sl.sanitize("semantic_scholar", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.semanticscholar.org/paper/abc123",
            "https://www.semanticscholar.org/author/Oren-Etzioni",
        ],
    )
    def test_semantic_scholar_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("semantic_scholar", url) is False
        assert sl.detect_platform(url) != "semantic_scholar"
