import pytest


class TestGitee:
    @pytest.mark.parametrize(
        "url",
        [
            "https://gitee.com/openharmony/docs",
        ],
    )
    def test_gitee_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("gitee", url) is False
        assert sl.detect_platform(url) != "gitee"
