class TestPinterest:
    def test_pinterest_localized(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("pinterest", f"https://pl.pinterest.com/{profile_id}") is True
        assert sl.is_valid("pinterest", f"https://www.pinterest.com/{profile_id}") is True
        assert sl.is_valid("pinterest", f"https://abcd.pinterest.com/{profile_id}") is False
