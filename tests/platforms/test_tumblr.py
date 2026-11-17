"""Tests for Tumblr platform."""


class TestTumblr:
    """Test Tumblr platform"""

    def test_tumblr_blog_path(self, sl):
        """Test Tumblr /blog/ path"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://tumblr.com/blog/{profile_id}") == "tumblr"
        assert sl.is_valid("tumblr", f"https://tumblr.com/blog/{profile_id}") is True
        assert sl.sanitize("tumblr", f"https://tumblr.com/blog/{profile_id}") == f"https://tumblr.com/{profile_id}"
