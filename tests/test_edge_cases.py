import pytest
import re
from sociallinks.core import SocialLinks
from sociallinks.exceptions import (
    PlatformIDExtractionError,
    URLMismatchError,
)


class TestExtractId:
    def test_id_from_match_with_named_group(self):
        pattern = re.compile(r"https?://example\.com/(?P<id>[A-Za-z0-9_]+)/?$")
        match = pattern.search("https://example.com/johndoe")
        assert match is not None
        assert SocialLinks._id_from_match(match) == "johndoe"

    def test_id_from_match_with_unnamed_group(self):
        pattern = re.compile(r"https?://example\.com/([A-Za-z0-9_]+)/?$")
        match = pattern.search("https://example.com/johndoe")
        assert match is not None
        assert SocialLinks._id_from_match(match) == "johndoe"

    def test_id_from_match_no_match(self):
        pattern = re.compile(r"https?://example\.com/")
        match = pattern.search("https://example.com/")
        assert match is not None
        assert SocialLinks._id_from_match(match) is None


class TestEdgeCases:
    def test_sanitize_no_id_extracted(self):
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = [{
            "patterns": ["https?://example\\.com/static/?$"],
            "sanitized": "https://example.com/{id}/"
        }]
        sl.set_platform("example", platform_data)
        with pytest.raises(PlatformIDExtractionError, match="Could not extract platform ID"):
            sl.sanitize("example", "https://example.com/static")

    def test_case_insensitive_matching(self):
        sl = SocialLinks()
        assert sl.detect_platform("HTTPS://WWW.LINKEDIN.COM/IN/JOHNDOE/") == "linkedin"
        assert sl.is_valid("linkedin", "HTTPS://WWW.LINKEDIN.COM/IN/JOHNDOE/") is True

    def test_multiple_patterns_same_platform(self):
        sl = SocialLinks()
        assert sl.is_valid("linkedin", "https://www.linkedin.com/in/johndoe/") is True
        assert sl.is_valid("linkedin", "https://www.linkedin.com/company/acme/") is True


class TestInputTypeValidation:
    def test_detect_platform_none(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not NoneType"):
            sl.detect_platform(None)

    def test_detect_platform_int(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not int"):
            sl.detect_platform(123)

    def test_detect_platform_list(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not list"):
            sl.detect_platform(["https://linkedin.com/in/johndoe"])

    def test_detect_platform_dict(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not dict"):
            sl.detect_platform({"url": "https://linkedin.com/in/johndoe"})

    def test_is_valid_none_url(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not NoneType"):
            sl.is_valid("linkedin", None)

    def test_is_valid_none_platform(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="platform_name must be str, not NoneType"):
            sl.is_valid(None, "https://linkedin.com/in/johndoe")

    def test_is_valid_int_url(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not int"):
            sl.is_valid("linkedin", 123)

    def test_is_valid_int_platform(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="platform_name must be str, not int"):
            sl.is_valid(123, "https://linkedin.com/in/johndoe")

    def test_sanitize_none_url(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not NoneType"):
            sl.sanitize("linkedin", None)

    def test_sanitize_none_platform(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="platform_name must be str, not NoneType"):
            sl.sanitize(None, "https://linkedin.com/in/johndoe")

    def test_sanitize_int_url(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not int"):
            sl.sanitize("linkedin", 123)

    def test_sanitize_float_url(self):
        sl = SocialLinks()
        with pytest.raises(TypeError, match="url must be str, not float"):
            sl.sanitize("linkedin", 3.14)


class TestEmptyStringHandling:
    def test_detect_platform_empty_string(self):
        sl = SocialLinks()
        assert sl.detect_platform("") is None

    def test_detect_platform_whitespace_only(self):
        sl = SocialLinks()
        assert sl.detect_platform("   ") is None
        assert sl.detect_platform("\t\n") is None
        assert sl.detect_platform("  \t  \n  ") is None

    def test_is_valid_empty_string(self):
        sl = SocialLinks()
        assert sl.is_valid("linkedin", "") is False

    def test_is_valid_whitespace_only(self):
        sl = SocialLinks()
        assert sl.is_valid("linkedin", "   ") is False
        assert sl.is_valid("linkedin", "\t\n") is False

    def test_sanitize_empty_string(self):
        sl = SocialLinks()
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            sl.sanitize("linkedin", "")

    def test_sanitize_whitespace_only(self):
        sl = SocialLinks()
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            sl.sanitize("linkedin", "   ")
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            sl.sanitize("linkedin", "\t\n")

    def test_detect_platform_leading_trailing_whitespace(self):
        sl = SocialLinks()
        url = "  https://www.linkedin.com/in/johndoe/  "
        assert sl.detect_platform(url) == "linkedin"


class TestMalformedURLs:
    def test_url_with_special_characters(self):
        sl = SocialLinks()
        assert sl.detect_platform("https://example.com/@#$%^&*()") is None

    def test_url_without_protocol(self):
        sl = SocialLinks()
        assert sl.detect_platform("www.linkedin.com/in/johndoe") is None

    def test_very_long_url(self):
        sl = SocialLinks()
        long_username = "a" * 10000
        long_url = f"https://www.linkedin.com/in/{long_username}/"
        assert sl.detect_platform(long_url) == "linkedin"

    def test_url_with_unicode_characters(self):
        sl = SocialLinks()
        # LinkedIn uses PROFILE_ID_UNICODE which supports Unicode in profile IDs
        unicode_url = "https://www.linkedin.com/in/josé-garcía/"
        assert sl.detect_platform(unicode_url) == "linkedin"
        
        sanitized = sl.sanitize("linkedin", unicode_url)
        assert sanitized == "https://linkedin.com/in/josé-garcía"

    def test_url_with_query_parameters(self):
        """Query parameters (share links) are ignored when matching"""
        sl = SocialLinks()
        url = "https://www.linkedin.com/in/johndoe/?utm_source=test"
        assert sl.detect_platform(url) == "linkedin"
        assert sl.sanitize("linkedin", url) == "https://linkedin.com/in/johndoe"

        clean_url = "https://www.linkedin.com/in/johndoe/"
        assert sl.detect_platform(clean_url) == "linkedin"

    def test_url_with_fragments(self):
        """Fragments are ignored when matching"""
        sl = SocialLinks()
        url = "https://www.linkedin.com/in/johndoe/#section"
        assert sl.detect_platform(url) == "linkedin"
        assert sl.sanitize("linkedin", url) == "https://linkedin.com/in/johndoe"

        clean_url = "https://www.linkedin.com/in/johndoe/"
        assert sl.detect_platform(clean_url) == "linkedin"

    def test_multiple_slashes_in_url(self):
        sl = SocialLinks()
        # Pattern expects exact format, multiple slashes cause mismatch
        url = "https://www.linkedin.com///in///johndoe///"
        assert sl.detect_platform(url) is None
        
        clean_url = "https://www.linkedin.com/in/johndoe/"
        assert sl.detect_platform(clean_url) == "linkedin"


class TestEmptyPlatformList:
    def test_detect_platform_no_platforms(self):
        sl = SocialLinks(use_predefined_platforms=False)
        assert sl.detect_platform("https://www.linkedin.com/in/johndoe/") is None

    def test_is_valid_no_platforms(self):
        sl = SocialLinks(use_predefined_platforms=False)
        assert sl.is_valid("linkedin", "https://www.linkedin.com/in/johndoe/") is False

