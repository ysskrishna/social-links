class TestYoutube:
    def test_youtube_channel(self, sl):
        profile_id = "UC1234567890"
        assert sl.detect_platform(f"https://youtube.com/channel/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/channel/{profile_id}") is True
        # Channel IDs only resolve under /channel/ (youtube.com/UC... is a 404)
        assert sl.sanitize("youtube", f"https://youtube.com/channel/{profile_id}") == f"https://youtube.com/channel/{profile_id}"
        assert sl.extract_id("youtube", f"https://www.youtube.com/channel/{profile_id}/") == profile_id

    def test_youtube_user(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://youtube.com/user/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/user/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/user/{profile_id}") == f"https://youtube.com/{profile_id}"

    def test_youtube_mobile(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.youtube.com/c/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://m.youtube.com/c/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://m.youtube.com/c/{profile_id}") == f"https://youtube.com/{profile_id}"

    def test_youtube_various_formats(self, sl):
        profile_id = "Google"
        assert sl.detect_platform(f"https://www.youtube.com/user/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://www.youtube.com/user/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://www.youtube.com/user/{profile_id}") == f"https://youtube.com/{profile_id}"
        assert sl.detect_platform(f"https://www.youtube.com/c/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://www.youtube.com/c/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://www.youtube.com/c/{profile_id}") == f"https://youtube.com/{profile_id}"
        assert sl.detect_platform(f"https://www.youtube.com/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://www.youtube.com/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://www.youtube.com/{profile_id}") == f"https://youtube.com/{profile_id}"
        assert sl.detect_platform(f"https://www.youtube.com/{profile_id}/") == "youtube"
        assert sl.is_valid("youtube", f"https://www.youtube.com/{profile_id}/") is True
        assert sl.sanitize("youtube", f"https://www.youtube.com/{profile_id}/") == f"https://youtube.com/{profile_id}"
        assert sl.detect_platform(f"https://youtube.com/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/{profile_id}") == f"https://youtube.com/{profile_id}"
        assert sl.detect_platform(f"http://www.youtube.com/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"http://www.youtube.com/{profile_id}") is True
        assert sl.sanitize("youtube", f"http://www.youtube.com/{profile_id}") == f"https://youtube.com/{profile_id}"
