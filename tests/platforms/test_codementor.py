import pytest


class TestCodementor:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.codementor.io/@ysskrishna/some-post-abc",
            "https://www.codementor.io/python-experts",
        ],
    )
    def test_codementor_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("codementor", url) is False
        assert sl.detect_platform(url) != "codementor"
