class TestUnsplash:
    def test_unsplash(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("unsplash", f"@{profile_id}") is True
        assert sl.sanitize("unsplash", f"@{profile_id}") == f"https://unsplash.com/@{profile_id}"
