import pytest


class TestKickstarter:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.kickstarter.com/profile/kickstarter/created", "https://www.kickstarter.com/profile/kickstarter"),
        ],
    )
    def test_kickstarter_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "kickstarter"
        assert sl.is_valid("kickstarter", url) is True
        assert sl.sanitize("kickstarter", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.kickstarter.com/projects/abc/def",
            "https://www.kickstarter.com/profile/kickstarter/backed",
        ],
    )
    def test_kickstarter_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("kickstarter", url) is False
        assert sl.detect_platform(url) != "kickstarter"
