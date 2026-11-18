class TestStackoverflow:
    def test_stackoverflow_full_link(self, sl):
        profile_id = "3573210"
        full_link = f"https://stackoverflow.com/users/{profile_id}/ysskrishna"
        assert sl.is_valid("stackoverflow", full_link) is True
        assert sl.detect_platform(full_link) == "stackoverflow"
        assert sl.sanitize("stackoverflow", full_link) == f"https://stackoverflow.com/users/{profile_id}"
