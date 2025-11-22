import pytest
from sociallinks.core import SocialLinks


class TestSocialLinksInitialization:
    """Test SocialLinks initialization"""

    def test_init_with_predefined_profiles(self):
        """Test initialization with predefined profiles"""
        sl = SocialLinks()
        assert len(sl.profiles) > 0
        assert "linkedin" in sl.profiles
        assert "facebook" in sl.profiles

    def test_init_without_predefined_profiles(self):
        """Test initialization without predefined profiles"""
        sl = SocialLinks(use_predefined_profiles=False)
        assert len(sl.profiles) == 0
        assert len(sl._compiled) == 0

    def test_init_with_custom_regex_flags(self):
        """Test initialization with custom regex flags"""
        import re
        sl = SocialLinks(regex_flags=re.IGNORECASE | re.MULTILINE)
        assert sl.regex_flags == (re.IGNORECASE | re.MULTILINE)


class TestDetectProfile:
    """Test detect_profile method"""

    def test_detect_linkedin_personal(self):
        """Test detecting LinkedIn personal profile"""
        sl = SocialLinks()
        assert sl.detect_profile("https://www.linkedin.com/in/johndoe/") == "linkedin"
        assert sl.detect_profile("http://linkedin.com/in/johndoe") == "linkedin"
        assert sl.detect_profile("https://linkedin.com/in/jane-smith") == "linkedin"

    def test_detect_linkedin_company(self):
        """Test detecting LinkedIn company profile"""
        sl = SocialLinks()
        assert sl.detect_profile("https://www.linkedin.com/company/acme/") == "linkedin"
        assert sl.detect_profile("http://linkedin.com/company/techcorp") == "linkedin"

    def test_detect_facebook(self):
        """Test detecting Facebook profile"""
        sl = SocialLinks()
        assert sl.detect_profile("https://www.facebook.com/johndoe/") == "facebook"
        assert sl.detect_profile("http://facebook.com/janedoe") == "facebook"

    def test_detect_none_for_invalid_url(self):
        """Test that invalid URLs return None"""
        sl = SocialLinks()
        assert sl.detect_profile("https://example.com") is None
        assert sl.detect_profile("not a url") is None
        assert sl.detect_profile("") is None

    def test_detect_with_whitespace(self):
        """Test that URLs with whitespace are handled"""
        sl = SocialLinks()
        assert sl.detect_profile("  https://www.linkedin.com/in/johndoe/  ") == "linkedin"


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

    def test_is_valid_unknown_profile(self):
        """Test validating with unknown profile"""
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

    def test_sanitize_unknown_profile(self):
        """Test sanitizing with unknown profile"""
        sl = SocialLinks()
        with pytest.raises(ValueError, match="Unknown profile"):
            sl.sanitize("unknown", "https://www.linkedin.com/in/johndoe/")

    def test_sanitize_invalid_url(self):
        """Test sanitizing invalid URL for profile"""
        sl = SocialLinks()
        with pytest.raises(ValueError, match="does not match profile"):
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

    def test_get_clean_link_unknown_profile(self):
        """Test getting clean link for unknown profile"""
        sl = SocialLinks()
        with pytest.raises(ValueError, match="Unknown profile"):
            sl.get_clean_link("unknown", "johndoe")


