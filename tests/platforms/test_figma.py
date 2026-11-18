import pytest


class TestFigma:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.figma.com/community/file/123",
            "https://www.figma.com/@figma/plugins",
            "https://www.figma.com/figma",
        ],
    )
    def test_figma_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("figma", url) is False
        assert sl.detect_platform(url) != "figma"
