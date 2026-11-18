class TestDouyin:
    def test_douyin_variations(self, sl):
        user_id = "MS4wLjABAAAA9yeV8IIJxpee3_u9zb_Al3_mOA8IffgD3_ueMCQUly4"
        
        assert sl.detect_platform(f"https://douyin.com/user/{user_id}") == "douyin"
        assert sl.is_valid("douyin", f"https://douyin.com/user/{user_id}") is True
        assert sl.sanitize("douyin", f"https://douyin.com/user/{user_id}") == f"https://www.douyin.com/user/{user_id}"
        
        assert sl.is_valid("douyin", f"https://www.douyin.com/user/{user_id}/") is True
        assert sl.sanitize("douyin", f"https://www.douyin.com/user/{user_id}/") == f"https://www.douyin.com/user/{user_id}"
        
        assert sl.detect_platform(f"http://www.douyin.com/user/{user_id}") == "douyin"
        assert sl.is_valid("douyin", f"http://www.douyin.com/user/{user_id}") is True
        assert sl.sanitize("douyin", f"http://www.douyin.com/user/{user_id}") == f"https://www.douyin.com/user/{user_id}"
