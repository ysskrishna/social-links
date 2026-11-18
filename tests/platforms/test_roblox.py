import pytest


class TestRoblox:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.roblox.com/users/156/profile/", "https://www.roblox.com/users/156/profile"),
            ("https://www.roblox.com/users/156", "https://www.roblox.com/users/156/profile"),
        ],
    )
    def test_roblox_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "roblox"
        assert sl.is_valid("roblox", url) is True
        assert sl.sanitize("roblox", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.roblox.com/games/920587237/Adopt-Me",
            "https://www.roblox.com/users/Roblox/profile",
            "https://www.roblox.com/users/1/friends",
        ],
    )
    def test_roblox_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("roblox", url) is False
        assert sl.detect_platform(url) != "roblox"
