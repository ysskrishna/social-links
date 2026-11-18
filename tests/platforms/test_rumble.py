class TestRumble:
    def test_rumble(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("rumble", f"https://rumble.com/c/{profile_id}") is True
        assert sl.sanitize("rumble", f"https://rumble.com/c/{profile_id}") == f"https://rumble.com/user/{profile_id}"
