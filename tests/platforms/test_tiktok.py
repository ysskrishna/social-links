class TestTiktok:
    def test_tiktok(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("tiktok", profile_id) is True
        assert sl.is_valid("tiktok", f"@{profile_id}") is True
        assert sl.sanitize("tiktok", profile_id) == f"https://tiktok.com/@{profile_id}"
        assert sl.sanitize("tiktok", f"@{profile_id}") == f"https://tiktok.com/@{profile_id}"
        assert sl.is_valid("tiktok", f"https://www.tiktok.com/@{profile_id}") is True
        assert sl.sanitize("tiktok", f"https://www.tiktok.com/@{profile_id}") == f"https://tiktok.com/@{profile_id}"
        assert sl.is_valid("tiktok", f"http://www.tiktok.com/@{profile_id}") is True
        assert sl.sanitize("tiktok", f"http://www.tiktok.com/@{profile_id}") == f"https://tiktok.com/@{profile_id}"
