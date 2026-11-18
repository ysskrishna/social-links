class TestWechat:
    def test_wechat_weixin_protocol(self, sl):
        username = "Bright_Writers"
        assert sl.detect_platform(f"weixin://dl/chat?{username}") == "wechat"
        assert sl.is_valid("wechat", f"weixin://dl/chat?{username}") is True
        assert sl.sanitize("wechat", f"weixin://dl/chat?{username}") == f"https://open.weixin.qq.com/qr/code?username={username}"
