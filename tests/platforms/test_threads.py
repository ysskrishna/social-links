class TestThreads:
    def test_threads(self, sl):
        profile_id = "ysskrishna"
        assert sl.sanitize("threads", f"https://www.threads.com/@{profile_id}") == f"https://threads.com/@{profile_id}"
        assert sl.is_valid("threads", f"@{profile_id}") is True
        assert sl.sanitize("threads", f"@{profile_id}") == f"https://threads.com/@{profile_id}"

    def test_threads_legacy_net_domain(self, sl):
        """threads.net redirects to threads.com and is still accepted as input"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://threads.net/@{profile_id}") == "threads"
        assert sl.is_valid("threads", f"https://www.threads.net/@{profile_id}") is True
        assert sl.sanitize("threads", f"https://threads.net/@{profile_id}") == f"https://threads.com/@{profile_id}"
