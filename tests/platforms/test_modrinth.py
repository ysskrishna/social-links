import pytest


class TestModrinth:
    @pytest.mark.parametrize(
        "url",
        [
            "https://modrinth.com/mod/sodium",
            "https://modrinth.com/user/jellysquid3/mods",
        ],
    )
    def test_modrinth_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("modrinth", url) is False
        assert sl.detect_platform(url) != "modrinth"
