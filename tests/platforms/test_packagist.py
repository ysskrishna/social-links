import pytest


class TestPackagist:
    @pytest.mark.parametrize(
        "url",
        [
            "https://packagist.org/packages/monolog/monolog",
            "https://packagist.org/users/seldaek/packages",
        ],
    )
    def test_packagist_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("packagist", url) is False
        assert sl.detect_platform(url) != "packagist"
