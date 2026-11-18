"""Tests for WordPress.org platform."""
import pytest


class TestWordpressOrg:
    """Test WordPress.org platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://wordpress.org/plugins/akismet/",
            "https://profiles.wordpress.org/matt/activity",
        ],
    )
    def test_wordpress_org_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("wordpress_org", url) is False
        assert sl.detect_platform(url) != "wordpress_org"
