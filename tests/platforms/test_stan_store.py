"""Tests for Stan Store platform."""
import pytest


class TestStanStore:
    """Test Stan Store platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://stan.store/vanessalau/p/course",
            "https://stan.store/pricing",
        ],
    )
    def test_stan_store_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("stan_store", url) is False
        assert sl.detect_platform(url) != "stan_store"
