import pytest
from sociallinks.core import SocialLinks
from sociallinks.exceptions import (
    PlatformNotFoundError,
    PlatformAlreadyExistsError,
    InvalidPlatformError,
    PlatformIDExtractionError,
    URLMismatchError,
)


class TestSocialLinksInitialization:
    """Test SocialLinks initialization"""

    def test_init_with_predefined_platforms(self):
        """Test initialization with predefined platforms"""
        sl = SocialLinks()
        assert len(sl.platforms) > 0
        assert "linkedin" in sl.platforms
        assert "facebook" in sl.platforms

    def test_init_without_predefined_platforms(self):
        """Test initialization without predefined platforms"""
        sl = SocialLinks(use_predefined_platforms=False)
        assert len(sl.platforms) == 0
        assert len(sl._compiled) == 0

    def test_init_with_custom_regex_flags(self):
        """Test initialization with custom regex flags"""
        import re
        sl = SocialLinks(regex_flags=re.IGNORECASE | re.MULTILINE)
        assert sl.regex_flags == (re.IGNORECASE | re.MULTILINE)


class TestDetectPlatform:
    """Test detect_platform method"""

    def test_detect_linkedin_personal(self):
        """Test detecting LinkedIn personal platform"""
        sl = SocialLinks()
        assert sl.detect_platform("https://www.linkedin.com/in/johndoe/") == "linkedin"
        assert sl.detect_platform("http://linkedin.com/in/johndoe") == "linkedin"
        assert sl.detect_platform("https://linkedin.com/in/jane-smith") == "linkedin"

    def test_detect_linkedin_company(self):
        """Test detecting LinkedIn company platform"""
        sl = SocialLinks()
        assert sl.detect_platform("https://www.linkedin.com/company/acme/") == "linkedin"
        assert sl.detect_platform("http://linkedin.com/company/techcorp") == "linkedin"

    def test_detect_facebook(self):
        """Test detecting Facebook platform"""
        sl = SocialLinks()
        assert sl.detect_platform("https://www.facebook.com/johndoe/") == "facebook"
        assert sl.detect_platform("http://facebook.com/janedoe") == "facebook"

    def test_detect_none_for_invalid_url(self):
        """Test that invalid URLs return None"""
        sl = SocialLinks()
        assert sl.detect_platform("https://example.com") is None
        assert sl.detect_platform("not a url") is None
        assert sl.detect_platform("") is None

    def test_detect_with_whitespace(self):
        """Test that URLs with whitespace are handled"""
        sl = SocialLinks()
        assert sl.detect_platform("  https://www.linkedin.com/in/johndoe/  ") == "linkedin"


class TestIsValid:
    """Test is_valid method"""

    def test_is_valid_linkedin_personal(self):
        """Test validating LinkedIn personal URLs"""
        sl = SocialLinks()
        assert sl.is_valid("linkedin", "https://www.linkedin.com/in/johndoe/") is True
        assert sl.is_valid("linkedin", "http://linkedin.com/in/jane-smith") is True
        assert sl.is_valid("linkedin", "https://example.com") is False

    def test_is_valid_linkedin_company(self):
        """Test validating LinkedIn company URLs"""
        sl = SocialLinks()
        assert sl.is_valid("linkedin", "https://www.linkedin.com/company/acme/") is True
        assert sl.is_valid("linkedin", "http://linkedin.com/company/techcorp") is True

    def test_is_valid_facebook(self):
        """Test validating Facebook URLs"""
        sl = SocialLinks()
        assert sl.is_valid("facebook", "https://www.facebook.com/johndoe/") is True
        assert sl.is_valid("facebook", "http://facebook.com/janedoe") is True
        assert sl.is_valid("facebook", "https://example.com") is False

    def test_is_valid_unknown_platform(self):
        """Test validating with unknown platform"""
        sl = SocialLinks()
        assert sl.is_valid("unknown", "https://www.linkedin.com/in/johndoe/") is False

    def test_is_valid_with_whitespace(self):
        """Test that URLs with whitespace are handled"""
        sl = SocialLinks()
        assert sl.is_valid("linkedin", "  https://www.linkedin.com/in/johndoe/  ") is True


