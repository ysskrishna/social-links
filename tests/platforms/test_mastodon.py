class TestMastodon:
    def test_mastodon(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("mastodon", profile_id) is True
        assert sl.is_valid("mastodon", f"@{profile_id}") is True
        assert sl.sanitize("mastodon", profile_id) == f"https://mastodon.social/@{profile_id}"
        assert sl.sanitize("mastodon", f"@{profile_id}") == f"https://mastodon.social/@{profile_id}"

    def test_mastodon_variants(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://mstdn.social/@{profile_id}") == "mastodon"
        assert sl.detect_platform(f"https://mastodon.world/@{profile_id}") == "mastodon"
        assert sl.is_valid("mastodon", f"https://mstdn.social/@{profile_id}") is True
        assert sl.is_valid("mastodon", f"https://mastodon.world/@{profile_id}") is True
