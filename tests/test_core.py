import pytest
from sociallinks.core import SocialLinks
from sociallinks.exceptions import (
    PlatformNotFoundError,
    URLMismatchError,
)


class TestSocialLinksInitialization:
    def test_init_with_predefined_platforms(self):
        sl = SocialLinks()
        assert len(sl.platforms) >= 50  # Should have all predefined platforms (37 as of current version)
        assert "linkedin" in sl.platforms
        assert "facebook" in sl.platforms
        assert "github" in sl.platforms
        assert "instagram" in sl.platforms
        assert "youtube" in sl.platforms
        assert "x" in sl.platforms
        assert "discord" in sl.platforms
        assert "threads" in sl.platforms

    def test_init_without_predefined_platforms(self):
        sl = SocialLinks(use_predefined_platforms=False)
        assert len(sl.platforms) == 0
        assert len(sl._compiled) == 0

    def test_init_with_custom_regex_flags(self):
        import re
        sl = SocialLinks(regex_flags=re.IGNORECASE | re.MULTILINE)
        assert sl.regex_flags == (re.IGNORECASE | re.MULTILINE)


class TestDetectPlatform:
    def test_detect_linkedin_personal(self):
        sl = SocialLinks()
        assert sl.detect_platform("https://www.linkedin.com/in/johndoe/") == "linkedin"
        assert sl.detect_platform("http://linkedin.com/in/johndoe") == "linkedin"
        assert sl.detect_platform("https://linkedin.com/in/jane-smith") == "linkedin"

    def test_detect_linkedin_company(self):
        sl = SocialLinks()
        assert sl.detect_platform("https://www.linkedin.com/company/acme/") == "linkedin"
        assert sl.detect_platform("http://linkedin.com/company/techcorp") == "linkedin"

    def test_detect_facebook(self):
        sl = SocialLinks()
        assert sl.detect_platform("https://www.facebook.com/johndoe/") == "facebook"
        assert sl.detect_platform("http://facebook.com/janedoe") == "facebook"

    def test_detect_none_for_invalid_url(self):
        sl = SocialLinks()
        assert sl.detect_platform("https://example.com") is None
        assert sl.detect_platform("not a url") is None
        assert sl.detect_platform("") is None


class TestIsValid:
    def test_is_valid_linkedin_personal(self):
        sl = SocialLinks()
        assert sl.is_valid("linkedin", "https://www.linkedin.com/in/johndoe/") is True
        assert sl.is_valid("linkedin", "http://linkedin.com/in/jane-smith") is True
        assert sl.is_valid("linkedin", "https://example.com") is False

    def test_is_valid_linkedin_company(self):
        sl = SocialLinks()
        assert sl.is_valid("linkedin", "https://www.linkedin.com/company/acme/") is True
        assert sl.is_valid("linkedin", "http://linkedin.com/company/techcorp") is True

    def test_is_valid_facebook(self):
        sl = SocialLinks()
        assert sl.is_valid("facebook", "https://www.facebook.com/johndoe/") is True
        assert sl.is_valid("facebook", "http://facebook.com/janedoe") is True
        assert sl.is_valid("facebook", "https://example.com") is False

    def test_is_valid_unknown_platform(self):
        sl = SocialLinks()
        assert sl.is_valid("unknown", "https://www.linkedin.com/in/johndoe/") is False


class TestSanitize:
    def test_sanitize_unknown_platform(self):
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            sl.sanitize("unknown", "https://www.linkedin.com/in/johndoe/")

    def test_sanitize_invalid_url(self):
        sl = SocialLinks()
        with pytest.raises(URLMismatchError, match="does not match platform"):
            sl.sanitize("linkedin", "https://example.com")


class TestExtractId:
    def test_extract_id_linkedin_personal(self):
        sl = SocialLinks()
        assert sl.extract_id("linkedin", "https://www.linkedin.com/in/johndoe/") == "johndoe"

    def test_extract_id_linkedin_company(self):
        sl = SocialLinks()
        assert sl.extract_id("linkedin", "https://www.linkedin.com/company/acme/") == "acme"

    def test_extract_id_github(self):
        sl = SocialLinks()
        assert sl.extract_id("github", "https://github.com/username") == "username"

    def test_extract_id_x_from_twitter(self):
        sl = SocialLinks()
        assert sl.extract_id("x", "https://twitter.com/elonmusk") == "elonmusk"

    def test_extract_id_unknown_platform(self):
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            sl.extract_id("unknown", "https://example.com/user")

    def test_extract_id_invalid_url(self):
        sl = SocialLinks()
        with pytest.raises(URLMismatchError, match="does not match platform"):
            sl.extract_id("linkedin", "https://example.com")
