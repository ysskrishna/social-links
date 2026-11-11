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
