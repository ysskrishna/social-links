class TestBluesky:
    def test_bluesky_with_at(self, sl):
        profile_id = "ysskrishna.bsky.social"
        assert sl.is_valid("bluesky", f"@{profile_id}") is True
        assert sl.sanitize("bluesky", f"@{profile_id}") == f"https://bsky.app/profile/{profile_id}"

    def test_bluesky_custom_domain(self, sl):
        profile_id = "example.com"
        assert sl.detect_platform(f"https://bsky.app/profile/{profile_id}") == "bluesky"
        assert sl.is_valid("bluesky", f"https://bsky.app/profile/{profile_id}") is True
        assert sl.sanitize("bluesky", f"https://bsky.app/profile/{profile_id}") == f"https://bsky.app/profile/{profile_id}"
