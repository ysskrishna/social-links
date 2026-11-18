import pytest


class TestCurseforge:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.curseforge.com/members/ysskrishna", "https://www.curseforge.com/members/ysskrishna"),
        ],
    )
    def test_curseforge_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "curseforge"
        assert sl.is_valid("curseforge", url) is True
        assert sl.sanitize("curseforge", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.curseforge.com/minecraft/mc-mods/jei",
            "https://www.curseforge.com/members/ysskrishna/followers",
        ],
    )
    def test_curseforge_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("curseforge", url) is False
        assert sl.detect_platform(url) != "curseforge"