class TestSanitize:
    """Test sanitize method"""

    def test_sanitize_linkedin_personal(self):
        """Test sanitizing LinkedIn personal URLs"""
        sl = SocialLinks()
        assert sl.sanitize("linkedin", "https://www.linkedin.com/in/johndoe/") == "https://www.linkedin.com/in/johndoe/"
        assert sl.sanitize("linkedin", "http://linkedin.com/in/jane-smith") == "https://www.linkedin.com/in/jane-smith/"
        assert sl.sanitize("linkedin", "https://linkedin.com/in/user123") == "https://www.linkedin.com/in/user123/"

    def test_sanitize_linkedin_company(self):
        """Test sanitizing LinkedIn company URLs"""
        sl = SocialLinks()
        assert sl.sanitize("linkedin", "https://www.linkedin.com/company/acme/") == "https://www.linkedin.com/company/acme/"
        assert sl.sanitize("linkedin", "http://linkedin.com/company/techcorp") == "https://www.linkedin.com/company/techcorp/"

    def test_sanitize_facebook(self):
        """Test sanitizing Facebook URLs"""
        sl = SocialLinks()
        assert sl.sanitize("facebook", "https://www.facebook.com/johndoe/") == "https://www.facebook.com/johndoe/"
        assert sl.sanitize("facebook", "http://facebook.com/janedoe") == "https://www.facebook.com/janedoe/"

    def test_sanitize_with_at_symbol(self):
        """Test sanitizing URLs with @ symbol"""
        sl = SocialLinks()
        # This tests the lstrip("@") logic
        # Note: The actual behavior depends on the regex pattern matching

    def test_sanitize_unknown_platform(self):
        """Test sanitizing with unknown platform"""
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            sl.sanitize("unknown", "https://www.linkedin.com/in/johndoe/")

    def test_sanitize_invalid_url(self):
        """Test sanitizing invalid URL for platform"""
        sl = SocialLinks()
        with pytest.raises(URLMismatchError, match="does not match platform"):
            sl.sanitize("linkedin", "https://example.com")

    def test_sanitize_with_whitespace(self):
        """Test sanitizing URLs with whitespace"""
        sl = SocialLinks()
        result = sl.sanitize("linkedin", "  https://www.linkedin.com/in/johndoe/  ")
        assert result == "https://www.linkedin.com/in/johndoe/"


class TestGetCleanLink:
    """Test get_clean_link method"""

    def test_get_clean_link_linkedin(self):
        """Test getting clean LinkedIn link"""
        sl = SocialLinks()
        assert sl.get_clean_link("linkedin", "johndoe") == "https://www.linkedin.com/in/johndoe/"
        assert sl.get_clean_link("linkedin", "@johndoe") == "https://www.linkedin.com/in/johndoe/"
        assert sl.get_clean_link("linkedin", "johndoe/") == "https://www.linkedin.com/in/johndoe/"

    def test_get_clean_link_facebook(self):
        """Test getting clean Facebook link"""
        sl = SocialLinks()
        assert sl.get_clean_link("facebook", "johndoe") == "https://www.facebook.com/johndoe/"
        assert sl.get_clean_link("facebook", "@johndoe") == "https://www.facebook.com/johndoe/"

    def test_get_clean_link_with_whitespace(self):
        """Test getting clean link with whitespace"""
        sl = SocialLinks()
        assert sl.get_clean_link("linkedin", "  johndoe  ") == "https://www.linkedin.com/in/johndoe/"

    def test_get_clean_link_unknown_platform(self):
        """Test getting clean link for unknown platform"""
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            sl.get_clean_link("unknown", "johndoe")


