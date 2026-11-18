import pytest


class TestOpencollective:
    @pytest.mark.parametrize(
        "url",
        [
            "https://opencollective.com/webpack/expenses",
        ],
    )
    def test_opencollective_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("opencollective", url) is False
        assert sl.detect_platform(url) != "opencollective"
