class TestLeetCode:
    def test_leetcode(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("leetcode", f"https://leetcode.com/u/{profile_id}") is True
        assert sl.sanitize("leetcode", f"https://leetcode.com/u/{profile_id}") == f"https://leetcode.com/{profile_id}"
