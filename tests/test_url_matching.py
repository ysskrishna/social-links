"""Tests for URL matching semantics.

Covers three behaviours:
  A. Patterns are anchored at the start of the input (no embedded URLs).
  B. ``detect_platform`` ignores bare-ID patterns (``johndoe`` is not a platform).
  C. Query strings and fragments are tolerated (share links), while platforms
     that need them in the URL (e.g. Hacker News ``?id=``) keep working.
"""
import pytest

from sociallinks import SocialLinks
from sociallinks.constants import PROFILE_ID
from sociallinks.exceptions import URLMismatchError


@pytest.fixture
def sl():
    return SocialLinks()


class TestLeftAnchor:
    """A. A URL embedded in a longer string must not match."""

    @pytest.mark.parametrize(
        "url",
        [
            "https://evil.com/?r=https://github.com/foo",
            "xhttps://github.com/foo",
            "see https://github.com/foo",
            "my profile: https://github.com/foo",
            "https://notgithub.com/foo",
        ],
    )
    def test_embedded_or_prefixed_url_is_invalid(self, sl, url):
        assert sl.is_valid("github", url) is False
        assert sl.detect_platform(url) is None
        with pytest.raises(URLMismatchError):
            sl.sanitize("github", url)
        with pytest.raises(URLMismatchError):
            sl.extract_id("github", url)

    def test_plain_urls_still_match(self, sl):
        assert sl.is_valid("github", "https://github.com/foo") is True
        assert sl.is_valid("github", "http://www.github.com/foo/") is True
        assert sl.detect_platform("  https://github.com/foo  ") == "github"


class TestBareIdDetection:
    """B. detect_platform must not guess a platform from a bare ID."""

    @pytest.mark.parametrize("value", ["johndoe", "ysskrishna", "abc", "12345", "@foo", "john.doe"])
    def test_bare_values_are_not_detected(self, sl, value):
        assert sl.detect_platform(value) is None

    @pytest.mark.parametrize(
        "value,platform",
        [
            ("u/foo", "reddit"),
            ("r/python", "reddit"),
            ("spotify:artist:4r7sp4bvfy", "spotify"),
            ("weixin://dl/chat?foo", "wechat"),
        ],
    )
    def test_prefixed_shorthands_are_still_detected(self, sl, value, platform):
        assert sl.detect_platform(value) == platform

    def test_explicit_platform_still_accepts_bare_ids(self, sl):
        assert sl.is_valid("github", "ysskrishna") is True
        assert sl.sanitize("github", "ysskrishna") == "https://github.com/ysskrishna"
        assert sl.extract_id("github", "ysskrishna") == "ysskrishna"
        assert sl.sanitize("x", "@foo") == "https://x.com/foo"

    def test_custom_bare_pattern_built_from_library_constant_is_not_detected(self):
        sl = SocialLinks(use_predefined_platforms=False)
        sl.set_platform(
            "demo",
            [{
                "patterns": [rf"https?://demo\.com/{PROFILE_ID}/?$", rf"^{PROFILE_ID}$"],
                "sanitized": "https://demo.com/{id}",
            }],
        )
        assert sl.detect_platform("https://demo.com/foo") == "demo"
        assert sl.detect_platform("foo") is None
        assert sl.sanitize("demo", "foo") == "https://demo.com/foo"
