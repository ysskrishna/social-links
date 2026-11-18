"""Tests for Paragraph platform."""
import pytest


class TestParagraph:
    """Test Paragraph platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://paragraph.xyz/@ysskrishna", "https://paragraph.com/@ysskrishna"),
        ],
    )
    def test_paragraph_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "paragraph"
        assert sl.is_valid("paragraph", url) is True
        assert sl.sanitize("paragraph", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://paragraph.com/@ysskrishna/post-slug",
            "https://paragraph.com/discover",
        ],
    )
    def test_paragraph_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("paragraph", url) is False
        assert sl.detect_platform(url) != "paragraph"
