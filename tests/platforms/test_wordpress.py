class TestWordPress:
    def test_wordpress(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("wordpress", f"https://{profile_id}.wordpress.com") is True
        assert sl.sanitize("wordpress", f"https://{profile_id}.wordpress.com") == f"https://wordpress.com/people/{profile_id}"
