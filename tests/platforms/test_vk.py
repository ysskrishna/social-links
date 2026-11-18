class TestVk:
    def test_vk(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("vk", profile_id) is True
        assert sl.is_valid("vk", f"@{profile_id}") is True
        assert sl.sanitize("vk", profile_id) == f"https://vk.com/{profile_id}"
        assert sl.sanitize("vk", f"@{profile_id}") == f"https://vk.com/{profile_id}"

    def test_vk_mobile(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.vk.com/{profile_id}") == "vk"
        assert sl.is_valid("vk", f"https://m.vk.com/{profile_id}") is True
        assert sl.sanitize("vk", f"https://m.vk.com/{profile_id}") == f"https://vk.com/{profile_id}"
