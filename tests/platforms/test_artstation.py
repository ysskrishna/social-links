class TestArtStation:
    def test_artstation(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("artstation", f"https://{profile_id}.artstation.com") is True
        assert sl.sanitize("artstation", f"https://{profile_id}.artstation.com") == f"https://www.artstation.com/{profile_id}"
