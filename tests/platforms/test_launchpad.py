import pytest


class TestLaunchpad:
    @pytest.mark.parametrize(
        "url",
        [
            "https://launchpad.net/ubuntu",
            "https://launchpad.net/~sabdfl/+archive/ubuntu/ppa",
        ],
    )
    def test_launchpad_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("launchpad", url) is False
        assert sl.detect_platform(url) != "launchpad"
