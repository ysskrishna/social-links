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

    def test_bluesky(self):
        """Test Bluesky platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna.bsky.social"
        assert sl.detect_platform(f"https://bsky.app/profile/{profile_id}") == "bluesky"
        assert sl.is_valid("bluesky", f"https://bsky.app/profile/{profile_id}") is True
        assert sl.sanitize("bluesky", f"https://bsky.app/profile/{profile_id}") == f"https://bsky.app/profile/{profile_id}"
        # Test direct handle
        assert sl.is_valid("bluesky", profile_id) is True
        assert sl.sanitize("bluesky", profile_id) == f"https://bsky.app/profile/{profile_id}"

    def test_bluesky_with_at(self):
        """Test Bluesky with @ prefix"""
        sl = SocialLinks()
        profile_id = "ysskrishna.bsky.social"
        # Test with @ prefix
        assert sl.is_valid("bluesky", f"@{profile_id}") is True
        assert sl.sanitize("bluesky", f"@{profile_id}") == f"https://bsky.app/profile/{profile_id}"

    def test_bluesky_with_www(self):
        """Test Bluesky with www subdomain"""
        sl = SocialLinks()
        profile_id = "ysskrishna.bsky.social"
        assert sl.detect_platform(f"https://www.bsky.app/profile/{profile_id}") == "bluesky"
        assert sl.is_valid("bluesky", f"https://www.bsky.app/profile/{profile_id}") is True
        assert sl.sanitize("bluesky", f"https://www.bsky.app/profile/{profile_id}") == f"https://bsky.app/profile/{profile_id}"

    def test_bluesky_with_http(self):
        """Test Bluesky with http protocol"""
        sl = SocialLinks()
        profile_id = "ysskrishna.bsky.social"
        assert sl.detect_platform(f"http://bsky.app/profile/{profile_id}") == "bluesky"
        assert sl.is_valid("bluesky", f"http://bsky.app/profile/{profile_id}") is True
        assert sl.sanitize("bluesky", f"http://bsky.app/profile/{profile_id}") == f"https://bsky.app/profile/{profile_id}"

    def test_bluesky_with_trailing_slash(self):
        """Test Bluesky with trailing slash"""
        sl = SocialLinks()
        profile_id = "ysskrishna.bsky.social"
        assert sl.is_valid("bluesky", f"https://bsky.app/profile/{profile_id}/") is True
        assert sl.sanitize("bluesky", f"https://bsky.app/profile/{profile_id}/") == f"https://bsky.app/profile/{profile_id}"

    def test_bluesky_custom_domain(self):
        """Test Bluesky with custom domain"""
        sl = SocialLinks()
        profile_id = "example.com"
        assert sl.detect_platform(f"https://bsky.app/profile/{profile_id}") == "bluesky"
        assert sl.is_valid("bluesky", f"https://bsky.app/profile/{profile_id}") is True
        assert sl.sanitize("bluesky", f"https://bsky.app/profile/{profile_id}") == f"https://bsky.app/profile/{profile_id}"

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

    def test_discord(self):
        """Test Discord platform with discord.gg"""
        sl = SocialLinks()
        invite_code = "ysskrishna"
        assert sl.detect_platform(f"https://discord.gg/{invite_code}") == "discord"
        assert sl.is_valid("discord", f"https://discord.gg/{invite_code}") is True
        assert sl.sanitize("discord", f"https://discord.gg/{invite_code}") == f"https://discord.gg/{invite_code}"
        # Test direct invite code
        assert sl.is_valid("discord", invite_code) is True
        assert sl.sanitize("discord", invite_code) == f"https://discord.gg/{invite_code}"

    def test_discord_invite_url(self):
        """Test Discord platform with discord.com/invite"""
        sl = SocialLinks()
        invite_code = "ysskrishna"
        # Test discord.com/invite format - should normalize to discord.gg
        assert sl.detect_platform(f"https://discord.com/invite/{invite_code}") == "discord"
        assert sl.is_valid("discord", f"https://discord.com/invite/{invite_code}") is True
        assert sl.sanitize("discord", f"https://discord.com/invite/{invite_code}") == f"https://discord.gg/{invite_code}"

    def test_discord_with_www(self):
        """Test Discord with www subdomain"""
        sl = SocialLinks()
        invite_code = "ysskrishna"
        # Test with www on discord.gg
        assert sl.detect_platform(f"https://www.discord.gg/{invite_code}") == "discord"
        assert sl.is_valid("discord", f"https://www.discord.gg/{invite_code}") is True
        assert sl.sanitize("discord", f"https://www.discord.gg/{invite_code}") == f"https://discord.gg/{invite_code}"
        # Test with www on discord.com/invite
        assert sl.detect_platform(f"https://www.discord.com/invite/{invite_code}") == "discord"
        assert sl.is_valid("discord", f"https://www.discord.com/invite/{invite_code}") is True
        assert sl.sanitize("discord", f"https://www.discord.com/invite/{invite_code}") == f"https://discord.gg/{invite_code}"

    def test_discord_with_http(self):
        """Test Discord with http protocol"""
        sl = SocialLinks()
        invite_code = "abc123XYZ"
        # Test http instead of https
        assert sl.detect_platform(f"http://discord.gg/{invite_code}") == "discord"
        assert sl.is_valid("discord", f"http://discord.gg/{invite_code}") is True
        assert sl.sanitize("discord", f"http://discord.gg/{invite_code}") == f"https://discord.gg/{invite_code}"

    def test_discord_with_trailing_slash(self):
        """Test Discord with trailing slash"""
        sl = SocialLinks()
        invite_code = "abc123XYZ"
        assert sl.is_valid("discord", f"https://discord.gg/{invite_code}/") is True
        assert sl.sanitize("discord", f"https://discord.gg/{invite_code}/") == f"https://discord.gg/{invite_code}"

    def test_douyin(self):
        """Test Douyin platform"""
        sl = SocialLinks()
        user_id = "MS4wLjABAAAA9yeV8IIJxpee3_u9zb_Al3_mOA8IffgD3_ueMCQUly4"
        assert sl.detect_platform(f"https://www.douyin.com/user/{user_id}") == "douyin"
        assert sl.is_valid("douyin", f"https://www.douyin.com/user/{user_id}") is True
        assert sl.sanitize("douyin", f"https://www.douyin.com/user/{user_id}") == f"https://www.douyin.com/user/{user_id}"
        # Test direct user ID
        assert sl.is_valid("douyin", user_id) is True
        assert sl.sanitize("douyin", user_id) == f"https://www.douyin.com/user/{user_id}"

    def test_douyin_variations(self):
        """Test Douyin with various URL formats"""
        sl = SocialLinks()
        user_id = "MS4wLjABAAAA9yeV8IIJxpee3_u9zb_Al3_mOA8IffgD3_ueMCQUly4"
        
        # Test without www subdomain
        assert sl.detect_platform(f"https://douyin.com/user/{user_id}") == "douyin"
        assert sl.is_valid("douyin", f"https://douyin.com/user/{user_id}") is True
        assert sl.sanitize("douyin", f"https://douyin.com/user/{user_id}") == f"https://www.douyin.com/user/{user_id}"
        
        # Test with trailing slash
        assert sl.is_valid("douyin", f"https://www.douyin.com/user/{user_id}/") is True
        assert sl.sanitize("douyin", f"https://www.douyin.com/user/{user_id}/") == f"https://www.douyin.com/user/{user_id}"
        
        # Test http protocol
        assert sl.detect_platform(f"http://www.douyin.com/user/{user_id}") == "douyin"
        assert sl.is_valid("douyin", f"http://www.douyin.com/user/{user_id}") is True
        assert sl.sanitize("douyin", f"http://www.douyin.com/user/{user_id}") == f"https://www.douyin.com/user/{user_id}"

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

    def test_etsy(self):
        """Test Etsy platform"""
        sl = SocialLinks()
        shop_name = "MyShopName"
        assert sl.detect_platform(f"https://etsy.com/shop/{shop_name}") == "etsy"
        assert sl.is_valid("etsy", f"https://etsy.com/shop/{shop_name}") is True
        assert sl.sanitize("etsy", f"https://etsy.com/shop/{shop_name}") == f"https://etsy.com/shop/{shop_name}"
        # Test direct shop name
        assert sl.is_valid("etsy", shop_name) is True
        assert sl.sanitize("etsy", shop_name) == f"https://etsy.com/shop/{shop_name}"

    def test_etsy_with_www(self):
        """Test Etsy with www subdomain"""
        sl = SocialLinks()
        shop_name = "MyShopName"
        assert sl.detect_platform(f"https://www.etsy.com/shop/{shop_name}") == "etsy"
        assert sl.is_valid("etsy", f"https://www.etsy.com/shop/{shop_name}") is True
        assert sl.sanitize("etsy", f"https://www.etsy.com/shop/{shop_name}") == f"https://etsy.com/shop/{shop_name}"

    def test_etsy_with_http(self):
        """Test Etsy with http protocol"""
        sl = SocialLinks()
        shop_name = "MyShopName"
        assert sl.detect_platform(f"http://etsy.com/shop/{shop_name}") == "etsy"
        assert sl.is_valid("etsy", f"http://etsy.com/shop/{shop_name}") is True
        assert sl.sanitize("etsy", f"http://etsy.com/shop/{shop_name}") == f"https://etsy.com/shop/{shop_name}"

    def test_etsy_with_trailing_slash(self):
        """Test Etsy with trailing slash"""
        sl = SocialLinks()
        shop_name = "MyShopName"
        assert sl.is_valid("etsy", f"https://etsy.com/shop/{shop_name}/") is True
        assert sl.sanitize("etsy", f"https://etsy.com/shop/{shop_name}/") == f"https://etsy.com/shop/{shop_name}"

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

    def test_flickr(self):
        """Test Flickr platform with /people/ path"""
        sl = SocialLinks()
        profile_id = "dv-hans"
        assert sl.detect_platform(f"https://www.flickr.com/people/{profile_id}") == "flickr"
        assert sl.is_valid("flickr", f"https://www.flickr.com/people/{profile_id}") is True
        assert sl.sanitize("flickr", f"https://www.flickr.com/people/{profile_id}") == f"https://www.flickr.com/people/{profile_id}"
        # Test direct username
        assert sl.is_valid("flickr", profile_id) is True
        assert sl.sanitize("flickr", profile_id) == f"https://www.flickr.com/people/{profile_id}"

    def test_flickr_without_www(self):
        """Test Flickr without www subdomain"""
        sl = SocialLinks()
        profile_id = "dv-hans"
        assert sl.detect_platform(f"https://flickr.com/people/{profile_id}") == "flickr"
        assert sl.is_valid("flickr", f"https://flickr.com/people/{profile_id}") is True
        assert sl.sanitize("flickr", f"https://flickr.com/people/{profile_id}") == f"https://www.flickr.com/people/{profile_id}"

    def test_flickr_with_http(self):
        """Test Flickr with http protocol"""
        sl = SocialLinks()
        profile_id = "dv-hans"
        assert sl.detect_platform(f"http://www.flickr.com/people/{profile_id}") == "flickr"
        assert sl.is_valid("flickr", f"http://www.flickr.com/people/{profile_id}") is True
        assert sl.sanitize("flickr", f"http://www.flickr.com/people/{profile_id}") == f"https://www.flickr.com/people/{profile_id}"

    def test_flickr_with_trailing_slash(self):
        """Test Flickr with trailing slash"""
        sl = SocialLinks()
        profile_id = "dv-hans"
        assert sl.is_valid("flickr", f"https://www.flickr.com/people/{profile_id}/") is True
        assert sl.sanitize("flickr", f"https://www.flickr.com/people/{profile_id}/") == f"https://www.flickr.com/people/{profile_id}"

    def test_flickr_with_at_symbol(self):
        """Test Flickr with @ symbol in username (common for numeric IDs)"""
        sl = SocialLinks()
        profile_id = "123456@N01"
        # Test direct username with @ symbol
        assert sl.is_valid("flickr", profile_id) is True
        assert sl.sanitize("flickr", profile_id) == f"https://www.flickr.com/people/{profile_id}"

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

    def test_gravatar(self):
        """Test Gravatar platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"https://gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("gravatar", profile_id) is True
        assert sl.sanitize("gravatar", profile_id) == f"https://gravatar.com/{profile_id}"

    def test_gravatar_with_language(self):
        """Test Gravatar with language subdomain"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Test with en subdomain
        assert sl.detect_platform(f"https://en.gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"https://en.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://en.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"
        # Test with other language codes
        assert sl.is_valid("gravatar", f"https://fr.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://fr.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"

    def test_gravatar_with_www(self):
        """Test Gravatar with www subdomain"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"https://www.gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"https://www.gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"

    def test_gravatar_with_http(self):
        """Test Gravatar with http protocol"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"http://gravatar.com/{profile_id}") == "gravatar"
        assert sl.is_valid("gravatar", f"http://gravatar.com/{profile_id}") is True
        assert sl.sanitize("gravatar", f"http://gravatar.com/{profile_id}") == f"https://gravatar.com/{profile_id}"

    def test_gravatar_with_trailing_slash(self):
        """Test Gravatar with trailing slash"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.is_valid("gravatar", f"https://gravatar.com/{profile_id}/") is True
        assert sl.sanitize("gravatar", f"https://gravatar.com/{profile_id}/") == f"https://gravatar.com/{profile_id}"

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

    def test_kuaishou(self):
        """Test Kuaishou platform"""
        sl = SocialLinks()
        profile_id = "3xxdnfw963m6abu"
        assert sl.detect_platform(f"https://www.kuaishou.com/profile/{profile_id}") == "kuaishou"
        assert sl.is_valid("kuaishou", f"https://www.kuaishou.com/profile/{profile_id}") is True
        assert sl.sanitize("kuaishou", f"https://www.kuaishou.com/profile/{profile_id}") == f"https://www.kuaishou.com/profile/{profile_id}"
        # Test direct username
        assert sl.is_valid("kuaishou", profile_id) is True
        assert sl.sanitize("kuaishou", profile_id) == f"https://www.kuaishou.com/profile/{profile_id}"

    def test_kuaishou_without_www(self):
        """Test Kuaishou without www subdomain"""
        sl = SocialLinks()
        profile_id = "3xxdnfw963m6abu"
        assert sl.detect_platform(f"https://kuaishou.com/profile/{profile_id}") == "kuaishou"
        assert sl.is_valid("kuaishou", f"https://kuaishou.com/profile/{profile_id}") is True
        assert sl.sanitize("kuaishou", f"https://kuaishou.com/profile/{profile_id}") == f"https://www.kuaishou.com/profile/{profile_id}"

    def test_kuaishou_with_http(self):
        """Test Kuaishou with http protocol"""
        sl = SocialLinks()
        profile_id = "3xxdnfw963m6abu"
        assert sl.detect_platform(f"http://www.kuaishou.com/profile/{profile_id}") == "kuaishou"
        assert sl.is_valid("kuaishou", f"http://www.kuaishou.com/profile/{profile_id}") is True
        assert sl.sanitize("kuaishou", f"http://www.kuaishou.com/profile/{profile_id}") == f"https://www.kuaishou.com/profile/{profile_id}"

    def test_kuaishou_with_trailing_slash(self):
        """Test Kuaishou with trailing slash"""
        sl = SocialLinks()
        profile_id = "3xxdnfw963m6abu"
        assert sl.is_valid("kuaishou", f"https://www.kuaishou.com/profile/{profile_id}/") is True
        assert sl.sanitize("kuaishou", f"https://www.kuaishou.com/profile/{profile_id}/") == f"https://www.kuaishou.com/profile/{profile_id}"

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
        assert sl.sanitize("linkedin", f"https://linkedin.com/company/{profile_id}") == f"https://linkedin.com/company/{profile_id}"

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

    def test_linkedin_additional_test_cases(self):
        """Test LinkedIn additional test cases from PHP NormalizersTest.php"""
        sl = SocialLinks()
        
        # LinkedIn profile test cases (from testLinkedinProfileNormalizer)
        profile_test_cases = [
            ('https://www.linkedin.com/in/dealroom/', 'https://linkedin.com/in/dealroom'),
            ('https://www.linkedin.com/in/dealroom', 'https://linkedin.com/in/dealroom'),
            ('http://www.linkedin.com/in/dealroom/', 'https://linkedin.com/in/dealroom'),
            ('http://de.linkedin.com/in/dealroom/', 'https://linkedin.com/in/dealroom'),
            ('https://de.linkedin.com/in/peter-müller-81a8/', 'https://linkedin.com/in/peter-müller-81a8'),
        ]
        
        for source, expected in profile_test_cases:
            assert sl.is_valid("linkedin", source) is True, f"URL should be valid: {source}"
            result = sl.sanitize("linkedin", source)
            assert result == expected, f"Expected {expected}, got {result} for {source}"
        
        # LinkedIn company test cases 
        company_test_cases = [
            ('https://www.linkedin.com/company/dealroom/', 'https://linkedin.com/company/dealroom'),
            ('https://www.linkedin.com/company/dealroom', 'https://linkedin.com/company/dealroom'),
            ('http://www.linkedin.com/company/dealroom/', 'https://linkedin.com/company/dealroom'),
            ('https://linkedin.com/company/dealroom/', 'https://linkedin.com/company/dealroom'),
            ('https://www.linkedin.com/company/dealroom-co/', 'https://linkedin.com/company/dealroom-co'),
            ('https://www.linkedin.com/company/upjers-gmbh-&-co.-kg', 'https://linkedin.com/company/upjers-gmbh-&-co.-kg'),
            ('https://www.linkedin.com/company/magis_official', 'https://linkedin.com/company/magis_official'),
            ('https://www.linkedin.com/company/cake-–-ridecake.com/', 'https://linkedin.com/company/cake-–-ridecake.com'),
            ('https://www.linkedin.com/company/brigham-and-women%27s-hospital/', 'https://linkedin.com/company/brigham-and-women%27s-hospital'),
            ('https://www.linkedin.com/school/linkedinschool/', 'https://linkedin.com/company/linkedinschool'),
            ('https://www.linkedin.com/school/linkedinschool', 'https://linkedin.com/company/linkedinschool'),
            ('http://www.linkedin.com/school/linkedinschool/', 'https://linkedin.com/company/linkedinschool'),
            ('https://linkedin.com/school/linkedinschool/', 'https://linkedin.com/company/linkedinschool'),
            ('https://www.linkedin.com/school/stanford-university/', 'https://linkedin.com/company/stanford-university'),
            ('https://www.linkedin.com/school/mit/', 'https://linkedin.com/company/mit'),
        ]
        
        for source, expected in company_test_cases:
            assert sl.is_valid("linkedin", source) is True, f"URL should be valid: {source}"
            result = sl.sanitize("linkedin", source)
            assert result == expected, f"Expected {expected}, got {result} for {source}"

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

    def test_wellfound_user(self):
        """Test Wellfound user profile"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://wellfound.com/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://wellfound.com/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://wellfound.com/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"
        # Test direct username
        assert sl.is_valid("wellfound", profile_id) is True
        assert sl.sanitize("wellfound", profile_id) == f"https://wellfound.com/u/{profile_id}"

    def test_wellfound_company(self):
        """Test Wellfound company profile"""
        sl = SocialLinks()
        profile_id = "homelight"
        assert sl.detect_platform(f"https://wellfound.com/company/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://wellfound.com/company/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://wellfound.com/company/{profile_id}") == f"https://wellfound.com/company/{profile_id}"

    def test_wellfound_legacy_angellist_user(self):
        """Test legacy AngelList user profile URLs (angel.co/u/)"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://angel.co/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"

    def test_wellfound_legacy_angellist_company(self):
        """Test legacy AngelList company URLs (angel.co/company/ and angel.co/)"""
        sl = SocialLinks()
        profile_id = "slack"
        # Test angel.co/company/ format
        assert sl.detect_platform(f"https://angel.co/company/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/company/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/company/{profile_id}") == f"https://wellfound.com/company/{profile_id}"
        # Test old angel.co/ format (without /company/)
        assert sl.detect_platform(f"https://angel.co/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://angel.co/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://angel.co/{profile_id}") == f"https://wellfound.com/company/{profile_id}"

    def test_wellfound_with_www(self):
        """Test Wellfound with www subdomain"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Test user profile with www
        assert sl.detect_platform(f"https://www.wellfound.com/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://www.wellfound.com/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"https://www.wellfound.com/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"
        # Test company profile with www
        company_id = "homelight"
        assert sl.detect_platform(f"https://www.wellfound.com/company/{company_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"https://www.wellfound.com/company/{company_id}") is True
        assert sl.sanitize("wellfound", f"https://www.wellfound.com/company/{company_id}") == f"https://wellfound.com/company/{company_id}"

    def test_wellfound_with_http(self):
        """Test Wellfound with http protocol"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Test http instead of https
        assert sl.detect_platform(f"http://wellfound.com/u/{profile_id}") == "wellfound"
        assert sl.is_valid("wellfound", f"http://wellfound.com/u/{profile_id}") is True
        assert sl.sanitize("wellfound", f"http://wellfound.com/u/{profile_id}") == f"https://wellfound.com/u/{profile_id}"

    def test_wellfound_with_trailing_slash(self):
        """Test Wellfound with trailing slash"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.is_valid("wellfound", f"https://wellfound.com/u/{profile_id}/") is True
        assert sl.sanitize("wellfound", f"https://wellfound.com/u/{profile_id}/") == f"https://wellfound.com/u/{profile_id}"

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

    def test_bandcamp(self):
        """Test Bandcamp platform with subdomain"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://{profile_id}.bandcamp.com") == "bandcamp"
        assert sl.is_valid("bandcamp", f"https://{profile_id}.bandcamp.com") is True
        assert sl.sanitize("bandcamp", f"https://{profile_id}.bandcamp.com") == f"https://{profile_id}.bandcamp.com"
        # Test direct username
        assert sl.is_valid("bandcamp", profile_id) is True
        assert sl.sanitize("bandcamp", profile_id) == f"https://{profile_id}.bandcamp.com"

    def test_bandcamp_with_trailing_slash(self):
        """Test Bandcamp with trailing slash"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.is_valid("bandcamp", f"https://{profile_id}.bandcamp.com/") is True
        assert sl.sanitize("bandcamp", f"https://{profile_id}.bandcamp.com/") == f"https://{profile_id}.bandcamp.com"

    def test_bandcamp_with_http(self):
        """Test Bandcamp with http protocol"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Test http instead of https
        assert sl.detect_platform(f"http://{profile_id}.bandcamp.com") == "bandcamp"
        assert sl.is_valid("bandcamp", f"http://{profile_id}.bandcamp.com") is True
        assert sl.sanitize("bandcamp", f"http://{profile_id}.bandcamp.com") == f"https://{profile_id}.bandcamp.com"

    def test_bandcamp_with_dashes(self):
        """Test Bandcamp with dashes in username"""
        sl = SocialLinks()
        profile_id = "my-band-name"
        assert sl.detect_platform(f"https://{profile_id}.bandcamp.com") == "bandcamp"
        assert sl.is_valid("bandcamp", f"https://{profile_id}.bandcamp.com") is True
        assert sl.sanitize("bandcamp", f"https://{profile_id}.bandcamp.com") == f"https://{profile_id}.bandcamp.com"

    def test_spotify_artist(self):
        """Test Spotify artist profile"""
        sl = SocialLinks()
        artist_id = "3WrFJ7ztbogyGnTHbHJFl2"
        assert sl.detect_platform(f"https://open.spotify.com/artist/{artist_id}") == "spotify"
        assert sl.is_valid("spotify", f"https://open.spotify.com/artist/{artist_id}") is True
        assert sl.sanitize("spotify", f"https://open.spotify.com/artist/{artist_id}") == f"https://open.spotify.com/artist/{artist_id}"
        # Test direct artist ID (defaults to artist)
        assert sl.is_valid("spotify", artist_id) is True
        assert sl.sanitize("spotify", artist_id) == f"https://open.spotify.com/artist/{artist_id}"
        
    def test_spotify_artist_uri(self):
        """Test Spotify artist URI format (spotify:artist:id)"""
        sl = SocialLinks()
        artist_id = "3WrFJ7ztbogyGnTHbHJFl2"
        uri = f"spotify:artist:{artist_id}"
        assert sl.detect_platform(uri) == "spotify"
        assert sl.is_valid("spotify", uri) is True
        assert sl.sanitize("spotify", uri) == f"https://open.spotify.com/artist/{artist_id}"

    def test_spotify_user(self):
        """Test Spotify user profile"""
        sl = SocialLinks()
        user_id = "vanesamartinoficial"
        assert sl.detect_platform(f"https://open.spotify.com/user/{user_id}") == "spotify"
        assert sl.is_valid("spotify", f"https://open.spotify.com/user/{user_id}") is True
        assert sl.sanitize("spotify", f"https://open.spotify.com/user/{user_id}") == f"https://open.spotify.com/user/{user_id}"
        
    def test_spotify_user_long_id(self):
        """Test Spotify user profile with long generated ID"""
        sl = SocialLinks()
        user_id = "31wwwnrvhv3i2l2z43ipcmpapoya"
        assert sl.detect_platform(f"https://open.spotify.com/user/{user_id}") == "spotify"
        assert sl.is_valid("spotify", f"https://open.spotify.com/user/{user_id}") is True
        assert sl.sanitize("spotify", f"https://open.spotify.com/user/{user_id}") == f"https://open.spotify.com/user/{user_id}"

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
        """Test Substack platform - all formats sanitize to @username format"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        
        # Test subdomain format - sanitizes to @username format
        assert sl.detect_platform(f"https://{profile_id}.substack.com") == "substack"
        assert sl.is_valid("substack", f"https://{profile_id}.substack.com") is True
        assert sl.sanitize("substack", f"https://{profile_id}.substack.com") == f"https://substack.com/@{profile_id}"
        
        # Test @username format
        assert sl.detect_platform(f"https://substack.com/@{profile_id}") == "substack"
        assert sl.is_valid("substack", f"https://substack.com/@{profile_id}") is True
        assert sl.sanitize("substack", f"https://substack.com/@{profile_id}") == f"https://substack.com/@{profile_id}"
        
        # Test with www subdomain
        assert sl.is_valid("substack", f"https://www.substack.com/@{profile_id}") is True
        assert sl.sanitize("substack", f"https://www.substack.com/@{profile_id}") == f"https://substack.com/@{profile_id}"
        
        # Test http protocol
        assert sl.is_valid("substack", f"http://substack.com/@{profile_id}") is True
        assert sl.sanitize("substack", f"http://substack.com/@{profile_id}") == f"https://substack.com/@{profile_id}"
        
        # Test with trailing slash
        assert sl.is_valid("substack", f"https://substack.com/@{profile_id}/") is True
        assert sl.sanitize("substack", f"https://substack.com/@{profile_id}/") == f"https://substack.com/@{profile_id}"
        
        # Test direct username - sanitizes to @username format
        assert sl.is_valid("substack", profile_id) is True
        assert sl.sanitize("substack", profile_id) == f"https://substack.com/@{profile_id}"

    def test_telegram(self):
        """Test Telegram platform with t.me"""
        sl = SocialLinks()
        profile_id = "telegram"
        assert sl.detect_platform(f"https://t.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://t.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://t.me/{profile_id}") == f"https://t.me/{profile_id}"
        # Test direct username
        assert sl.is_valid("telegram", profile_id) is True
        assert sl.sanitize("telegram", profile_id) == f"https://t.me/{profile_id}"

    def test_telegram_with_underscore(self):
        """Test Telegram with underscores in username"""
        sl = SocialLinks()
        profile_id = "list_telegram"
        assert sl.detect_platform(f"https://t.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://t.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://t.me/{profile_id}") == f"https://t.me/{profile_id}"

    def test_telegram_dog(self):
        """Test Telegram dog domain"""
        sl = SocialLinks()
        profile_id = "mrhallo"
        assert sl.detect_platform(f"https://telegram.dog/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://telegram.dog/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://telegram.dog/{profile_id}") == f"https://t.me/{profile_id}"

    def test_telegram_me(self):
        """Test Telegram.me domain"""
        sl = SocialLinks()
        profile_id = "shajareyan"
        assert sl.detect_platform(f"https://telegram.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://telegram.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://telegram.me/{profile_id}") == f"https://t.me/{profile_id}"
        # Test with www
        assert sl.detect_platform(f"https://www.telegram.me/{profile_id}") == "telegram"
        assert sl.is_valid("telegram", f"https://www.telegram.me/{profile_id}") is True
        assert sl.sanitize("telegram", f"https://www.telegram.me/{profile_id}") == f"https://t.me/{profile_id}"

    def test_telegram_web_client_numeric_id(self):
        """Test Telegram web client with numeric ID"""
        sl = SocialLinks()
        # Web client with numeric ID (can be negative for groups/channels)
        numeric_id = "-2128475717"
        web_url = f"https://web.telegram.org/k/#{numeric_id}"
        assert sl.detect_platform(web_url) == "telegram"
        assert sl.is_valid("telegram", web_url) is True
        assert sl.sanitize("telegram", web_url) == f"https://t.me/{numeric_id}"
        
        # Test positive numeric ID
        positive_id = "6891155458"
        web_url_positive = f"http://web.telegram.org/a/#{positive_id}"
        assert sl.detect_platform(web_url_positive) == "telegram"
        assert sl.is_valid("telegram", web_url_positive) is True
        assert sl.sanitize("telegram", web_url_positive) == f"https://t.me/{positive_id}"

    def test_telegram_web_client_username(self):
        """Test Telegram web client with username"""
        sl = SocialLinks()
        username = "Banana_traffbot"
        # Web client can have @ prefix in URL
        web_url = f"https://web.telegram.org/k/#@{username}"
        assert sl.detect_platform(web_url) == "telegram"
        assert sl.is_valid("telegram", web_url) is True
        # @ should be stripped in sanitized output
        assert sl.sanitize("telegram", web_url) == f"https://t.me/{username}"

    def test_threads(self):
        """Test Threads platform"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://threads.net/@{profile_id}") == "threads"
        assert sl.is_valid("threads", f"https://threads.net/@{profile_id}") is True
        assert sl.sanitize("threads", f"https://threads.net/@{profile_id}") == f"https://threads.net/@{profile_id}"
        # Test direct username (with and without @)
        assert sl.is_valid("threads", profile_id) is True
        assert sl.is_valid("threads", f"@{profile_id}") is True
        assert sl.sanitize("threads", profile_id) == f"https://threads.net/@{profile_id}"
        assert sl.sanitize("threads", f"@{profile_id}") == f"https://threads.net/@{profile_id}"

    def test_threads_with_www(self):
        """Test Threads with www subdomain"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://www.threads.net/@{profile_id}") == "threads"
        assert sl.is_valid("threads", f"https://www.threads.net/@{profile_id}") is True
        assert sl.sanitize("threads", f"https://www.threads.net/@{profile_id}") == f"https://threads.net/@{profile_id}"

    def test_threads_with_http(self):
        """Test Threads with http protocol"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"http://threads.net/@{profile_id}") == "threads"
        assert sl.is_valid("threads", f"http://threads.net/@{profile_id}") is True
        assert sl.sanitize("threads", f"http://threads.net/@{profile_id}") == f"https://threads.net/@{profile_id}"

    def test_threads_with_trailing_slash(self):
        """Test Threads with trailing slash"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.is_valid("threads", f"https://threads.net/@{profile_id}/") is True
        assert sl.sanitize("threads", f"https://threads.net/@{profile_id}/") == f"https://threads.net/@{profile_id}"

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
        profile_id = "@ysskrishna"
        assert sl.detect_platform(f"https://youtube.com/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/{profile_id}") == f"https://youtube.com/{profile_id}"

    def test_youtube_channel(self):
        """Test YouTube channel URL"""
        sl = SocialLinks()
        profile_id = "UC1234567890"
        assert sl.detect_platform(f"https://youtube.com/channel/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/channel/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/channel/{profile_id}") == f"https://youtube.com/{profile_id}"

    def test_youtube_user(self):
        """Test YouTube user URL"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://youtube.com/user/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/user/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/user/{profile_id}") == f"https://youtube.com/{profile_id}"

    def test_youtube_mobile(self):
        """Test YouTube mobile URL"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.youtube.com/c/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://m.youtube.com/c/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://m.youtube.com/c/{profile_id}") == f"https://youtube.com/{profile_id}"

    def test_youtube_various_formats(self):
        """Test YouTube with various URL formats (matching PHP test cases)"""
        sl = SocialLinks()
        profile_id = "Google"
        # Test www.youtube.com/user/Google
        assert sl.detect_platform(f"https://www.youtube.com/user/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://www.youtube.com/user/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://www.youtube.com/user/{profile_id}") == f"https://youtube.com/{profile_id}"
        # Test www.youtube.com/c/Google
        assert sl.detect_platform(f"https://www.youtube.com/c/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://www.youtube.com/c/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://www.youtube.com/c/{profile_id}") == f"https://youtube.com/{profile_id}"
        # Test www.youtube.com/Google
        assert sl.detect_platform(f"https://www.youtube.com/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://www.youtube.com/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://www.youtube.com/{profile_id}") == f"https://youtube.com/{profile_id}"
        # Test www.youtube.com/Google/ (with trailing slash)
        assert sl.detect_platform(f"https://www.youtube.com/{profile_id}/") == "youtube"
        assert sl.is_valid("youtube", f"https://www.youtube.com/{profile_id}/") is True
        assert sl.sanitize("youtube", f"https://www.youtube.com/{profile_id}/") == f"https://youtube.com/{profile_id}"
        # Test youtube.com/Google (without www)
        assert sl.detect_platform(f"https://youtube.com/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"https://youtube.com/{profile_id}") is True
        assert sl.sanitize("youtube", f"https://youtube.com/{profile_id}") == f"https://youtube.com/{profile_id}"
        # Test http://www.youtube.com/Google (http instead of https)
        assert sl.detect_platform(f"http://www.youtube.com/{profile_id}") == "youtube"
        assert sl.is_valid("youtube", f"http://www.youtube.com/{profile_id}") is True
        assert sl.sanitize("youtube", f"http://www.youtube.com/{profile_id}") == f"https://youtube.com/{profile_id}"

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

    def test_reddit_u_prefix(self):
        """Test Reddit u/ prefix format (e.g., u/username)"""
        sl = SocialLinks()
        profile_id = "ysskrishna"
        # Test u/username format
        assert sl.detect_platform(f"u/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"u/{profile_id}") is True
        assert sl.sanitize("reddit", f"u/{profile_id}") == f"https://reddit.com/user/{profile_id}"

    def test_reddit_subreddit(self):
        """Test Reddit subreddit /r/ path"""
        sl = SocialLinks()
        subreddit_name = "python"
        assert sl.detect_platform(f"https://reddit.com/r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"https://reddit.com/r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"https://reddit.com/r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"

    def test_reddit_subreddit_variations(self):
        """Test Reddit subreddit with various URL formats"""
        sl = SocialLinks()
        subreddit_name = "learnprogramming"
        
        # Test www subdomain
        assert sl.detect_platform(f"https://www.reddit.com/r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"https://www.reddit.com/r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"https://www.reddit.com/r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"
        
        # Test old.reddit.com
        assert sl.detect_platform(f"https://old.reddit.com/r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"https://old.reddit.com/r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"https://old.reddit.com/r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"
        
        # Test with trailing slash
        assert sl.is_valid("reddit", f"https://reddit.com/r/{subreddit_name}/") is True
        assert sl.sanitize("reddit", f"https://reddit.com/r/{subreddit_name}/") == f"https://reddit.com/r/{subreddit_name}"
        
        # Test http protocol
        assert sl.detect_platform(f"http://reddit.com/r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"http://reddit.com/r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"http://reddit.com/r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"

    def test_reddit_subreddit_r_prefix(self):
        """Test Reddit r/ prefix format (e.g., r/subreddit)"""
        sl = SocialLinks()
        subreddit_name = "python"
        # Test r/subreddit format
        assert sl.detect_platform(f"r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"

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

    def test_signal(self):
        """Test Signal platform"""
        sl = SocialLinks()
        profile_id = "abc123xyz"
        assert sl.detect_platform(f"https://signal.me/#p/{profile_id}") == "signal"
        assert sl.is_valid("signal", f"https://signal.me/#p/{profile_id}") is True
        assert sl.sanitize("signal", f"https://signal.me/#p/{profile_id}") == f"https://signal.me/#p/{profile_id}"
        # Test direct profile ID
        assert sl.is_valid("signal", profile_id) is True
        assert sl.sanitize("signal", profile_id) == f"https://signal.me/#p/{profile_id}"

    def test_signal_with_www(self):
        """Test Signal with www subdomain"""
        sl = SocialLinks()
        profile_id = "abc123xyz"
        assert sl.detect_platform(f"https://www.signal.me/#p/{profile_id}") == "signal"
        assert sl.is_valid("signal", f"https://www.signal.me/#p/{profile_id}") is True
        assert sl.sanitize("signal", f"https://www.signal.me/#p/{profile_id}") == f"https://signal.me/#p/{profile_id}"

    def test_signal_with_http(self):
        """Test Signal with http protocol"""
        sl = SocialLinks()
        profile_id = "abc123xyz"
        assert sl.detect_platform(f"http://signal.me/#p/{profile_id}") == "signal"
        assert sl.is_valid("signal", f"http://signal.me/#p/{profile_id}") is True
        assert sl.sanitize("signal", f"http://signal.me/#p/{profile_id}") == f"https://signal.me/#p/{profile_id}"

    def test_signal_with_trailing_slash(self):
        """Test Signal with trailing slash"""
        sl = SocialLinks()
        profile_id = "abc123xyz"
        assert sl.is_valid("signal", f"https://signal.me/#p/{profile_id}/") is True
        assert sl.sanitize("signal", f"https://signal.me/#p/{profile_id}/") == f"https://signal.me/#p/{profile_id}"

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

    def test_whatsapp_send_format(self):
        """Test WhatsApp whatsapp.com/send?phone= format"""
        sl = SocialLinks()
        phone_number = "1234567890"
        # Test whatsapp.com/send?phone= format
        assert sl.detect_platform(f"https://whatsapp.com/send?phone={phone_number}") == "whatsapp"
        assert sl.is_valid("whatsapp", f"https://whatsapp.com/send?phone={phone_number}") is True
        assert sl.sanitize("whatsapp", f"https://whatsapp.com/send?phone={phone_number}") == f"https://wa.me/{phone_number}"
        # Test with www subdomain
        assert sl.is_valid("whatsapp", f"https://www.whatsapp.com/send?phone={phone_number}") is True
        assert sl.sanitize("whatsapp", f"https://www.whatsapp.com/send?phone={phone_number}") == f"https://wa.me/{phone_number}"
        # Test http protocol
        assert sl.is_valid("whatsapp", f"http://whatsapp.com/send?phone={phone_number}") is True
        assert sl.sanitize("whatsapp", f"http://whatsapp.com/send?phone={phone_number}") == f"https://wa.me/{phone_number}"

    def test_whatsapp_send_format_with_plus(self):
        """Test WhatsApp whatsapp.com/send?phone= format with international format"""
        sl = SocialLinks()
        phone_number = "+1234567890"
        # Test whatsapp.com/send?phone= format with +
        assert sl.detect_platform(f"https://whatsapp.com/send?phone={phone_number}") == "whatsapp"
        assert sl.is_valid("whatsapp", f"https://whatsapp.com/send?phone={phone_number}") is True
        assert sl.sanitize("whatsapp", f"https://whatsapp.com/send?phone={phone_number}") == f"https://wa.me/{phone_number}"

    def test_wechat(self):
        """Test WeChat platform with open.weixin.qq.com format"""
        sl = SocialLinks()
        username = "DutchEmbassy_BJ"
        assert sl.detect_platform(f"https://open.weixin.qq.com/qr/code?username={username}") == "wechat"
        assert sl.is_valid("wechat", f"https://open.weixin.qq.com/qr/code?username={username}") is True
        assert sl.sanitize("wechat", f"https://open.weixin.qq.com/qr/code?username={username}") == f"https://open.weixin.qq.com/qr/code?username={username}"
        # Test direct username
        assert sl.is_valid("wechat", username) is True
        assert sl.sanitize("wechat", username) == f"https://open.weixin.qq.com/qr/code?username={username}"

    def test_wechat_weixin_protocol(self):
        """Test WeChat with weixin:// protocol"""
        sl = SocialLinks()
        username = "Bright_Writers"
        assert sl.detect_platform(f"weixin://dl/chat?{username}") == "wechat"
        assert sl.is_valid("wechat", f"weixin://dl/chat?{username}") is True
        assert sl.sanitize("wechat", f"weixin://dl/chat?{username}") == f"https://open.weixin.qq.com/qr/code?username={username}"

    def test_weibo(self):
        """Test Weibo platform with direct username"""
        sl = SocialLinks()
        username = "guanzhilin"
        assert sl.detect_platform(f"https://weibo.com/{username}") == "weibo"
        assert sl.is_valid("weibo", f"https://weibo.com/{username}") is True
        assert sl.sanitize("weibo", f"https://weibo.com/{username}") == f"https://weibo.com/{username}"
        # Test direct username
        assert sl.is_valid("weibo", username) is True
        assert sl.sanitize("weibo", username) == f"https://weibo.com/{username}"

    def test_weibo_user_id(self):
        """Test Weibo platform with /u/ user ID format"""
        sl = SocialLinks()
        user_id = "1669879400"
        assert sl.detect_platform(f"https://weibo.com/u/{user_id}") == "weibo"
        assert sl.is_valid("weibo", f"https://weibo.com/u/{user_id}") is True
        assert sl.sanitize("weibo", f"https://weibo.com/u/{user_id}") == f"https://weibo.com/u/{user_id}"

    def test_weibo_variations(self):
        """Test Weibo with various URL formats"""
        sl = SocialLinks()
        username = "guanzhilin"
        
        # Test with www subdomain
        assert sl.detect_platform(f"https://www.weibo.com/{username}") == "weibo"
        assert sl.is_valid("weibo", f"https://www.weibo.com/{username}") is True
        assert sl.sanitize("weibo", f"https://www.weibo.com/{username}") == f"https://weibo.com/{username}"
        
        # Test with trailing slash
        assert sl.is_valid("weibo", f"https://weibo.com/{username}/") is True
        assert sl.sanitize("weibo", f"https://weibo.com/{username}/") == f"https://weibo.com/{username}"
        
        # Test http protocol
        assert sl.detect_platform(f"http://weibo.com/{username}") == "weibo"
        assert sl.is_valid("weibo", f"http://weibo.com/{username}") is True
        assert sl.sanitize("weibo", f"http://weibo.com/{username}") == f"https://weibo.com/{username}"
        
        # Test /u/ format with www
        user_id = "1669879400"
        assert sl.is_valid("weibo", f"https://www.weibo.com/u/{user_id}") is True
        assert sl.sanitize("weibo", f"https://www.weibo.com/u/{user_id}") == f"https://weibo.com/u/{user_id}"

    def test_quora_profile(self):
        """Test Quora platform with /profile/ path"""
        sl = SocialLinks()
        username = "Jay-Hoque"
        assert sl.detect_platform(f"https://www.quora.com/profile/{username}") == "quora"
        assert sl.is_valid("quora", f"https://www.quora.com/profile/{username}") is True
        assert sl.sanitize("quora", f"https://www.quora.com/profile/{username}") == f"https://quora.com/profile/{username}"
        # Test direct username
        assert sl.is_valid("quora", username) is True
        assert sl.sanitize("quora", username) == f"https://quora.com/profile/{username}"

    def test_quora_direct_username(self):
        """Test Quora platform with direct username path"""
        sl = SocialLinks()
        username = "Uthma-Faheem"
        assert sl.detect_platform(f"https://www.quora.com/{username}") == "quora"
        assert sl.is_valid("quora", f"https://www.quora.com/{username}") is True
        assert sl.sanitize("quora", f"https://www.quora.com/{username}") == f"https://quora.com/profile/{username}"

    def test_quora_with_http(self):
        """Test Quora with http protocol"""
        sl = SocialLinks()
        username = "Jay-Hoque"
        assert sl.detect_platform(f"http://quora.com/profile/{username}") == "quora"
        assert sl.is_valid("quora", f"http://quora.com/profile/{username}") is True
        assert sl.sanitize("quora", f"http://quora.com/profile/{username}") == f"https://quora.com/profile/{username}"

    def test_quora_with_trailing_slash(self):
        """Test Quora with trailing slash"""
        sl = SocialLinks()
        username = "Jay-Hoque"
        assert sl.is_valid("quora", f"https://quora.com/profile/{username}/") is True
        assert sl.sanitize("quora", f"https://quora.com/profile/{username}/") == f"https://quora.com/profile/{username}"

    def test_quora_with_unicode(self):
        """Test Quora profile with Unicode characters (URL-encoded)"""
        sl = SocialLinks()
        username = "Nitish-Kumar-%E0%A4%A8%E0%A5%80%E0%A4%A4%E0%A5%80%E0%A4%B6"
        assert sl.detect_platform(f"https://www.quora.com/profile/{username}") == "quora"
        assert sl.is_valid("quora", f"https://www.quora.com/profile/{username}") is True
        assert sl.sanitize("quora", f"https://www.quora.com/profile/{username}") == f"https://quora.com/profile/{username}"

    def test_steam_id(self):
        """Test Steam platform with /id/ path"""
        sl = SocialLinks()
        username = "pepepro76561198317693716"
        assert sl.detect_platform(f"https://steamcommunity.com/id/{username}") == "steam"
        assert sl.is_valid("steam", f"https://steamcommunity.com/id/{username}") is True
        assert sl.sanitize("steam", f"https://steamcommunity.com/id/{username}") == f"https://steamcommunity.com/id/{username}"
        # Test direct username
        assert sl.is_valid("steam", username) is True
        assert sl.sanitize("steam", username) == f"https://steamcommunity.com/id/{username}"

    def test_steam_profiles(self):
        """Test Steam platform with /profiles/ path (numeric Steam ID)"""
        sl = SocialLinks()
        steam_id = "76561198014898339"
        assert sl.detect_platform(f"https://steamcommunity.com/profiles/{steam_id}") == "steam"
        assert sl.is_valid("steam", f"https://steamcommunity.com/profiles/{steam_id}") is True
        # Profiles path should be preserved (not converted to /id/)
        assert sl.sanitize("steam", f"https://steamcommunity.com/profiles/{steam_id}") == f"https://steamcommunity.com/profiles/{steam_id}"

    def test_steam_with_www(self):
        """Test Steam with www subdomain"""
        sl = SocialLinks()
        username = "testuser"
        assert sl.detect_platform(f"https://www.steamcommunity.com/id/{username}") == "steam"
        assert sl.is_valid("steam", f"https://www.steamcommunity.com/id/{username}") is True
        assert sl.sanitize("steam", f"https://www.steamcommunity.com/id/{username}") == f"https://steamcommunity.com/id/{username}"

    def test_steam_with_http(self):
        """Test Steam with http protocol"""
        sl = SocialLinks()
        username = "testuser"
        assert sl.detect_platform(f"http://steamcommunity.com/id/{username}") == "steam"
        assert sl.is_valid("steam", f"http://steamcommunity.com/id/{username}") is True
        assert sl.sanitize("steam", f"http://steamcommunity.com/id/{username}") == f"https://steamcommunity.com/id/{username}"

    def test_steam_with_trailing_slash(self):
        """Test Steam with trailing slash"""
        sl = SocialLinks()
        username = "testuser"
        assert sl.is_valid("steam", f"https://steamcommunity.com/id/{username}/") is True
        assert sl.sanitize("steam", f"https://steamcommunity.com/id/{username}/") == f"https://steamcommunity.com/id/{username}"


