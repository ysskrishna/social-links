class TestProducthunt:
    def test_producthunt(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("producthunt", profile_id) is True
        assert sl.is_valid("producthunt", f"@{profile_id}") is True
        assert sl.sanitize("producthunt", profile_id) == f"https://www.producthunt.com/@{profile_id}"
        assert sl.sanitize("producthunt", f"@{profile_id}") == f"https://www.producthunt.com/@{profile_id}"
