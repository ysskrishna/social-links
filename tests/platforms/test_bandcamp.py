class TestBandcamp:
    def test_bandcamp_with_dashes(self, sl):
        profile_id = "my-band-name"
        assert sl.detect_platform(f"https://{profile_id}.bandcamp.com") == "bandcamp"
        assert sl.is_valid("bandcamp", f"https://{profile_id}.bandcamp.com") is True
        assert sl.sanitize("bandcamp", f"https://{profile_id}.bandcamp.com") == f"https://{profile_id}.bandcamp.com"
