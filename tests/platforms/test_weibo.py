class TestWeibo:
    def test_weibo_user_id(self, sl):
        user_id = "1669879400"
        assert sl.detect_platform(f"https://weibo.com/u/{user_id}") == "weibo"
        assert sl.is_valid("weibo", f"https://weibo.com/u/{user_id}") is True
        assert sl.sanitize("weibo", f"https://weibo.com/u/{user_id}") == f"https://weibo.com/u/{user_id}"

    def test_weibo_variations(self, sl):
        username = "guanzhilin"
        
        assert sl.detect_platform(f"https://www.weibo.com/{username}") == "weibo"
        assert sl.is_valid("weibo", f"https://www.weibo.com/{username}") is True
        assert sl.sanitize("weibo", f"https://www.weibo.com/{username}") == f"https://weibo.com/{username}"
        
        assert sl.is_valid("weibo", f"https://weibo.com/{username}/") is True
        assert sl.sanitize("weibo", f"https://weibo.com/{username}/") == f"https://weibo.com/{username}"
        
        assert sl.detect_platform(f"http://weibo.com/{username}") == "weibo"
        assert sl.is_valid("weibo", f"http://weibo.com/{username}") is True
        assert sl.sanitize("weibo", f"http://weibo.com/{username}") == f"https://weibo.com/{username}"
        
        user_id = "1669879400"
        assert sl.is_valid("weibo", f"https://www.weibo.com/u/{user_id}") is True
        assert sl.sanitize("weibo", f"https://www.weibo.com/u/{user_id}") == f"https://weibo.com/u/{user_id}"
