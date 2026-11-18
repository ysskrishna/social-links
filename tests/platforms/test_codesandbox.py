import pytest


class TestCodesandbox:
    @pytest.mark.parametrize(
        "url",
        [
            "https://codesandbox.io/s/new",
            "https://codesandbox.io/p/sandbox/abc",
        ],
    )
    def test_codesandbox_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("codesandbox", url) is False
        assert sl.detect_platform(url) != "codesandbox"
