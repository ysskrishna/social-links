import pytest


class TestKhanAcademy:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.khanacademy.org/math/algebra",
            "https://www.khanacademy.org/profile/ysskrishna/projects",
        ],
    )
    def test_khan_academy_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("khan_academy", url) is False
        assert sl.detect_platform(url) != "khan_academy"
