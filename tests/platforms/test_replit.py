class TestReplit:
    def test_replit(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("replit", f"@{profile_id}") is True
        assert sl.sanitize("replit", f"@{profile_id}") == f"https://replit.com/@{profile_id}"
