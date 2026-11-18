class TestSnapchat:
    def test_snapchat(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("snapchat", profile_id) is True
        assert sl.is_valid("snapchat", f"@{profile_id}") is True
        assert sl.sanitize("snapchat", profile_id) == f"https://snapchat.com/@{profile_id}"
        assert sl.sanitize("snapchat", f"@{profile_id}") == f"https://snapchat.com/@{profile_id}"

    def test_snapchat_at_path(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://snapchat.com/@{profile_id}") == "snapchat"
        assert sl.is_valid("snapchat", f"https://snapchat.com/@{profile_id}") is True
        assert sl.sanitize("snapchat", f"https://snapchat.com/@{profile_id}") == f"https://snapchat.com/@{profile_id}"
