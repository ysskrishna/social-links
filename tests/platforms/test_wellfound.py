class TestWellfound:
    def test_wellfound_company(self, sl):
        profile_id = "homelight"
        assert sl.detect_platform(f"https://wellfound.com/company/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://wellfound.com/company/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://wellfound.com/company/{profile_id}") == f"https://wellfound.com/company/{profile_id}"

    def test_wellfound_legacy_angellist_user(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://angel.co/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"

    def test_wellfound_legacy_angellist_company(self, sl):
        profile_id = "slack"
        assert sl.detect_platform(f"https://angel.co/company/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/company/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/company/{profile_id}") == f"https://wellfound.com/company/{profile_id}"
        assert sl.detect_platform(f"https://angel.co/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/{profile_id}") == f"https://wellfound.com/company/{profile_id}"
