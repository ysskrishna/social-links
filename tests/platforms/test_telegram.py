class TestTelegram:
    def test_telegram_with_underscore(self, sl):
        profile_id = "list_telegram"
        assert sl.detect_platform(f"https://t.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://t.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://t.me/{profile_id}") == f"https://t.me/{profile_id}"

    def test_telegram_dog(self, sl):
        profile_id = "mrhallo"
        assert sl.detect_platform(f"https://telegram.dog/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://telegram.dog/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://telegram.dog/{profile_id}") == f"https://t.me/{profile_id}"

    def test_telegram_me(self, sl):
        profile_id = "shajareyan"
        assert sl.detect_platform(f"https://telegram.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://telegram.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://telegram.me/{profile_id}") == f"https://t.me/{profile_id}"
        assert sl.detect_platform(f"https://www.telegram.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://www.telegram.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://www.telegram.me/{profile_id}") == f"https://t.me/{profile_id}"

    def test_telegram_web_client_numeric_id(self, sl):
        # Web client with numeric ID (can be negative for groups/channels)
        numeric_id = "-2128475717"
        web_url = f"https://web.telegram.org/k/#{numeric_id}"
        assert sl.detect_platform(web_url) == "telegram"
        assert sl.is_valid("telegram", web_url) is True
        assert sl.sanitize("telegram", web_url) == f"https://t.me/{numeric_id}"
        
        positive_id = "6891155458"
        web_url_positive = f"http://web.telegram.org/a/#{positive_id}"
        assert sl.detect_platform(web_url_positive) == "telegram"
        assert sl.is_valid("telegram", web_url_positive) is True
        assert sl.sanitize("telegram", web_url_positive) == f"https://t.me/{positive_id}"

    def test_telegram_web_client_username(self, sl):
        username = "Banana_traffbot"
        web_url = f"https://web.telegram.org/k/#@{username}"
        assert sl.detect_platform(web_url) == "telegram"
        assert sl.is_valid("telegram", web_url) is True
        assert sl.sanitize("telegram", web_url) == f"https://t.me/{username}"
