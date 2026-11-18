class TestHashnode:
    def test_hashnode(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("hashnode", profile_id) is True
        assert sl.is_valid("hashnode", f"@{profile_id}") is True
        assert sl.sanitize("hashnode", profile_id) == f"https://hashnode.com/@{profile_id}"
        assert sl.sanitize("hashnode", f"@{profile_id}") == f"https://hashnode.com/@{profile_id}"

    def test_hashnode_dev_subdomain(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://{profile_id}.hashnode.dev") == "hashnode"
        assert sl.is_valid("hashnode", f"https://{profile_id}.hashnode.dev") is True
        assert sl.sanitize("hashnode", f"https://{profile_id}.hashnode.dev") == f"https://hashnode.com/@{profile_id}"
