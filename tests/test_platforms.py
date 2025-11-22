from sociallinks.core import SocialLinks


class TestAllPlatforms:
    """Test all predefined platforms"""

    def test_behance(self):
        """Test Behance platform"""
        sl = SocialLinks()
        profile_id = "grzegorzkumierz"
        assert sl.detect_platform("https://behance.net/grzegorzkumierz") == "behance"
        assert sl.is_valid("behance", "https://behance.net/grzegorzkumierz") is True
        assert sl.sanitize("behance", "https://behance.net/grzegorzkumierz") == "https://behance.net/grzegorzkumierz"

    def test_dev_to(self):
        """Test Dev.to platform"""
        sl = SocialLinks()
        profile_id = "gkucmierz"
        assert sl.detect_platform("https://dev.to/gkucmierz") == "dev_to"
        assert sl.is_valid("dev_to", "https://dev.to/gkucmierz") is True
        assert sl.sanitize("dev_to", "https://dev.to/gkucmierz") == "https://dev.to/gkucmierz"

    def test_dribbble(self):
        """Test Dribbble platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://dribbble.com/username") == "dribbble"
        assert sl.is_valid("dribbble", "https://dribbble.com/username") is True
        assert sl.sanitize("dribbble", "https://dribbble.com/username") == "https://dribbble.com/username"

    def test_exercism(self):
        """Test Exercism platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://exercism.io/profiles/username") == "exercism"
        assert sl.is_valid("exercism", "https://exercism.io/profiles/username") is True
        assert sl.sanitize("exercism", "https://exercism.io/profiles/username") == "https://exercism.io/profiles/username"

    def test_facebook(self):
        """Test Facebook desktop platform"""
        sl = SocialLinks()
        profile_id = "johndoe"
        assert sl.detect_platform("https://facebook.com/johndoe") == "facebook"
        assert sl.is_valid("facebook", "https://facebook.com/johndoe") is True
        assert sl.sanitize("facebook", "https://facebook.com/johndoe") == "https://facebook.com/johndoe"

    def test_facebook_mobile(self):
        """Test Facebook mobile platform"""
        sl = SocialLinks()
        profile_id = "johndoe"
        assert sl.detect_platform("https://m.facebook.com/johndoe") == "facebook"
        assert sl.is_valid("facebook", "https://m.facebook.com/johndoe") is True
        assert sl.sanitize("facebook", "https://m.facebook.com/johndoe") == "https://facebook.com/johndoe"

    def test_github(self):
        """Test GitHub platform"""
        sl = SocialLinks()
        profile_id = "octocat"
        assert sl.detect_platform("https://github.com/octocat") == "github"
        assert sl.is_valid("github", "https://github.com/octocat") is True
        assert sl.sanitize("github", "https://github.com/octocat") == "https://github.com/octocat"

    def test_instagram(self):
        """Test Instagram platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://instagram.com/username") == "instagram"
        assert sl.is_valid("instagram", "https://instagram.com/username") is True
        assert sl.sanitize("instagram", "https://instagram.com/username") == "https://instagram.com/username"

    def test_instagram_mobile(self):
        """Test Instagram mobile platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://m.instagram.com/username") == "instagram"
        assert sl.is_valid("instagram", "https://m.instagram.com/username") is True
        assert sl.sanitize("instagram", "https://m.instagram.com/username") == "https://instagram.com/username"

    def test_keybase(self):
        """Test Keybase platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://keybase.io/username") == "keybase"
        assert sl.is_valid("keybase", "https://keybase.io/username") is True
        assert sl.sanitize("keybase", "https://keybase.io/username") == "https://keybase.io/username"

    def test_lemmy_world(self):
        """Test Lemmy World platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://lemmy.world/u/username") == "lemmy_world"
        assert sl.is_valid("lemmy_world", "https://lemmy.world/u/username") is True
        assert sl.sanitize("lemmy_world", "https://lemmy.world/u/username") == "https://lemmy.world/u/username"

    def test_linkedin_personal(self):
        """Test LinkedIn personal profile"""
        sl = SocialLinks()
        profile_id = "johndoe"
        assert sl.detect_platform("https://linkedin.com/in/johndoe") == "linkedin"
        assert sl.is_valid("linkedin", "https://linkedin.com/in/johndoe") is True
        assert sl.sanitize("linkedin", "https://linkedin.com/in/johndoe") == "https://linkedin.com/in/johndoe"

    def test_linkedin_company(self):
        """Test LinkedIn company profile"""
        sl = SocialLinks()
        profile_id = "acme"
        assert sl.detect_platform("https://linkedin.com/company/acme") == "linkedin"
        assert sl.is_valid("linkedin", "https://linkedin.com/company/acme") is True
        assert sl.sanitize("linkedin", "https://linkedin.com/company/acme") == "https://www.linkedin.com/company/acme/"

    def test_linkedin_mobile(self):
        """Test LinkedIn mobile platform"""
        sl = SocialLinks()
        profile_id = "johndoe"
        assert sl.detect_platform("https://linkedin.com/mwlite/in/johndoe") == "linkedin"
        assert sl.is_valid("linkedin", "https://linkedin.com/mwlite/in/johndoe") is True
        assert sl.sanitize("linkedin", "https://linkedin.com/mwlite/in/johndoe") == "https://linkedin.com/in/johndoe"

    def test_linktree(self):
        """Test Linktree platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://linktr.ee/username") == "linktree"
        assert sl.is_valid("linktree", "https://linktr.ee/username") is True
        assert sl.sanitize("linktree", "https://linktr.ee/username") == "https://linktr.ee/username"

    def test_mastodon(self):
        """Test Mastodon platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://mastodon.social/@username") == "mastodon"
        assert sl.is_valid("mastodon", "https://mastodon.social/@username") is True
        assert sl.sanitize("mastodon", "https://mastodon.social/@username") == "https://mastodon.social/@username"

    def test_mastodon_variants(self):
        """Test Mastodon platform variants"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://mstdn.social/@username") == "mastodon"
        assert sl.detect_platform("https://mastodon.world/@username") == "mastodon"
        assert sl.is_valid("mastodon", "https://mstdn.social/@username") is True
        assert sl.is_valid("mastodon", "https://mastodon.world/@username") is True

    def test_medium(self):
        """Test Medium platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://medium.com/@username") == "medium"
        assert sl.is_valid("medium", "https://medium.com/@username") is True
        assert sl.sanitize("medium", "https://medium.com/@username") == "https://medium.com/@username"

    def test_patreon(self):
        """Test Patreon platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://patreon.com/username") == "patreon"
        assert sl.is_valid("patreon", "https://patreon.com/username") is True
        assert sl.sanitize("patreon", "https://patreon.com/username") == "https://patreon.com/username"

    def test_pinterest(self):
        """Test Pinterest platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://pinterest.com/username") == "pinterest"
        assert sl.is_valid("pinterest", "https://pinterest.com/username") is True
        assert sl.sanitize("pinterest", "https://pinterest.com/username") == "https://pinterest.com/username"

    def test_soundcloud(self):
        """Test SoundCloud platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://soundcloud.com/username") == "soundcloud"
        assert sl.is_valid("soundcloud", "https://soundcloud.com/username") is True
        assert sl.sanitize("soundcloud", "https://soundcloud.com/username") == "https://soundcloud.com/username"

    def test_spotify(self):
        """Test Spotify platform"""
        sl = SocialLinks()
        profile_id = "artist123"
        assert sl.detect_platform("https://open.spotify.com/artist/artist123") == "spotify"
        assert sl.is_valid("spotify", "https://open.spotify.com/artist/artist123") is True
        assert sl.sanitize("spotify", "https://open.spotify.com/artist/artist123") == "https://open.spotify.com/artist/artist123"

    def test_stackoverflow(self):
        """Test Stack Overflow platform"""
        sl = SocialLinks()
        profile_id = "12345"
        assert sl.detect_platform("https://stackoverflow.com/users/12345") == "stackoverflow"
        assert sl.is_valid("stackoverflow", "https://stackoverflow.com/users/12345") is True
        assert sl.sanitize("stackoverflow", "https://stackoverflow.com/users/12345") == "https://stackoverflow.com/users/12345"

    def test_substack(self):
        """Test Substack platform"""
        sl = SocialLinks()
        profile_id = "newsletter"
        assert sl.detect_platform("https://newsletter.substack.com") == "substack"
        assert sl.is_valid("substack", "https://newsletter.substack.com") is True
        assert sl.sanitize("substack", "https://newsletter.substack.com") == "https://newsletter.substack.com"

    def test_telegram(self):
        """Test Telegram platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://t.me/username") == "telegram"
        assert sl.is_valid("telegram", "https://t.me/username") is True
        assert sl.sanitize("telegram", "https://t.me/username") == "https://t.me/username"

    def test_telegram_alternate(self):
        """Test Telegram alternate domain"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://telegram.me/username") == "telegram"
        assert sl.is_valid("telegram", "https://telegram.me/username") is True
        assert sl.sanitize("telegram", "https://telegram.me/username") == "https://t.me/username"

    def test_tiktok(self):
        """Test TikTok platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://tiktok.com/@username") == "tiktok"
        assert sl.is_valid("tiktok", "https://tiktok.com/@username") is True
        assert sl.sanitize("tiktok", "https://tiktok.com/@username") == "https://tiktok.com/@username"

    def test_twitch(self):
        """Test Twitch platform"""
        sl = SocialLinks()
        profile_id = "streamer"
        assert sl.detect_platform("https://twitch.tv/streamer") == "twitch"
        assert sl.is_valid("twitch", "https://twitch.tv/streamer") is True
        assert sl.sanitize("twitch", "https://twitch.tv/streamer") == "https://twitch.tv/streamer"

    def test_twitch_mobile(self):
        """Test Twitch mobile platform"""
        sl = SocialLinks()
        profile_id = "streamer"
        assert sl.detect_platform("https://m.twitch.tv/streamer") == "twitch"
        assert sl.is_valid("twitch", "https://m.twitch.tv/streamer") is True
        assert sl.sanitize("twitch", "https://m.twitch.tv/streamer") == "https://twitch.tv/streamer"

    def test_vk(self):
        """Test VK platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://vk.com/username") == "vk"
        assert sl.is_valid("vk", "https://vk.com/username") is True
        assert sl.sanitize("vk", "https://vk.com/username") == "https://vk.com/username"

    def test_vk_mobile(self):
        """Test VK mobile platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://m.vk.com/username") == "vk"
        assert sl.is_valid("vk", "https://m.vk.com/username") is True
        assert sl.sanitize("vk", "https://m.vk.com/username") == "https://vk.com/username"

    def test_x(self):
        """Test X (formerly Twitter) platform"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://x.com/username") == "x"
        assert sl.is_valid("x", "https://x.com/username") is True
        assert sl.sanitize("x", "https://x.com/username") == "https://x.com/username"

    def test_x_twitter_urls(self):
        """Test X platform with Twitter URLs (X handles both x.com and twitter.com)"""
        sl = SocialLinks()
        profile_id = "username"
        # Twitter URLs should be detected as X platform
        assert sl.detect_platform("https://twitter.com/username") == "x"
        assert sl.detect_platform("https://mobile.twitter.com/username") == "x"
        assert sl.is_valid("x", "https://twitter.com/username") is True
        assert sl.is_valid("x", "https://mobile.twitter.com/username") is True
        # Twitter URLs should be sanitized to x.com
        assert sl.sanitize("x", "https://twitter.com/username") == "https://x.com/username"
        assert sl.sanitize("x", "https://mobile.twitter.com/username") == "https://x.com/username"

    def test_youtube(self):
        """Test YouTube platform"""
        sl = SocialLinks()
        profile_id = "channelname"
        assert sl.detect_platform("https://youtube.com/@channelname") == "youtube"
        assert sl.is_valid("youtube", "https://youtube.com/@channelname") is True
        assert sl.sanitize("youtube", "https://youtube.com/@channelname") == "https://youtube.com/@channelname"

    def test_youtube_channel(self):
        """Test YouTube channel URL"""
        sl = SocialLinks()
        profile_id = "UC1234567890"
        assert sl.detect_platform("https://youtube.com/channel/UC1234567890") == "youtube"
        assert sl.is_valid("youtube", "https://youtube.com/channel/UC1234567890") is True
        assert sl.sanitize("youtube", "https://youtube.com/channel/UC1234567890") == "https://youtube.com/@UC1234567890"

    def test_youtube_user(self):
        """Test YouTube user URL"""
        sl = SocialLinks()
        profile_id = "username"
        assert sl.detect_platform("https://youtube.com/user/username") == "youtube"
        assert sl.is_valid("youtube", "https://youtube.com/user/username") is True
        assert sl.sanitize("youtube", "https://youtube.com/user/username") == "https://youtube.com/@username"

    def test_youtube_mobile(self):
        """Test YouTube mobile URL"""
        sl = SocialLinks()
        profile_id = "channelname"
        assert sl.detect_platform("https://m.youtube.com/c/channelname") == "youtube"
        assert sl.is_valid("youtube", "https://m.youtube.com/c/channelname") is True
        assert sl.sanitize("youtube", "https://m.youtube.com/c/channelname") == "https://youtube.com/@channelname"

