class TestSubstack:
    def test_substack(self, sl):
        """Test Substack platform - all formats sanitize to @username format"""
        profile_id = "ysskrishna"
        
        
        assert sl.detect_platform(f"https://substack.com/@{profile_id}") == "substack"
        assert sl.is_valid("substack", f"https://substack.com/@{profile_id}") is True
        assert sl.sanitize("substack", f"https://substack.com/@{profile_id}") == f"https://substack.com/@{profile_id}"
        
        assert sl.is_valid("substack", f"https://www.substack.com/@{profile_id}") is True
        assert sl.sanitize("substack", f"https://www.substack.com/@{profile_id}") == f"https://substack.com/@{profile_id}"
        
        assert sl.is_valid("substack", f"http://substack.com/@{profile_id}") is True
        assert sl.sanitize("substack", f"http://substack.com/@{profile_id}") == f"https://substack.com/@{profile_id}"
        
        assert sl.is_valid("substack", f"https://substack.com/@{profile_id}/") is True
        assert sl.sanitize("substack", f"https://substack.com/@{profile_id}/") == f"https://substack.com/@{profile_id}"
        
