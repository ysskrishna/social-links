class TestDiscord:
    def test_discord_invite_url(self, sl):
        invite_code = "ysskrishna"
        assert sl.detect_platform(f"https://discord.com/invite/{invite_code}") == "discord"
        assert sl.is_valid("discord", f"https://discord.com/invite/{invite_code}") is True
        assert sl.sanitize("discord", f"https://discord.com/invite/{invite_code}") == f"https://discord.gg/{invite_code}"
