"""Tests for RubyGems platform."""
import pytest


class TestRubygems:
    """Test RubyGems platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://rubygems.org/gems/rails",
            "https://rubygems.org/profiles/dhh/gems",
        ],
    )
    def test_rubygems_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("rubygems", url) is False
        assert sl.detect_platform(url) != "rubygems"