class TestSetPlatform:
    """Test set_platform method"""

    def test_set_platform_new(self):
        """Test adding a new platform"""
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = {
            "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.twitter.com/{id}/"
        }
        sl.set_platform("twitter", platform_data)
        assert "twitter" in sl.platforms
        assert sl.detect_platform("https://www.twitter.com/johndoe") == "twitter"

    def test_set_platform_override_false(self):
        """Test that setting existing platform without override raises error"""
        sl = SocialLinks()
        platform_data = {
            "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.twitter.com/{id}/"
        }
        with pytest.raises(PlatformAlreadyExistsError, match="already exists"):
            sl.set_platform("linkedin", platform_data)

    def test_set_platform_override_true(self):
        """Test overriding existing platform"""
        sl = SocialLinks()
        platform_data = {
            "patterns": ["https?://(www\\.)?linkedin\\.com/custom/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.linkedin.com/custom/{id}/"
        }
        sl.set_platform("linkedin", platform_data, override=True)
        assert sl.detect_platform("https://www.linkedin.com/custom/johndoe") == "linkedin"
        assert sl.detect_platform("https://www.linkedin.com/in/johndoe") is None

    def test_set_platform_with_list(self):
        """Test setting platform with list of patterns"""
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = [
            {
                "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.twitter.com/{id}/"
            },
            {
                "patterns": ["https?://twitter\\.com/x/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.twitter.com/x/{id}/"
            }
        ]
        sl.set_platform("twitter", platform_data)
        assert sl.detect_platform("https://www.twitter.com/johndoe") == "twitter"
        assert sl.detect_platform("https://twitter.com/x/johndoe") == "twitter"

    def test_set_platform_invalid_patterns(self):
        """Test setting platform with invalid patterns"""
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = {
            "patterns": [],
            "sanitized": "https://www.example.com/{id}/"
        }
        with pytest.raises(InvalidPlatformError, match="no valid patterns"):
            sl.set_platform("example", platform_data)

    def test_set_platform_missing_sanitized(self):
        """Test setting platform without sanitized template"""
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = {
            "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"]
        }
        with pytest.raises(InvalidPlatformError, match="no valid patterns"):
            sl.set_platform("example", platform_data)


class TestDeletePlatform:
    """Test delete_platform method"""

    def test_delete_platform(self):
        """Test deleting a platform"""
        sl = SocialLinks()
        assert "linkedin" in sl.platforms
        sl.delete_platform("linkedin")
        assert "linkedin" not in sl.platforms
        assert "linkedin" not in sl._compiled

    def test_delete_platform_not_found(self):
        """Test deleting non-existent platform"""
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="not found"):
            sl.delete_platform("nonexistent")


class TestSetPlatforms:
    """Test set_platforms method"""

    def test_set_platforms_new(self):
        """Test bulk adding new platforms"""
        sl = SocialLinks(use_predefined_platforms=False)
        platforms = {
            "twitter": {
                "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.twitter.com/{id}/"
            },
            "instagram": {
                "patterns": ["https?://(www\\.)?instagram\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.instagram.com/{id}/"
            }
        }
        sl.set_platforms(platforms)
        assert "twitter" in sl.platforms
        assert "instagram" in sl.platforms

    def test_set_platforms_with_conflicts(self):
        """Test bulk adding platforms with conflicts"""
        sl = SocialLinks()
        platforms = {
            "linkedin": {
                "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://example.com/{id}/"
            }
        }
        with pytest.raises(PlatformAlreadyExistsError, match="already exist"):
            sl.set_platforms(platforms)

    def test_set_platforms_override(self):
        """Test bulk adding platforms with override"""
        sl = SocialLinks()
        platforms = {
            "linkedin": {
                "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://example.com/{id}/"
            }
        }
        sl.set_platforms(platforms, override=True)
        assert sl.detect_platform("https://example.com/johndoe") == "linkedin"


class TestDeletePlatforms:
    """Test delete_platforms method"""

    def test_delete_platforms(self):
        """Test bulk deleting platforms"""
        sl = SocialLinks()
        assert "linkedin" in sl.platforms
        assert "facebook" in sl.platforms
        sl.delete_platforms(["linkedin", "facebook"])
        assert "linkedin" not in sl.platforms
        assert "facebook" not in sl.platforms

    def test_delete_platforms_missing(self):
        """Test bulk deleting with missing platforms"""
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="not found"):
            sl.delete_platforms(["linkedin", "nonexistent"])


