import pytest


class TestGoogleScholar:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://scholar.google.com/citations?hl=en&user=JicYPdAAAAAJ", "https://scholar.google.com/citations?user=JicYPdAAAAAJ"),
            ("https://scholar.google.co.uk/citations?user=JicYPdAAAAAJ", "https://scholar.google.com/citations?user=JicYPdAAAAAJ"),
        ],
    )
    def test_google_scholar_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "google_scholar"
        assert sl.is_valid("google_scholar", url) is True
        assert sl.sanitize("google_scholar", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://scholar.google.com/scholar?q=deep+learning",
            "https://scholar.google.com/citations?view_op=search_authors&mauthors=hinton",
            "https://scholar.google.evil.com/citations?user=JicYPdAAAAAJ",
        ],
    )
    def test_google_scholar_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("google_scholar", url) is False
        assert sl.detect_platform(url) != "google_scholar"
