"""Tests for Naver Blog platform."""
import pytest


class TestNaverBlog:
    """Test Naver Blog platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://m.blog.naver.com/naver_diary", "https://blog.naver.com/naver_diary"),
            ("https://blog.naver.com/prologue/PrologueList.naver?blogId=naver_diary", "https://blog.naver.com/naver_diary"),
        ],
    )
    def test_naver_blog_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "naver_blog"
        assert sl.is_valid("naver_blog", url) is True
        assert sl.sanitize("naver_blog", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://blog.naver.com/naver_diary/223456789",
        ],
    )
    def test_naver_blog_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("naver_blog", url) is False
        assert sl.detect_platform(url) != "naver_blog"
