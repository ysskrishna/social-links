class TestX:
    def test_x(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("x", profile_id) is True
        assert sl.is_valid("x", f"@{profile_id}") is True
        assert sl.sanitize("x", profile_id) == f"https://x.com/{profile_id}"
        assert sl.sanitize("x", f"@{profile_id}") == f"https://x.com/{profile_id}"

    def test_x_twitter_urls(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://twitter.com/{profile_id}") == "x"
        assert sl.detect_platform(f"https://mobile.twitter.com/{profile_id}") == "x"
        assert sl.is_valid("x", f"https://twitter.com/{profile_id}") is True
        assert sl.is_valid("x", f"https://mobile.twitter.com/{profile_id}") is True
        assert sl.sanitize("x", f"https://twitter.com/{profile_id}") == f"https://x.com/{profile_id}"
        assert sl.sanitize("x", f"https://mobile.twitter.com/{profile_id}") == f"https://x.com/{profile_id}"
