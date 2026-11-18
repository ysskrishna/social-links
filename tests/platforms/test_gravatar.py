class TestGravatar:
    def test_gravatar_with_language(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://en.gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"https://en.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://en.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"
        assert sl.is_valid("gravatar", f"https://fr.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://fr.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"
