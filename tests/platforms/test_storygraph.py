"""Tests for The StoryGraph platform."""
import pytest


class TestStorygraph:
    """Test The StoryGraph platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://app.thestorygraph.com/books/abc",
            "https://app.thestorygraph.com/profile/ysskrishna/reviews",
        ],
    )
    def test_storygraph_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("storygraph", url) is False
        assert sl.detect_platform(url) != "storygraph"
