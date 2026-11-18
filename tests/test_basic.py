import pytest
from sociallinks import detect_platform, is_valid, sanitize, extract_id, list_platforms
from sociallinks.core import SocialLinks
from sociallinks.exceptions import (
    PlatformNotFoundError,
    URLMismatchError,
)


class TestModuleLevelDetectPlatform:
    def test_detect_linkedin_personal(self):
        assert detect_platform("https://www.linkedin.com/in/johndoe/") == "linkedin"
        assert detect_platform("http://linkedin.com/in/johndoe") == "linkedin"
        assert detect_platform("https://linkedin.com/in/jane-smith") == "linkedin"

    def test_detect_linkedin_company(self):
        assert detect_platform("https://www.linkedin.com/company/acme/") == "linkedin"
        assert detect_platform("http://linkedin.com/company/techcorp") == "linkedin"

    def test_detect_facebook(self):
        assert detect_platform("https://www.facebook.com/johndoe/") == "facebook"
        assert detect_platform("http://facebook.com/janedoe") == "facebook"

    def test_detect_github(self):
        assert detect_platform("https://github.com/username") == "github"
        assert detect_platform("https://www.github.com/username") == "github"

    def test_detect_x(self):
        assert detect_platform("https://x.com/username") == "x"
        assert detect_platform("https://twitter.com/username") == "x"

    def test_detect_instagram(self):
        assert detect_platform("https://instagram.com/username") == "instagram"
        assert detect_platform("https://www.instagram.com/username") == "instagram"

    def test_detect_youtube(self):
        assert detect_platform("https://youtube.com/@username") == "youtube"
        assert detect_platform("https://www.youtube.com/@username") == "youtube"

    def test_detect_none_for_invalid_url(self):
        assert detect_platform("https://example.com") is None
        assert detect_platform("not a url") is None
        assert detect_platform("") is None

    def test_detect_platform_type_error_none(self):
        with pytest.raises(TypeError, match="url must be str, not NoneType"):
            detect_platform(None)

    def test_detect_platform_type_error_int(self):
        with pytest.raises(TypeError, match="url must be str, not int"):
            detect_platform(123)

    def test_detect_platform_type_error_list(self):
        with pytest.raises(TypeError, match="url must be str, not list"):
            detect_platform(["https://linkedin.com/in/johndoe"])

    def test_detect_platform_type_error_dict(self):
        with pytest.raises(TypeError, match="url must be str, not dict"):
            detect_platform({"url": "https://linkedin.com/in/johndoe"})

    def test_detect_platform_whitespace_handling(self):
        url = "  https://www.linkedin.com/in/johndoe/  "
        assert detect_platform(url) == "linkedin"
        assert detect_platform("   ") is None
        assert detect_platform("\t\n") is None

    def test_detect_platform_empty_string(self):
        assert detect_platform("") is None

    def test_detect_platform_case_insensitive(self):
        assert detect_platform("HTTPS://WWW.LINKEDIN.COM/IN/JOHNDOE/") == "linkedin"
        assert detect_platform("https://GITHUB.COM/USERNAME") == "github"


class TestModuleLevelIsValid:
    def test_is_valid_linkedin_personal(self):
        assert is_valid("linkedin", "https://www.linkedin.com/in/johndoe/") is True
        assert is_valid("linkedin", "http://linkedin.com/in/jane-smith") is True
        assert is_valid("linkedin", "https://example.com") is False

    def test_is_valid_linkedin_company(self):
        assert is_valid("linkedin", "https://www.linkedin.com/company/acme/") is True
        assert is_valid("linkedin", "http://linkedin.com/company/techcorp") is True

    def test_is_valid_facebook(self):
        assert is_valid("facebook", "https://www.facebook.com/johndoe/") is True
        assert is_valid("facebook", "http://facebook.com/janedoe") is True
        assert is_valid("facebook", "https://example.com") is False

    def test_is_valid_github(self):
        assert is_valid("github", "https://github.com/username") is True
        assert is_valid("github", "https://example.com") is False

    def test_is_valid_x(self):
        assert is_valid("x", "https://x.com/username") is True
        assert is_valid("x", "https://twitter.com/username") is True
        assert is_valid("x", "https://example.com") is False

    def test_is_valid_unknown_platform(self):
        assert is_valid("unknown", "https://www.linkedin.com/in/johndoe/") is False
        assert is_valid("nonexistent", "https://github.com/username") is False

    def test_is_valid_type_error_none_url(self):
        with pytest.raises(TypeError, match="url must be str, not NoneType"):
            is_valid("linkedin", None)

    def test_is_valid_type_error_none_platform(self):
        with pytest.raises(TypeError, match="platform_name must be str, not NoneType"):
            is_valid(None, "https://linkedin.com/in/johndoe")

    def test_is_valid_type_error_int_url(self):
        with pytest.raises(TypeError, match="url must be str, not int"):
            is_valid("linkedin", 123)

    def test_is_valid_type_error_int_platform(self):
        with pytest.raises(TypeError, match="platform_name must be str, not int"):
            is_valid(123, "https://linkedin.com/in/johndoe")

    def test_is_valid_empty_string(self):
        assert is_valid("linkedin", "") is False

    def test_is_valid_whitespace_only(self):
        assert is_valid("linkedin", "   ") is False
        assert is_valid("linkedin", "\t\n") is False

    def test_is_valid_whitespace_handling(self):
        url = "  https://www.linkedin.com/in/johndoe/  "
        assert is_valid("linkedin", url) is True

    def test_is_valid_case_insensitive(self):
        assert is_valid("linkedin", "HTTPS://WWW.LINKEDIN.COM/IN/JOHNDOE/") is True
        assert is_valid("github", "https://GITHUB.COM/USERNAME") is True


