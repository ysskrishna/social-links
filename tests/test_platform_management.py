import pytest
from sociallinks.core import SocialLinks
from sociallinks.exceptions import (
    PlatformNotFoundError,
    PlatformAlreadyExistsError,
    InvalidPlatformError,
    InvalidPlatformRegexError,
)


class TestSetPlatform:
    def test_set_platform_new(self):
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = [{
            "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.twitter.com/{id}/"
        }]
        sl.set_platform("twitter", platform_data)
        assert "twitter" in sl.platforms
        assert sl.detect_platform("https://www.twitter.com/johndoe") == "twitter"

    def test_set_platform_override_false(self):
        sl = SocialLinks()
        platform_data = [{
            "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.twitter.com/{id}/"
        }]
        with pytest.raises(PlatformAlreadyExistsError, match="already exists"):
            sl.set_platform("linkedin", platform_data)

    def test_set_platform_override_true(self):
        sl = SocialLinks()
        platform_data = [{
            "patterns": ["https?://(www\\.)?linkedin\\.com/custom/(?P<id>[A-Za-z0-9_]+)/?$"],
            "sanitized": "https://www.linkedin.com/custom/{id}/"
        }]
        sl.set_platform("linkedin", platform_data, override=True)
        assert sl.detect_platform("https://www.linkedin.com/custom/johndoe") == "linkedin"
        assert sl.detect_platform("https://www.linkedin.com/in/johndoe") is None

    def test_set_platform_with_list(self):
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
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = [{
            "patterns": [],
            "sanitized": "https://www.example.com/{id}/"
        }]
        with pytest.raises(InvalidPlatformError, match="no valid patterns"):
            sl.set_platform("example", platform_data)

    def test_set_platform_missing_sanitized(self):
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = [{
            "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"]
        }]
        with pytest.raises(InvalidPlatformError, match="no valid patterns"):
            sl.set_platform("example", platform_data)

    def test_set_platform_invalid_regex_pattern(self):
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = [{
            "patterns": ["[invalid regex["],  # Unclosed bracket
            "sanitized": "https://www.example.com/{id}/"
        }]
        with pytest.raises(InvalidPlatformRegexError, match="Invalid regex pattern"):
            sl.set_platform("example", platform_data)

    def test_set_platform_invalid_regex_pattern_with_platform_name(self):
        sl = SocialLinks(use_predefined_platforms=False)
        platform_data = [{
            "patterns": ["(unclosed group"],  # Unclosed parenthesis
            "sanitized": "https://www.example.com/{id}/"
        }]
        with pytest.raises(InvalidPlatformRegexError, match="platform 'test_platform'"):
            sl.set_platform("test_platform", platform_data)


class TestDeletePlatform:
    def test_delete_platform(self):
        sl = SocialLinks()
        assert "linkedin" in sl.platforms
        sl.delete_platform("linkedin")
        assert "linkedin" not in sl.platforms
        assert "linkedin" not in sl._compiled

    def test_delete_platform_not_found(self):
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="not found"):
            sl.delete_platform("nonexistent")


class TestSetPlatforms:
    def test_set_platforms_new(self):
        sl = SocialLinks(use_predefined_platforms=False)
        platforms = {
            "twitter": [{
                "patterns": ["https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.twitter.com/{id}/"
            }],
            "instagram": [{
                "patterns": ["https?://(www\\.)?instagram\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://www.instagram.com/{id}/"
            }]
        }
        sl.set_platforms(platforms)
        assert "twitter" in sl.platforms
        assert "instagram" in sl.platforms

    def test_set_platforms_with_conflicts(self):
        sl = SocialLinks()
        platforms = {
            "linkedin": [{
                "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://example.com/{id}/"
            }]
        }
        with pytest.raises(PlatformAlreadyExistsError, match="already exist"):
            sl.set_platforms(platforms)

    def test_set_platforms_override(self):
        sl = SocialLinks()
        platforms = {
            "linkedin": [{
                "patterns": ["https?://example\\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
                "sanitized": "https://example.com/{id}/"
            }]
        }
        sl.set_platforms(platforms, override=True)
        assert sl.detect_platform("https://example.com/johndoe") == "linkedin"


class TestDeletePlatforms:
    def test_delete_platforms(self):
        sl = SocialLinks()
        assert "linkedin" in sl.platforms
        assert "facebook" in sl.platforms
        sl.delete_platforms(["linkedin", "facebook"])
        assert "linkedin" not in sl.platforms
        assert "facebook" not in sl.platforms

    def test_delete_platforms_missing(self):
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="not found"):
            sl.delete_platforms(["linkedin", "nonexistent"])


class TestClearPlatforms:
    def test_clear_platforms(self):
        sl = SocialLinks()
        assert len(sl.platforms) > 0
        sl.clear_platforms()
        assert len(sl.platforms) == 0
        assert len(sl._compiled) == 0


class TestGetPlatform:
    def test_get_platform(self):
        sl = SocialLinks()
        platform = sl.get_platform("linkedin")
        assert platform is not None
        assert isinstance(platform, list)

    def test_get_platform_not_found(self):
        sl = SocialLinks()
        with pytest.raises(PlatformNotFoundError, match="not found"):
            sl.get_platform("nonexistent")


class TestListPlatforms:
    def test_list_platforms(self):
        sl = SocialLinks()
        platforms = sl.list_platforms()
        assert isinstance(platforms, list)
        assert len(platforms) >= 25
        assert "linkedin" in platforms
        assert "facebook" in platforms
        assert "github" in platforms
        assert "instagram" in platforms
        assert "youtube" in platforms
        assert "x" in platforms
        assert "behance" in platforms
        assert "dev_to" in platforms

    def test_list_platforms_empty(self):
        sl = SocialLinks(use_predefined_platforms=False)
        platforms = sl.list_platforms()
        assert platforms == []

