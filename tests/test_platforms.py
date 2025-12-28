from sociallinks.core import SocialLinks


class TestAllPlatforms:
    """Test all predefined platforms"""

    def test_behance(self):
        """Test Behance platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://behance.net/{profile_id}") == "behance"
        assert sl.is_valid("behance", f"https://behance.net/{profile_id}") is True
        assert sl.sanitize("behance", f"https://behance.net/{profile_id}") == f"https://behance.net/{profile_id}"
        # Test direct username
        assert sl.is_valid("behance", profile_id) is True
        assert sl.sanitize("behance", profile_id) == f"https://behance.net/{profile_id}"

    def test_dev_to(self):
        """Test Dev.to platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://dev.to/{profile_id}") == "dev_to"
        assert sl.is_valid("dev_to", f"https://dev.to/{profile_id}") is True
        assert sl.sanitize("dev_to", f"https://dev.to/{profile_id}") == f"https://dev.to/{profile_id}"
        # Test direct username
        assert sl.is_valid("dev_to", profile_id) is True
        assert sl.sanitize("dev_to", profile_id) == f"https://dev.to/{profile_id}"

    def test_dribbble(self):
        """Test Dribbble platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://dribbble.com/{profile_id}") == "dribbble"
        assert sl.is_valid("dribbble", f"https://dribbble.com/{profile_id}") is True
        assert sl.sanitize("dribbble", f"https://dribbble.com/{profile_id}") == f"https://dribbble.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("dribbble", profile_id) is True
        assert sl.sanitize("dribbble", profile_id) == f"https://dribbble.com/{profile_id}"

    def test_exercism(self):
        """Test Exercism platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://exercism.io/profiles/{profile_id}") == "exercism"
        assert sl.is_valid("exercism", f"https://exercism.io/profiles/{profile_id}") is True
        assert sl.sanitize("exercism", f"https://exercism.io/profiles/{profile_id}") == f"https://exercism.io/profiles/{profile_id}"
        # Test direct username
        assert sl.is_valid("exercism", profile_id) is True
        assert sl.sanitize("exercism", profile_id) == f"https://exercism.io/profiles/{profile_id}"

    def test_facebook(self):
        """Test Facebook desktop platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://facebook.com/{profile_id}") == "facebook"
        assert sl.is_valid("facebook", f"https://facebook.com/{profile_id}") is True
        assert sl.sanitize("facebook", f"https://facebook.com/{profile_id}") == f"https://facebook.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("facebook", profile_id) is True
        assert sl.sanitize("facebook", profile_id) == f"https://facebook.com/{profile_id}"

    def test_facebook_mobile(self):
        """Test Facebook mobile platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.facebook.com/{profile_id}") == "facebook"
        assert sl.is_valid("facebook", f"https://m.facebook.com/{profile_id}") is True
        assert sl.sanitize("facebook", f"https://m.facebook.com/{profile_id}") == f"https://facebook.com/{profile_id}"

    def test_github(self):
        """Test GitHub platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://github.com/{profile_id}") == "github"
        assert sl.is_valid("github", f"https://github.com/{profile_id}") is True
        assert sl.sanitize("github", f"https://github.com/{profile_id}") == f"https://github.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("github", profile_id) is True
        assert sl.sanitize("github", profile_id) == f"https://github.com/{profile_id}"

    def test_instagram(self):
        """Test Instagram platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://instagram.com/{profile_id}") == "instagram"
        assert sl.is_valid("instagram", f"https://instagram.com/{profile_id}") is True
        assert sl.sanitize("instagram", f"https://instagram.com/{profile_id}") == f"https://instagram.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("instagram", profile_id) is True
        assert sl.sanitize("instagram", profile_id) == f"https://instagram.com/{profile_id}"

    def test_instagram_mobile(self):
        """Test Instagram mobile platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.instagram.com/{profile_id}") == "instagram"
        assert sl.is_valid("instagram", f"https://m.instagram.com/{profile_id}") is True
        assert sl.sanitize("instagram", f"https://m.instagram.com/{profile_id}") == f"https://instagram.com/{profile_id}"

    def test_instagram_with_at_symbol(self):
        """Test Instagram URLs with @ symbol in path"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Instagram URLs can have @ in the URL path
        assert sl.is_valid("instagram", f"https://instagram.com/{profile_id}") is True
        assert sl.detect_platform(f"https://instagram.com/{profile_id}") == "instagram"
        assert sl.sanitize("instagram", f"https://instagram.com/{profile_id}") == f"https://instagram.com/{profile_id}"

    def test_keybase(self):
        """Test Keybase platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://keybase.io/{profile_id}") == "keybase"
        assert sl.is_valid("keybase", f"https://keybase.io/{profile_id}") is True
        assert sl.sanitize("keybase", f"https://keybase.io/{profile_id}") == f"https://keybase.io/{profile_id}"
        # Test direct username
        assert sl.is_valid("keybase", profile_id) is True
        assert sl.sanitize("keybase", profile_id) == f"https://keybase.io/{profile_id}"

    def test_lemmy_world(self):
        """Test Lemmy World platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://lemmy.world/u/{profile_id}") == "lemmy_world"
        assert sl.is_valid("lemmy_world", f"https://lemmy.world/u/{profile_id}") is True
        assert sl.sanitize("lemmy_world", f"https://lemmy.world/u/{profile_id}") == f"https://lemmy.world/u/{profile_id}"
        # Test direct username
        assert sl.is_valid("lemmy_world", profile_id) is True
        assert sl.sanitize("lemmy_world", profile_id) == f"https://lemmy.world/u/{profile_id}"

    def test_linkedin_personal(self):
        """Test LinkedIn personal profile"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://linkedin.com/in/{profile_id}") == "linkedin"
        assert sl.is_valid("linkedin", f"https://linkedin.com/in/{profile_id}") is True
        assert sl.sanitize("linkedin", f"https://linkedin.com/in/{profile_id}") == f"https://linkedin.com/in/{profile_id}"
        # Test direct username
        assert sl.is_valid("linkedin", profile_id) is True
        assert sl.sanitize("linkedin", profile_id) == f"https://linkedin.com/in/{profile_id}"

    def test_linkedin_company(self):
        """Test LinkedIn company profile"""
        sl = SocialLinks()
        profile_id = "acme"
        assert sl.detect_platform(f"https://linkedin.com/company/{profile_id}") == "linkedin"
        assert sl.is_valid("linkedin", f"https://linkedin.com/company/{profile_id}") is True
        assert sl.sanitize("linkedin", f"https://linkedin.com/company/{profile_id}") == f"https://linkedin.com/company/{profile_id}/"

    def test_linkedin_mobile(self):
        """Test LinkedIn mobile platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://linkedin.com/mwlite/in/{profile_id}") == "linkedin"
        assert sl.is_valid("linkedin", f"https://linkedin.com/mwlite/in/{profile_id}") is True
        assert sl.sanitize("linkedin", f"https://linkedin.com/mwlite/in/{profile_id}") == f"https://linkedin.com/in/{profile_id}"

    def test_linkedin_localized(self):
        """Test LinkedIn localized URLs (e.g., de.linkedin.com)"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Test localized personal profile
        assert sl.is_valid("linkedin", f"https://de.linkedin.com/in/{profile_id}/") is True
        assert sl.sanitize("linkedin", f"https://de.linkedin.com/in/{profile_id}/") == f"https://linkedin.com/in/{profile_id}"
        # Test localized mobile profile
        assert sl.is_valid("linkedin", f"https://de.linkedin.com/mwlite/in/{profile_id}/") is True
        assert sl.sanitize("linkedin", f"https://de.linkedin.com/mwlite/in/{profile_id}/") == f"https://linkedin.com/in/{profile_id}"

    def test_linktree(self):
        """Test Linktree platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://linktr.ee/{profile_id}") == "linktree"
        assert sl.is_valid("linktree", f"https://linktr.ee/{profile_id}") is True
        assert sl.sanitize("linktree", f"https://linktr.ee/{profile_id}") == f"https://linktr.ee/{profile_id}"
        # Test direct username
        assert sl.is_valid("linktree", profile_id) is True
        assert sl.sanitize("linktree", profile_id) == f"https://linktr.ee/{profile_id}"

    def test_mastodon(self):
        """Test Mastodon platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://mastodon.social/@{profile_id}") == "mastodon"
        assert sl.is_valid("mastodon", f"https://mastodon.social/@{profile_id}") is True
        assert sl.sanitize("mastodon", f"https://mastodon.social/@{profile_id}") == f"https://mastodon.social/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("mastodon", profile_id) is True
        assert sl.is_valid("mastodon", f"@{profile_id}") is True
        assert sl.sanitize("mastodon", profile_id) == f"https://mastodon.social/@{profile_id}"
        assert sl.sanitize("mastodon", f"@{profile_id}") == f"https://mastodon.social/@{profile_id}"

    def test_mastodon_variants(self):
        """Test Mastodon platform variants"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://mstdn.social/@{profile_id}") == "mastodon"
        assert sl.detect_platform(f"https://mastodon.world/@{profile_id}") == "mastodon"
        assert sl.is_valid("mastodon", f"https://mstdn.social/@{profile_id}") is True
        assert sl.is_valid("mastodon", f"https://mastodon.world/@{profile_id}") is True

    def test_medium(self):
        """Test Medium platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://medium.com/@{profile_id}") == "medium"
        assert sl.is_valid("medium", f"https://medium.com/@{profile_id}") is True
        assert sl.sanitize("medium", f"https://medium.com/@{profile_id}") == f"https://medium.com/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("medium", profile_id) is True
        assert sl.is_valid("medium", f"@{profile_id}") is True
        assert sl.sanitize("medium", profile_id) == f"https://medium.com/@{profile_id}"
        assert sl.sanitize("medium", f"@{profile_id}") == f"https://medium.com/@{profile_id}"

    def test_patreon(self):
        """Test Patreon platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://patreon.com/{profile_id}") == "patreon"
        assert sl.is_valid("patreon", f"https://patreon.com/{profile_id}") is True
        assert sl.sanitize("patreon", f"https://patreon.com/{profile_id}") == f"https://patreon.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("patreon", profile_id) is True
        assert sl.sanitize("patreon", profile_id) == f"https://patreon.com/{profile_id}"

    def test_pinterest(self):
        """Test Pinterest platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://pinterest.com/{profile_id}") == "pinterest"
        assert sl.is_valid("pinterest", f"https://pinterest.com/{profile_id}") is True
        assert sl.sanitize("pinterest", f"https://pinterest.com/{profile_id}") == f"https://pinterest.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("pinterest", profile_id) is True
        assert sl.sanitize("pinterest", profile_id) == f"https://pinterest.com/{profile_id}"

    def test_pinterest_localized(self):
        """Test Pinterest localized subdomains"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Test with country code subdomain (1-3 characters)
        assert sl.is_valid("pinterest", f"https://pl.pinterest.com/{profile_id}") is True
        assert sl.is_valid("pinterest", f"https://www.pinterest.com/{profile_id}") is True
        # Test that subdomains with more than 3 characters are rejected
        assert sl.is_valid("pinterest", f"https://abcd.pinterest.com/{profile_id}") is False

    def test_soundcloud(self):
        """Test SoundCloud platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://soundcloud.com/{profile_id}") == "soundcloud"
        assert sl.is_valid("soundcloud", f"https://soundcloud.com/{profile_id}") is True
        assert sl.sanitize("soundcloud", f"https://soundcloud.com/{profile_id}") == f"https://soundcloud.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("soundcloud", profile_id) is True
        assert sl.sanitize("soundcloud", profile_id) == f"https://soundcloud.com/{profile_id}"

    def test_apple_music(self):
        """Test Apple Music platform"""
        sl = SocialLinks()
        artist_id = "136975"
        assert sl.detect_platform(f"https://music.apple.com/artist/{artist_id}") == "apple_music"
        assert sl.is_valid("apple_music", f"https://music.apple.com/artist/{artist_id}") is True
        assert sl.sanitize("apple_music", f"https://music.apple.com/artist/{artist_id}") == f"https://music.apple.com/artist/{artist_id}"
        
        assert sl.is_valid("apple_music", artist_id) is True
        assert sl.sanitize("apple_music", artist_id) == f"https://music.apple.com/artist/{artist_id}"
        
        test_cases = [
            ('https://music.apple.com/us/artist/the-beatles/136975', 'https://music.apple.com/artist/136975'),
            ('https://music.apple.com/us/artist/beatles/136975', 'https://music.apple.com/artist/136975'),
            ('https://music.apple.com/artist/beatles/136975', 'https://music.apple.com/artist/136975'),
            ('https://music.apple.com/artist/136975', 'https://music.apple.com/artist/136975'),
            ('https://itunes.apple.com/us/artist/id136975', 'https://music.apple.com/artist/136975'),
        ]
        for source, expected in test_cases:
            assert sl.is_valid("apple_music", source) is True
            assert sl.sanitize("apple_music", source) == expected

    def test_spotify(self):
        """Test Spotify platform"""
        sl = SocialLinks()
        profile_id = "3WrFJ7ztbogyGnTHbHJFl2"
        assert sl.detect_platform(f"https://open.spotify.com/artist/{profile_id}") == "spotify"
        assert sl.is_valid("spotify", f"https://open.spotify.com/artist/{profile_id}") is True
        assert sl.sanitize("spotify", f"https://open.spotify.com/artist/{profile_id}") == f"https://open.spotify.com/artist/{profile_id}"
        # Test direct username
        assert sl.is_valid("spotify", profile_id) is True
        assert sl.sanitize("spotify", profile_id) == f"https://open.spotify.com/artist/{profile_id}"
        
        test_cases = [
            ('spotify:artist:3WrFJ7ztbogyGnTHbHJFl2', 'https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2'),
        ]
        for source, expected in test_cases:
            assert sl.is_valid("spotify", source) is True
            assert sl.sanitize("spotify", source) == expected

    def test_stackoverflow(self):
        """Test Stack Overflow platform"""
        sl = SocialLinks()
        profile_id = "12345"
        assert sl.detect_platform(f"https://stackoverflow.com/users/{profile_id}") == "stackoverflow"
        assert sl.is_valid("stackoverflow", f"https://stackoverflow.com/users/{profile_id}") is True
        assert sl.sanitize("stackoverflow", f"https://stackoverflow.com/users/{profile_id}") == f"https://stackoverflow.com/users/{profile_id}"
        # Test direct username
        assert sl.is_valid("stackoverflow", profile_id) is True
        assert sl.sanitize("stackoverflow", profile_id) == f"https://stackoverflow.com/users/{profile_id}"

    def test_stackoverflow_full_link(self):
        """Test Stack Overflow with full link including username"""
        sl = SocialLinks()
        profile_id = "3573210"
        full_link = f"https://stackoverflow.com/users/{profile_id}/ysskrishna"
        assert sl.is_valid("stackoverflow", full_link) is True
        assert sl.detect_platform(full_link) == "stackoverflow"
        assert sl.sanitize("stackoverflow", full_link) == f"https://stackoverflow.com/users/{profile_id}"

    def test_substack(self):
        """Test Substack platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://{profile_id}.substack.com") == "substack"
        assert sl.is_valid("substack", f"https://{profile_id}.substack.com") is True
        assert sl.sanitize("substack", f"https://{profile_id}.substack.com") == f"https://{profile_id}.substack.com"
        # Test direct username
        assert sl.is_valid("substack", profile_id) is True
        assert sl.sanitize("substack", profile_id) == f"https://{profile_id}.substack.com"

    def test_telegram(self):
        """Test Telegram platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://t.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://t.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://t.me/{profile_id}") == f"https://t.me/{profile_id}"
        # Test direct username
        assert sl.is_valid("telegram", profile_id) is True
        assert sl.sanitize("telegram", profile_id) == f"https://t.me/{profile_id}"

    def test_telegram_alternate(self):
        """Test Telegram alternate domain"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://telegram.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://telegram.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://telegram.me/{profile_id}") == f"https://t.me/{profile_id}"

    def test_tiktok(self):
        """Test TikTok platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://tiktok.com/@{profile_id}") == "tiktok"
        assert sl.is_valid("tiktok", f"https://tiktok.com/@{profile_id}") is True
        assert sl.sanitize("tiktok", f"https://tiktok.com/@{profile_id}") == f"https://tiktok.com/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("tiktok", profile_id) is True
        assert sl.is_valid("tiktok", f"@{profile_id}") is True
        assert sl.sanitize("tiktok", profile_id) == f"https://tiktok.com/@{profile_id}"
        assert sl.sanitize("tiktok", f"@{profile_id}") == f"https://tiktok.com/@{profile_id}"
        # Test www and http variations
        assert sl.is_valid("tiktok", f"https://www.tiktok.com/@{profile_id}") is True
        assert sl.sanitize("tiktok", f"https://www.tiktok.com/@{profile_id}") == f"https://tiktok.com/@{profile_id}"
        assert sl.is_valid("tiktok", f"http://www.tiktok.com/@{profile_id}") is True
        assert sl.sanitize("tiktok", f"http://www.tiktok.com/@{profile_id}") == f"https://tiktok.com/@{profile_id}"

    def test_twitch(self):
        """Test Twitch platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://twitch.tv/{profile_id}") == "twitch"
        assert sl.is_valid("twitch", f"https://twitch.tv/{profile_id}") is True
        assert sl.sanitize("twitch", f"https://twitch.tv/{profile_id}") == f"https://twitch.tv/{profile_id}"
        # Test direct username
        assert sl.is_valid("twitch", profile_id) is True
        assert sl.sanitize("twitch", profile_id) == f"https://twitch.tv/{profile_id}"

    def test_twitch_mobile(self):
        """Test Twitch mobile platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.twitch.tv/{profile_id}") == "twitch"
        assert sl.is_valid("twitch", f"https://m.twitch.tv/{profile_id}") is True
        assert sl.sanitize("twitch", f"https://m.twitch.tv/{profile_id}") == f"https://twitch.tv/{profile_id}"

    def test_vk(self):
        """Test VK platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://vk.com/{profile_id}") == "vk"
        assert sl.is_valid("vk", f"https://vk.com/{profile_id}") is True
        assert sl.sanitize("vk", f"https://vk.com/{profile_id}") == f"https://vk.com/{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("vk", profile_id) is True
        assert sl.is_valid("vk", f"@{profile_id}") is True
        assert sl.sanitize("vk", profile_id) == f"https://vk.com/{profile_id}"
        assert sl.sanitize("vk", f"@{profile_id}") == f"https://vk.com/{profile_id}"

    def test_vk_mobile(self):
        """Test VK mobile platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.vk.com/{profile_id}") == "vk"
        assert sl.is_valid("vk", f"https://m.vk.com/{profile_id}") is True
        assert sl.sanitize("vk", f"https://m.vk.com/{profile_id}") == f"https://vk.com/{profile_id}"

    def test_x(self):
        """Test X (formerly Twitter) platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://x.com/{profile_id}") == "x"
        assert sl.is_valid("x", f"https://x.com/{profile_id}") is True
        assert sl.sanitize("x", f"https://x.com/{profile_id}") == f"https://x.com/{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("x", profile_id) is True
        assert sl.is_valid("x", f"@{profile_id}") is True
        assert sl.sanitize("x", profile_id) == f"https://x.com/{profile_id}"
        assert sl.sanitize("x", f"@{profile_id}") == f"https://x.com/{profile_id}"

    def test_x_twitter_urls(self):
        """Test X platform with Twitter URLs (X handles both x.com and twitter.com)"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Twitter URLs should be detected as X platform
        assert sl.detect_platform(f"https://twitter.com/{profile_id}") == "x"
        assert sl.detect_platform(f"https://mobile.twitter.com/{profile_id}") == "x"
        assert sl.is_valid("x", f"https://twitter.com/{profile_id}") is True
        assert sl.is_valid("x", f"https://mobile.twitter.com/{profile_id}") is True
        # Twitter URLs should be sanitized to x.com
        assert sl.sanitize("x", f"https://twitter.com/{profile_id}") == f"https://x.com/{profile_id}"
        assert sl.sanitize("x", f"https://mobile.twitter.com/{profile_id}") == f"https://x.com/{profile_id}"

    def test_youtube(self):
        """Test YouTube platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://youtube.com/@{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/@{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/@{profile_id}") == f"https://youtube.com/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("youtube", profile_id) is True
        assert sl.is_valid("youtube", f"@{profile_id}") is True
        assert sl.sanitize("youtube", profile_id) == f"https://youtube.com/@{profile_id}"
        assert sl.sanitize("youtube", f"@{profile_id}") == f"https://youtube.com/@{profile_id}"

    def test_youtube_channel(self):
        """Test YouTube channel URL"""
        sl = SocialLinks()
        profile_id = "UC1234567890"
        assert sl.detect_platform(f"https://youtube.com/channel/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/channel/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/channel/{profile_id}") == f"https://youtube.com/@{profile_id}"

    def test_youtube_user(self):
        """Test YouTube user URL"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://youtube.com/user/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/user/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/user/{profile_id}") == f"https://youtube.com/@{profile_id}"

    def test_youtube_mobile(self):
        """Test YouTube mobile URL"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.youtube.com/c/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://m.youtube.com/c/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://m.youtube.com/c/{profile_id}") == f"https://youtube.com/@{profile_id}"

    def test_reddit(self):
        """Test Reddit platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://reddit.com/user/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"https://reddit.com/user/{profile_id}") is True
        assert sl.sanitize("reddit", f"https://reddit.com/user/{profile_id}") == f"https://reddit.com/user/{profile_id}"
        # Test direct username
        assert sl.is_valid("reddit", profile_id) is True
        assert sl.sanitize("reddit", profile_id) == f"https://reddit.com/user/{profile_id}"

    def test_reddit_u_path(self):
        """Test Reddit /u/ path"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://reddit.com/u/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"https://reddit.com/u/{profile_id}") is True
        assert sl.sanitize("reddit", f"https://reddit.com/u/{profile_id}") == f"https://reddit.com/user/{profile_id}"

    def test_reddit_old(self):
        """Test Reddit old.reddit.com"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://old.reddit.com/user/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"https://old.reddit.com/user/{profile_id}") is True
        assert sl.sanitize("reddit", f"https://old.reddit.com/user/{profile_id}") == f"https://reddit.com/user/{profile_id}"
        # Test old.reddit.com with /u/ path
        assert sl.detect_platform(f"https://old.reddit.com/u/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"https://old.reddit.com/u/{profile_id}") is True
        assert sl.sanitize("reddit", f"https://old.reddit.com/u/{profile_id}") == f"https://reddit.com/user/{profile_id}"

    def test_snapchat(self):
        """Test Snapchat platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://snapchat.com/add/{profile_id}") == "snapchat"
        assert sl.is_valid("snapchat", f"https://snapchat.com/add/{profile_id}") is True
        assert sl.sanitize("snapchat", f"https://snapchat.com/add/{profile_id}") == f"https://snapchat.com/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("snapchat", profile_id) is True
        assert sl.is_valid("snapchat", f"@{profile_id}") is True
        assert sl.sanitize("snapchat", profile_id) == f"https://snapchat.com/@{profile_id}"
        assert sl.sanitize("snapchat", f"@{profile_id}") == f"https://snapchat.com/@{profile_id}"

    def test_snapchat_at_path(self):
        """Test Snapchat @username path"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://snapchat.com/@{profile_id}") == "snapchat"
        assert sl.is_valid("snapchat", f"https://snapchat.com/@{profile_id}") is True
        assert sl.sanitize("snapchat", f"https://snapchat.com/@{profile_id}") == f"https://snapchat.com/@{profile_id}"

    def test_tumblr(self):
        """Test Tumblr platform with subdomain"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://{profile_id}.tumblr.com") == "tumblr"
        assert sl.is_valid("tumblr", f"https://{profile_id}.tumblr.com") is True
        assert sl.sanitize("tumblr", f"https://{profile_id}.tumblr.com") == f"https://tumblr.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("tumblr", profile_id) is True
        assert sl.sanitize("tumblr", profile_id) == f"https://tumblr.com/{profile_id}"

    def test_tumblr_blog_path(self):
        """Test Tumblr /blog/ path"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://tumblr.com/blog/{profile_id}") == "tumblr"
        assert sl.is_valid("tumblr", f"https://tumblr.com/blog/{profile_id}") is True
        assert sl.sanitize("tumblr", f"https://tumblr.com/blog/{profile_id}") == f"https://tumblr.com/{profile_id}"

    def test_tumblr_with_trailing_slash(self):
        """Test Tumblr with trailing slash"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.is_valid("tumblr", f"https://{profile_id}.tumblr.com/") is True
        assert sl.sanitize("tumblr", f"https://{profile_id}.tumblr.com/") == f"https://tumblr.com/{profile_id}"

    def test_vimeo(self):
        """Test Vimeo platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://vimeo.com/{profile_id}") == "vimeo"
        assert sl.is_valid("vimeo", f"https://vimeo.com/{profile_id}") is True
        assert sl.sanitize("vimeo", f"https://vimeo.com/{profile_id}") == f"https://vimeo.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("vimeo", profile_id) is True
        assert sl.sanitize("vimeo", profile_id) == f"https://vimeo.com/{profile_id}"

    def test_vimeo_with_www(self):
        """Test Vimeo with www subdomain"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.vimeo.com/{profile_id}") == "vimeo"
        assert sl.is_valid("vimeo", f"https://www.vimeo.com/{profile_id}") is True
        assert sl.sanitize("vimeo", f"https://www.vimeo.com/{profile_id}") == f"https://vimeo.com/{profile_id}"

    def test_whatsapp(self):
        """Test WhatsApp platform with wa.me"""
        sl = SocialLinks()
        phone_number = "1234567890"
        assert sl.detect_platform(f"https://wa.me/{phone_number}") == "whatsapp"
        assert sl.is_valid("whatsapp", f"https://wa.me/{phone_number}") is True
        assert sl.sanitize("whatsapp", f"https://wa.me/{phone_number}") == f"https://wa.me/{phone_number}"
        # Test direct phone number
        assert sl.is_valid("whatsapp", phone_number) is True
        assert sl.sanitize("whatsapp", phone_number) == f"https://wa.me/{phone_number}"

    def test_whatsapp_with_plus(self):
        """Test WhatsApp with international format (+)"""
        sl = SocialLinks()
        phone_number = "+1234567890"
        assert sl.detect_platform(f"https://wa.me/{phone_number}") == "whatsapp"
        assert sl.is_valid("whatsapp", f"https://wa.me/{phone_number}") is True
        assert sl.sanitize("whatsapp", f"https://wa.me/{phone_number}") == f"https://wa.me/{phone_number}"
        # Test direct phone number with + (note: + is kept in sanitized output)
        assert sl.is_valid("whatsapp", phone_number) is True
        assert sl.sanitize("whatsapp", phone_number) == f"https://wa.me/{phone_number}"


