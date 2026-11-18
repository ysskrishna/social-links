class TestCrunchbase:
    def test_crunchbase_company(self, sl):
        profile_id = "tiny-speck"
        assert sl.detect_platform(f"https://www.crunchbase.com/company/{profile_id}") == "crunchbase"
        assert sl.is_valid("crunchbase", f"https://www.crunchbase.com/company/{profile_id}") is True
        assert sl.sanitize("crunchbase", f"https://www.crunchbase.com/company/{profile_id}") == f"https://www.crunchbase.com/organization/{profile_id}"

    def test_crunchbase_person(self, sl):
        profile_id = "elon-musk"
        assert sl.detect_platform(f"https://www.crunchbase.com/person/{profile_id}") == "crunchbase"
        assert sl.is_valid("crunchbase", f"https://www.crunchbase.com/person/{profile_id}") is True
        assert sl.sanitize("crunchbase", f"https://www.crunchbase.com/person/{profile_id}") == f"https://www.crunchbase.com/person/{profile_id}"
