import pytest


class TestStanStore:
    @pytest.mark.parametrize(
        "url",
        [
            "https://stan.store/vanessalau/p/course",
        ],
    )
    def test_stan_store_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("stan_store", url) is False
        assert sl.detect_platform(url) != "stan_store"
