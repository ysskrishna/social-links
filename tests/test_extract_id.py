import pytest
from sociallinks import extract_id as module_extract_id, sanitize
from sociallinks.core import SocialLinks
from sociallinks.exceptions import (
    PlatformNotFoundError,
    URLMismatchError,
    PlatformIDExtractionError,
)


class TestExtractIdClassMethod:
    """Test SocialLinks.extract_id() class method — success cases across platforms"""

    def setup_method(self):
        self.sl = SocialLinks()

    # LinkedIn variants
    def test_linkedin_personal(self):
        assert self.sl.extract_id("linkedin", "https://www.linkedin.com/in/johndoe/") == "johndoe"

    def test_linkedin_personal_http(self):
        assert self.sl.extract_id("linkedin", "http://linkedin.com/in/johndoe") == "johndoe"

    def test_linkedin_company(self):
        assert self.sl.extract_id("linkedin", "https://www.linkedin.com/company/acme/") == "acme"

    def test_linkedin_school(self):
        assert self.sl.extract_id("linkedin", "https://www.linkedin.com/school/mit/") == "mit"

    def test_linkedin_mobile(self):
        assert self.sl.extract_id("linkedin", "https://www.linkedin.com/mwlite/in/johndoe") == "johndoe"

    def test_linkedin_unicode(self):
        assert self.sl.extract_id("linkedin", "https://www.linkedin.com/in/josé-garcía/") == "josé-garcía"

    # GitHub
    def test_github(self):
        assert self.sl.extract_id("github", "https://github.com/username") == "username"

    def test_github_www(self):
        assert self.sl.extract_id("github", "https://www.github.com/user123") == "user123"

    def test_github_http(self):
        assert self.sl.extract_id("github", "http://github.com/my-user") == "my-user"

    # X / Twitter
    def test_x_native(self):
        assert self.sl.extract_id("x", "https://x.com/elonmusk") == "elonmusk"

    def test_x_from_twitter(self):
        assert self.sl.extract_id("x", "https://twitter.com/username") == "username"

    def test_x_mobile_twitter(self):
        assert self.sl.extract_id("x", "https://mobile.twitter.com/username") == "username"

    # Facebook
    def test_facebook(self):
        assert self.sl.extract_id("facebook", "https://www.facebook.com/johndoe/") == "johndoe"

    def test_facebook_http(self):
        assert self.sl.extract_id("facebook", "http://facebook.com/janedoe") == "janedoe"

    # Instagram
    def test_instagram(self):
        assert self.sl.extract_id("instagram", "https://www.instagram.com/johndoe/") == "johndoe"

    def test_instagram_http(self):
        assert self.sl.extract_id("instagram", "http://instagram.com/janedoe") == "janedoe"

    # YouTube
    def test_youtube_handle(self):
        assert self.sl.extract_id("youtube", "https://www.youtube.com/@channel") == "@channel"

    def test_youtube_channel_id(self):
        result = self.sl.extract_id("youtube", "https://www.youtube.com/channel/UC12345")
        assert result == "UC12345"


class TestExtractIdModuleFunction:
    """Test module-level extract_id() convenience function"""

    def test_module_function_works(self):
        assert module_extract_id("github", "https://github.com/username") == "username"

    def test_module_function_matches_class_method(self):
        sl = SocialLinks()
        url = "https://www.linkedin.com/in/johndoe/"
        assert module_extract_id("linkedin", url) == sl.extract_id("linkedin", url)

    def test_module_function_linkedin(self):
        assert module_extract_id("linkedin", "https://linkedin.com/in/johndoe") == "johndoe"

    def test_module_function_x(self):
        assert module_extract_id("x", "https://twitter.com/elonmusk") == "elonmusk"

    def test_module_function_facebook(self):
        assert module_extract_id("facebook", "https://facebook.com/johndoe") == "johndoe"


