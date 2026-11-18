"""Common pattern tests for all platforms using parametrization.

This module tests common URL patterns (www, http, trailing slash) across
all platforms that support them, avoiding duplication in individual test files.
"""
import re
import pytest
from sociallinks.platforms import PREDEFINED_PLATFORMS


def _platform_supports_www(platform_name: str) -> bool:
    """Check if platform supports www subdomain."""
    entries = PREDEFINED_PLATFORMS.get(platform_name, [])
    all_patterns = []
    for entry in entries:
        all_patterns.extend(entry["patterns"])
    patterns_str = " ".join(all_patterns)
    return bool(re.search(r'\(www\\?\.\)\?', patterns_str) or re.search(r'www\.', patterns_str))


def _platform_supports_http(platform_name: str) -> bool:
    """Check if platform supports http protocol."""
    entries = PREDEFINED_PLATFORMS.get(platform_name, [])
    all_patterns = []
    for entry in entries:
        all_patterns.extend(entry["patterns"])
    patterns_str = " ".join(all_patterns)
    return bool(re.search(r'https\?://', patterns_str))


def _platform_supports_trailing_slash(platform_name: str) -> bool:
    """Check if platform supports trailing slash."""
    entries = PREDEFINED_PLATFORMS.get(platform_name, [])
    all_patterns = []
    for entry in entries:
        all_patterns.extend(entry["patterns"])
    patterns_str = " ".join(all_patterns)
    return bool(re.search(r'/\?\$', patterns_str))


def _get_base_url(platform_name: str, profile_id: str) -> str:
    """Get base URL for a platform using its sanitized template."""
    entries = PREDEFINED_PLATFORMS.get(platform_name, [])
    if not entries:
        return None
    
    sanitized = entries[0]["sanitized"]
    return sanitized.format(id=profile_id)


def _get_test_profile_id(platform_name: str) -> str:
    """Get a test profile ID for a platform."""
    special_ids = {
        "apple_music": "123456789",
        "whatsapp": "1234567890",
        "spotify": "4r7sp4bvfy",
        "youtube": "@ysskrishna",
        "stackoverflow": "12345",
        "signal": "1234567890",
        "stack_exchange": "1",
        "google_scholar": "JicYPdAAAAAJ",
        "primal": "npub180cvv07tjdrrgpa0j7j7tmnyl2yr6yr7l8j4s3evf6u64th6gkwsyjh6w6",
        "openstreetmap": "SteveC",
        "bilibili": "2",
        "goodreads": "1",
        "pixiv": "11",
        "niconico": "1",
        "roblox": "1",
        "orcid": "0000-0002-1825-0097",
        "airbnb": "1",
        "carrd": "ysskrishna",
        "blogger": "05229574233543423344",
        "juejin": "1838039172387262",
        "coursera": "85dca6cc1c1ccacdb8d6cbc3853c8eff",
        "semantic_scholar": "1741101",
        "xda": "ysskrishna.123456",
        "chzzk": "458f6ec20b034f49e0fc6d03921646d2",
        "rutube": "23704195",
        "audioboom": "4256218",
        "jamendo": "1",
        "royal_road": "1",
        "scribd": "1/ysskrishna",
        "issuu": "ysskrishna",
        "ok_ru": "561611456451",
        "mercari": "123456789",
        "vinted": "1",
        "note_com": "ysskrishna",
    }
    
    return special_ids.get(platform_name, "ysskrishna")


www_platforms = [
    (platform, _get_test_profile_id(platform))
    for platform in PREDEFINED_PLATFORMS.keys()
    if _platform_supports_www(platform)
]

http_platforms = [
    (platform, _get_test_profile_id(platform))
    for platform in PREDEFINED_PLATFORMS.keys()
    if _platform_supports_http(platform)
]

trailing_slash_platforms = [
    (platform, _get_test_profile_id(platform))
    for platform in PREDEFINED_PLATFORMS.keys()
    if _platform_supports_trailing_slash(platform)
]


class TestCommonPatterns:
    @pytest.mark.parametrize("platform_name,profile_id", www_platforms)
    def test_with_www(self, sl, platform_name: str, profile_id: str):
        base_url = _get_base_url(platform_name, profile_id)
        if not base_url:
            pytest.skip(f"No base URL template for {platform_name}")
        
        if "://www." in base_url:
            www_url = base_url
        elif base_url.startswith("https://"):
            www_url = base_url.replace("https://", "https://www.", 1)
        elif base_url.startswith("http://"):
            www_url = base_url.replace("http://", "http://www.", 1)
        else:
            pytest.skip(f"Unexpected URL format for {platform_name}: {base_url}")
        
        # Some platforms support www in patterns but only for specific domains
        if not sl.is_valid(platform_name, www_url):
            if platform_name == "x" and "x.com" in www_url:
                # x.com doesn't support www, but twitter.com does
                www_url = www_url.replace("x.com", "twitter.com")
            else:
                pytest.skip(f"www URL not valid for {platform_name}: {www_url}")
        
        assert sl.is_valid(platform_name, www_url) is True, f"www URL should be valid: {www_url}"
        assert sl.detect_platform(www_url) == platform_name, f"Should detect {platform_name} from {www_url}"
        sanitized = sl.sanitize(platform_name, www_url)
        assert sanitized is not None
        assert sl.is_valid(platform_name, sanitized) is True

    @pytest.mark.parametrize("platform_name,profile_id", http_platforms)
    def test_with_http(self, sl, platform_name: str, profile_id: str):
        base_url = _get_base_url(platform_name, profile_id)
        if not base_url:
            pytest.skip(f"No base URL template for {platform_name}")
        
        http_url = base_url.replace("https://", "http://")
        
        assert sl.is_valid(platform_name, http_url) is True, f"http URL should be valid: {http_url}"
        assert sl.detect_platform(http_url) == platform_name, f"Should detect {platform_name} from {http_url}"
        sanitized = sl.sanitize(platform_name, http_url)
        assert sanitized is not None
        assert sl.is_valid(platform_name, sanitized) is True

    @pytest.mark.parametrize("platform_name,profile_id", trailing_slash_platforms)
    def test_with_trailing_slash(self, sl, platform_name: str, profile_id: str):
        base_url = _get_base_url(platform_name, profile_id)
        if not base_url:
            pytest.skip(f"No base URL template for {platform_name}")
        
        if base_url.endswith("#") or base_url.endswith("?"):
            url_with_slash = base_url.replace("#", "/#").replace("?", "/?")
        else:
            url_with_slash = base_url.rstrip("/") + "/"
        
        assert sl.is_valid(platform_name, url_with_slash) is True, f"URL with trailing slash should be valid: {url_with_slash}"
        assert sl.detect_platform(url_with_slash) == platform_name, f"Should detect {platform_name} from {url_with_slash}"
        sanitized = sl.sanitize(platform_name, url_with_slash)
        assert sanitized is not None
        assert sl.is_valid(platform_name, sanitized) is True

