"""Tests for Open Collective platform."""
import pytest


class TestOpencollective:
    """Test Open Collective platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://opencollective.com/webpack/expenses",
            "https://opencollective.com/discover",
            "https://opencollective.com/pricing",
        ],
    )
    def test_opencollective_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("opencollective", url) is False
        assert sl.detect_platform(url) != "opencollective"