class TestExtractIdErrorHandling:
    """Test all error paths for extract_id()"""

    def setup_method(self):
        self.sl = SocialLinks()

    # TypeError — non-string inputs
    def test_type_error_none_url(self):
        with pytest.raises(TypeError, match="url must be str, not NoneType"):
            self.sl.extract_id("linkedin", None)

    def test_type_error_int_url(self):
        with pytest.raises(TypeError, match="url must be str, not int"):
            self.sl.extract_id("linkedin", 123)

    def test_type_error_float_url(self):
        with pytest.raises(TypeError, match="url must be str, not float"):
            self.sl.extract_id("linkedin", 3.14)

    def test_type_error_list_url(self):
        with pytest.raises(TypeError, match="url must be str, not list"):
            self.sl.extract_id("linkedin", ["https://linkedin.com/in/johndoe"])

    def test_type_error_dict_url(self):
        with pytest.raises(TypeError, match="url must be str, not dict"):
            self.sl.extract_id("linkedin", {"url": "https://linkedin.com/in/johndoe"})

    def test_type_error_none_platform(self):
        with pytest.raises(TypeError, match="platform_name must be str, not NoneType"):
            self.sl.extract_id(None, "https://linkedin.com/in/johndoe")

    def test_type_error_int_platform(self):
        with pytest.raises(TypeError, match="platform_name must be str, not int"):
            self.sl.extract_id(123, "https://linkedin.com/in/johndoe")

    # PlatformNotFoundError
    def test_platform_not_found(self):
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            self.sl.extract_id("unknown_platform", "https://example.com/user")

    def test_platform_not_found_empty_name(self):
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            self.sl.extract_id("", "https://example.com/user")

    # URLMismatchError
    def test_url_mismatch(self):
        with pytest.raises(URLMismatchError, match="does not match platform"):
            self.sl.extract_id("linkedin", "https://example.com")

    def test_empty_url(self):
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            self.sl.extract_id("linkedin", "")

    def test_whitespace_url(self):
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            self.sl.extract_id("linkedin", "   ")

    def test_tab_newline_url(self):
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            self.sl.extract_id("linkedin", "\t\n")


class TestExtractIdEdgeCases:
    """Test edge cases for extract_id()"""

    def setup_method(self):
        self.sl = SocialLinks()

    def test_whitespace_handling(self):
        """Leading/trailing whitespace is stripped before matching"""
        result = self.sl.extract_id("linkedin", "  https://www.linkedin.com/in/johndoe/  ")
        assert result == "johndoe"

    def test_case_insensitive(self):
        """URL matching is case insensitive"""
        result = self.sl.extract_id("linkedin", "HTTPS://WWW.LINKEDIN.COM/IN/JohnDoe/")
        assert result == "JohnDoe"

    def test_trailing_slash_stripped(self):
        """Trailing slash on ID is stripped"""
        result = self.sl.extract_id("github", "https://github.com/username/")
        assert result == "username"

    def test_consistency_with_sanitize(self):
        """extract_id result is consistent with what sanitize uses"""
        url = "https://www.linkedin.com/in/johndoe/"
        pid = self.sl.extract_id("linkedin", url)
        sanitized = self.sl.sanitize("linkedin", url)
        assert sanitized == f"https://linkedin.com/in/{pid}"

    def test_consistency_with_sanitize_github(self):
        """extract_id result is consistent with sanitize for GitHub"""
        url = "http://www.github.com/myuser"
        pid = self.sl.extract_id("github", url)
        sanitized = self.sl.sanitize("github", url)
        assert sanitized == f"https://github.com/{pid}"

    def test_consistency_with_sanitize_x(self):
        """extract_id result is consistent with sanitize for X"""
        url = "https://twitter.com/username"
        pid = self.sl.extract_id("x", url)
        sanitized = self.sl.sanitize("x", url)
        assert sanitized == f"https://x.com/{pid}"

    def test_no_platforms_configured(self):
        """extract_id raises PlatformNotFoundError when no platforms configured"""
        sl = SocialLinks(use_predefined_platforms=False)
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            sl.extract_id("linkedin", "https://linkedin.com/in/johndoe")
