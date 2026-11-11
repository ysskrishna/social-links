"""Tests for Facebook platform."""


class TestFacebook:
    """Test Facebook platform"""

    def test_facebook(self, sl):
        """Test Facebook desktop platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://facebook.com/{profile_id}") == "facebook"
        assert sl.is_valid("facebook", f"https://facebook.com/{profile_id}") is True
        assert sl.sanitize("facebook", f"https://facebook.com/{profile_id}") == f"https://facebook.com/{profile_id}"
        # Test direct username
        assert sl.is_valid("facebook", profile_id) is True
        assert sl.sanitize("facebook", profile_id) == f"https://facebook.com/{profile_id}"

    def test_facebook_mobile(self, sl):
        """Test Facebook mobile platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://m.facebook.com/{profile_id}") == "facebook"
        assert sl.is_valid("facebook", f"https://m.facebook.com/{profile_id}") is True
        assert sl.sanitize("facebook", f"https://m.facebook.com/{profile_id}") == f"https://facebook.com/{profile_id}"

    def test_facebook_profile_php(self, sl):
        """Accounts without a vanity name use profile.php?id=<digits>"""
        url = "https://www.facebook.com/profile.php?id=100000000000000"
        assert sl.detect_platform(url) == "facebook"
        assert sl.is_valid("facebook", url) is True
        assert sl.sanitize("facebook", url) == "https://facebook.com/profile.php?id=100000000000000"
        assert sl.extract_id("facebook", url) == "100000000000000"
        # extra parameters and the mobile host
        assert sl.sanitize("facebook", "https://m.facebook.com/profile.php?id=4&sk=about") == "https://facebook.com/profile.php?id=4"
        # non-numeric ids and a missing id are not profiles
        assert sl.is_valid("facebook", "https://facebook.com/profile.php?id=abc") is False
        assert sl.detect_platform("https://facebook.com/profile.php?foo=1") is None
