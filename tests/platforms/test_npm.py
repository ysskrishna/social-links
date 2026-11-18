import pytest


class TestNpm:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.npmjs.com/package/react",
            "https://www.npmjs.com/~sindresorhus/packages",
            "https://www.npmjs.com/sindresorhus",
        ],
    )
    def test_npm_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("npm", url) is False
        assert sl.detect_platform(url) != "npm"
