class TestLichess:
    def test_lichess(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("lichess", f"@{profile_id}") is True
        assert sl.sanitize("lichess", f"@{profile_id}") == f"https://lichess.org/@/{profile_id}"