class TestModuleLevelSanitize:
    def test_sanitize_linkedin_personal(self):
        result = sanitize("linkedin", "https://www.linkedin.com/in/johndoe/")
        assert result == "https://linkedin.com/in/johndoe"
        
        result = sanitize("linkedin", "http://linkedin.com/in/jane-smith")
        assert result == "https://linkedin.com/in/jane-smith"

    def test_sanitize_linkedin_company(self):
        result = sanitize("linkedin", "https://www.linkedin.com/company/acme/")
        assert result == "https://linkedin.com/company/acme"
        
        result = sanitize("linkedin", "http://linkedin.com/company/techcorp")
        assert result == "https://linkedin.com/company/techcorp"

    def test_sanitize_facebook(self):
        result = sanitize("facebook", "https://www.facebook.com/johndoe/")
        assert result == "https://facebook.com/johndoe"
        
        result = sanitize("facebook", "http://facebook.com/janedoe")
        assert result == "https://facebook.com/janedoe"

    def test_sanitize_github(self):
        result = sanitize("github", "http://www.github.com/username")
        assert result == "https://github.com/username"
        
        result = sanitize("github", "https://github.com/username")
        assert result == "https://github.com/username"

    def test_sanitize_x(self):
        result = sanitize("x", "https://twitter.com/username")
        assert result == "https://x.com/username"
        
        result = sanitize("x", "https://mobile.twitter.com/username")
        assert result == "https://x.com/username"

    def test_sanitize_platform_not_found(self):
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            sanitize("unknown", "https://linkedin.com/in/johndoe")
        
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            sanitize("nonexistent", "https://github.com/username")

    def test_sanitize_url_mismatch(self):
        with pytest.raises(URLMismatchError, match="does not match platform"):
            sanitize("linkedin", "https://example.com")
        
        with pytest.raises(URLMismatchError, match="does not match platform"):
            sanitize("github", "https://example.com")

    def test_sanitize_type_error_none_url(self):
        with pytest.raises(TypeError, match="url must be str, not NoneType"):
            sanitize("linkedin", None)

    def test_sanitize_type_error_none_platform(self):
        with pytest.raises(TypeError, match="platform_name must be str, not NoneType"):
            sanitize(None, "https://linkedin.com/in/johndoe")

    def test_sanitize_type_error_int_url(self):
        with pytest.raises(TypeError, match="url must be str, not int"):
            sanitize("linkedin", 123)

    def test_sanitize_type_error_float_url(self):
        with pytest.raises(TypeError, match="url must be str, not float"):
            sanitize("linkedin", 3.14)

    def test_sanitize_empty_string(self):
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            sanitize("linkedin", "")

    def test_sanitize_whitespace_only(self):
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            sanitize("linkedin", "   ")
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            sanitize("linkedin", "\t\n")

    def test_sanitize_whitespace_handling(self):
        url = "  https://www.linkedin.com/in/johndoe/  "
        result = sanitize("linkedin", url)
        assert result == "https://linkedin.com/in/johndoe"

    def test_sanitize_unicode_characters(self):
        unicode_url = "https://www.linkedin.com/in/josé-garcía/"
        result = sanitize("linkedin", unicode_url)
        assert result == "https://linkedin.com/in/josé-garcía"


class TestModuleLevelListPlatforms:
    def test_list_platforms_returns_list(self):
        platforms = list_platforms()
        assert isinstance(platforms, list)

    def test_list_platforms_non_empty(self):
        platforms = list_platforms()
        assert len(platforms) > 0
        assert len(platforms) >= 50  # Should have 50+ predefined platforms

    def test_list_platforms_matches_class_method(self):
        module_result = set(list_platforms())
        class_result = set(SocialLinks().list_platforms())
        assert module_result == class_result


class TestModuleLevelExtractId:
    def test_extract_id_linkedin(self):
        assert extract_id("linkedin", "https://www.linkedin.com/in/johndoe/") == "johndoe"
        assert extract_id("linkedin", "http://linkedin.com/in/jane-smith") == "jane-smith"

    def test_extract_id_github(self):
        assert extract_id("github", "https://github.com/username") == "username"
        assert extract_id("github", "http://www.github.com/user123") == "user123"

    def test_extract_id_x(self):
        assert extract_id("x", "https://x.com/elonmusk") == "elonmusk"
        assert extract_id("x", "https://twitter.com/username") == "username"

    def test_extract_id_facebook(self):
        assert extract_id("facebook", "https://www.facebook.com/johndoe/") == "johndoe"
        assert extract_id("facebook", "http://facebook.com/janedoe") == "janedoe"

    def test_extract_id_platform_not_found(self):
        with pytest.raises(PlatformNotFoundError, match="Unknown platform"):
            extract_id("unknown", "https://example.com/user")

    def test_extract_id_url_mismatch(self):
        with pytest.raises(URLMismatchError, match="does not match platform"):
            extract_id("linkedin", "https://example.com")

    def test_extract_id_type_error_none_url(self):
        with pytest.raises(TypeError, match="url must be str, not NoneType"):
            extract_id("linkedin", None)

    def test_extract_id_type_error_none_platform(self):
        with pytest.raises(TypeError, match="platform_name must be str, not NoneType"):
            extract_id(None, "https://linkedin.com/in/johndoe")

    def test_extract_id_empty_string(self):
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            extract_id("linkedin", "")

    def test_extract_id_whitespace_only(self):
        with pytest.raises(URLMismatchError, match="URL cannot be empty"):
            extract_id("linkedin", "   ")

    def test_extract_id_unicode_characters(self):
        result = extract_id("linkedin", "https://www.linkedin.com/in/josé-garcía/")
        assert result == "josé-garcía"