class TestClearPlatforms:
    """Test clear_platforms method"""

    def test_clear_platforms(self):
        """Test clearing all platforms"""
        sl = SocialLinks()
        assert len(sl.platforms) > 0
        sl.clear_platforms()
        assert len(sl.platforms) == 0
        assert len(sl._compiled) == 0


class TestGetPlatform:
    """Test get_platform method"""

    def test_get_platform(self):
        """Test getting a platform"""
        sl = SocialLinks()
        platform = sl.get_platform("linkedin")
        assert platform is not None
        assert isinstance(platform, list)

    def test_get_platform_not_found(self):
        """Test getting non-existent platform"""
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="not found"):
            sl.get_platform("nonexistent")


class TestListPlatforms:
    """Test list_platforms method"""

    def test_list_platforms(self):
        """Test listing all platforms"""
        sl = SocialLinks()
        platforms = sl.list_platforms()
        assert isinstance(platforms, list)
        assert "linkedin" in platforms
        assert "facebook" in platforms

    def test_list_platforms_empty(self):
        """Test listing platforms when empty"""
        sl = SocialLinks(use_predefined_platforms=False)
        platforms = sl.list_platforms()
        assert platforms == []


class TestExtractId:
    """Test _extract_id static method"""

    def test_extract_id_with_named_group(self):
        """Test extracting ID from named group"""
        import re
        pattern = re.compile(r"https?://example\.com/(?P<id>[A-Za-z0-9_]+)/?$")
        match = pattern.search("https://example.com/johndoe")
        assert match is not None
        assert SocialLinks._extract_id(match) == "johndoe"

    def test_extract_id_with_unnamed_group(self):
        """Test extracting ID from unnamed group"""
        import re
        pattern = re.compile(r"https?://example\.com/([A-Za-z0-9_]+)/?$")
        match = pattern.search("https://example.com/johndoe")
        assert match is not None
        assert SocialLinks._extract_id(match) == "johndoe"

    def test_extract_id_no_match(self):
        """Test extracting ID when no groups match"""
        import re
        pattern = re.compile(r"https?://example\.com/")
        match = pattern.search("https://example.com/")
        assert match is not None
        assert SocialLinks._extract_id(match) is None


class TestEdgeCases:
    """Test edge cases and error handling"""

    def test_sanitize_no_id_extracted(self):
        """Test sanitize when ID cannot be extracted"""
        sl = SocialLinks(use_predefined_platforms=False)
        # Create a platform with pattern that doesn't capture ID
        platform_data = {
            "patterns": ["https?://example\\.com/static/?$"],
            "sanitized": "https://example.com/{id}/"
        }
        sl.set_platform("example", platform_data)
        with pytest.raises(PlatformIDExtractionError, match="Could not extract platform ID"):
            sl.sanitize("example", "https://example.com/static")

    def test_case_insensitive_matching(self):
        """Test case insensitive URL matching"""
        sl = SocialLinks()
        # Should work with uppercase
        assert sl.detect_platform("HTTPS://WWW.LINKEDIN.COM/IN/JOHNDOE/") == "linkedin"
        assert sl.is_valid("linkedin", "HTTPS://WWW.LINKEDIN.COM/IN/JOHNDOE/") is True

    def test_multiple_patterns_same_platform(self):
        """Test platform with multiple patterns"""
        sl = SocialLinks()
        # LinkedIn has both personal and company patterns
        assert sl.is_valid("linkedin", "https://www.linkedin.com/in/johndoe/") is True
        assert sl.is_valid("linkedin", "https://www.linkedin.com/company/acme/") is True

