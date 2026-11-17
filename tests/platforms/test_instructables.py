"""Tests for Instructables platform."""
import pytest


class TestInstructables:
    """Test Instructables platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.instructables.com/Some-Project-Title/",
            "https://www.instructables.com/member/randofo/instructables/",
        ],
    )
    def test_instructables_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("instructables", url) is False
        assert sl.detect_platform(url) != "instructables"