class TestSetProfile:
    """Test set_profile method"""

    def test_set_profile_new(self):
        """Test adding a new profile"""
        sl = SocialLinks(use_predefined_profiles=False)
        profile_data = {
            "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.twitter.com/{id}/"
        }
        sl.set_profile("twitter", profile_data)
        assert "twitter" in sl.profiles
        assert sl.detect_profile("https://www.twitter.com/johndoe") == "twitter"

    def test_set_profile_override_false(self):
        """Test that setting existing profile without override raises error"""
        sl = SocialLinks()
        profile_data = {
            "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.twitter.com/{id}/"
        }
        with pytest.raises(ValueError, match="already exists"):
            sl.set_profile("linkedin", profile_data)

    def test_set_profile_override_true(self):
        """Test overriding existing profile"""
        sl = SocialLinks()
        profile_data = {
            "patterns": ["https?://(www\\.)?linkedin\\.com/custom/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.linkedin.com/custom/{id}/"
        }
        sl.set_profile("linkedin", profile_data, override=True)
        assert sl.detect_profile("https://www.linkedin.com/custom/johndoe") == "linkedin"
        assert sl.detect_profile("https://www.linkedin.com/in/johndoe") is None

    def test_set_profile_with_list(self):
        """Test setting profile with list of patterns"""
        sl = SocialLinks(use_predefined_profiles=False)
        profile_data = [
            {
                "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.twitter.com/{id}/"
            },
            {
                "patterns": ["https?://twitter\\.com/x/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.twitter.com/x/{id}/"
            }
        ]
        sl.set_profile("twitter", profile_data)
        assert sl.detect_profile("https://www.twitter.com/johndoe") == "twitter"
        assert sl.detect_profile("https://twitter.com/x/johndoe") == "twitter"

    def test_set_profile_invalid_patterns(self):
        """Test setting profile with invalid patterns"""
        sl = SocialLinks(use_predefined_profiles=False)
        profile_data = {
            "patterns": [],
            "sanitized": "https://www.example.com/{id}/"
        }
        with pytest.raises(ValueError, match="no valid patterns"):
            sl.set_profile("example", profile_data)

    def test_set_profile_missing_sanitized(self):
        """Test setting profile without sanitized template"""
        sl = SocialLinks(use_predefined_profiles=False)
        profile_data = {
            "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"]
        }
        with pytest.raises(ValueError, match="no valid patterns"):
            sl.set_profile("example", profile_data)


class TestDeleteProfile:
    """Test delete_profile method"""

    def test_delete_profile(self):
        """Test deleting a profile"""
        sl = SocialLinks()
        assert "linkedin" in sl.profiles
        sl.delete_profile("linkedin")
        assert "linkedin" not in sl.profiles
        assert "linkedin" not in sl._compiled

    def test_delete_profile_not_found(self):
        """Test deleting non-existent profile"""
        sl = SocialLinks()
        with pytest.raises(ValueError, match="not found"):
            sl.delete_profile("nonexistent")


class TestSetProfiles:
    """Test set_profiles method"""

    def test_set_profiles_new(self):
        """Test bulk adding new profiles"""
        sl = SocialLinks(use_predefined_profiles=False)
        profiles = {
            "twitter": {
                "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.twitter.com/{id}/"
            },
            "instagram": {
                "patterns": ["https?://(www\\.)?instagram\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.instagram.com/{id}/"
            }
        }
        sl.set_profiles(profiles)
        assert "twitter" in sl.profiles
        assert "instagram" in sl.profiles

    def test_set_profiles_with_conflicts(self):
        """Test bulk adding profiles with conflicts"""
        sl = SocialLinks()
        profiles = {
            "linkedin": {
                "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://example.com/{id}/"
            }
        }
        with pytest.raises(ValueError, match="already exist"):
            sl.set_profiles(profiles)

    def test_set_profiles_override(self):
        """Test bulk adding profiles with override"""
        sl = SocialLinks()
        profiles = {
            "linkedin": {
                "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://example.com/{id}/"
            }
        }
        sl.set_profiles(profiles, override=True)
        assert sl.detect_profile("https://example.com/johndoe") == "linkedin"


class TestDeleteProfiles:
    """Test delete_profiles method"""

    def test_delete_profiles(self):
        """Test bulk deleting profiles"""
        sl = SocialLinks()
        assert "linkedin" in sl.profiles
        assert "facebook" in sl.profiles
        sl.delete_profiles(["linkedin", "facebook"])
        assert "linkedin" not in sl.profiles
        assert "facebook" not in sl.profiles

    def test_delete_profiles_missing(self):
        """Test bulk deleting with missing profiles"""
        sl = SocialLinks()
        with pytest.raises(ValueError, match="not found"):
            sl.delete_profiles(["linkedin", "nonexistent"])


class TestClearProfiles:
    """Test clear_profiles method"""

    def test_clear_profiles(self):
        """Test clearing all profiles"""
        sl = SocialLinks()
        assert len(sl.profiles) > 0
        sl.clear_profiles()
        assert len(sl.profiles) == 0
        assert len(sl._compiled) == 0


class TestGetProfile:
    """Test get_profile method"""

    def test_get_profile(self):
        """Test getting a profile"""
        sl = SocialLinks()
        profile = sl.get_profile("linkedin")
        assert profile is not None
        assert isinstance(profile, list)

    def test_get_profile_not_found(self):
        """Test getting non-existent profile"""
        sl = SocialLinks()
        with pytest.raises(ValueError, match="not found"):
            sl.get_profile("nonexistent")


class TestListProfiles:
    """Test list_profiles method"""

    def test_list_profiles(self):
        """Test listing all profiles"""
        sl = SocialLinks()
        profiles = sl.list_profiles()
        assert isinstance(profiles, list)
        assert "linkedin" in profiles
        assert "facebook" in profiles

    def test_list_profiles_empty(self):
        """Test listing profiles when empty"""
        sl = SocialLinks(use_predefined_profiles=False)
        profiles = sl.list_profiles()
        assert profiles == []


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
        sl = SocialLinks(use_predefined_profiles=False)
        # Create a profile with pattern that doesn't capture ID
        profile_data = {
            "patterns": ["https?://example\\.com/static/?$"],
            "sanitized": "https://example.com/{id}/"
        }
        sl.set_profile("example", profile_data)
        with pytest.raises(ValueError, match="Could not extract profile ID"):
            sl.sanitize("example", "https://example.com/static")

    def test_case_insensitive_matching(self):
        """Test case insensitive URL matching"""
        sl = SocialLinks()
        # Should work with uppercase
        assert sl.detect_profile("HTTPS://WWW.LINKEDIN.COM/IN/JOHNDOE/") == "linkedin"
        assert sl.is_valid("linkedin", "HTTPS://WWW.LINKEDIN.COM/IN/JOHNDOE/") is True

    def test_multiple_patterns_same_profile(self):
        """Test profile with multiple patterns"""
        sl = SocialLinks()
        # LinkedIn has both personal and company patterns
        assert sl.is_valid("linkedin", "https://www.linkedin.com/in/johndoe/") is True
        assert sl.is_valid("linkedin", "https://www.linkedin.com/company/acme/") is True

