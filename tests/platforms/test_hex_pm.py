import pytest


class TestHexPm:
    @pytest.mark.parametrize(
        "url",
        [
            "https://hex.pm/packages/phoenix",
            "https://hex.pm/users/josevalim/packages",
        ],
    )
    def test_hex_pm_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("hex_pm", url) is False
        assert sl.detect_platform(url) != "hex_pm"
