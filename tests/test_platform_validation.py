"""Tests for platform validation and atomic registration."""
import pytest

from sociallinks import SocialLinks
from sociallinks.exceptions import (
    InvalidPlatformError,
    InvalidPlatformRegexError,
    PlatformAlreadyExistsError,
    PlatformIDExtractionError,
    URLMismatchError,
)

GOOD = [{"patterns": [r"https?://example\.com/(?P<id>\w+)$"], "sanitized": "https://example.com/{id}"}]


@pytest.fixture
def empty():
    return SocialLinks(use_predefined_platforms=False)


class TestTemplateValidation:
    @pytest.mark.parametrize(
        "template",
        ["https://example.com/no-placeholder", "https://example.com/{name}", "https://example.com/{id}/{other}", "https://example.com/{}"],
    )
    def test_template_must_use_id_only(self, empty, template):
        data = [{"patterns": [r"https?://example\.com/(?P<id>\w+)$"], "sanitized": template}]
        with pytest.raises(InvalidPlatformError, match="platform 'demo'|Platform 'demo'"):
            empty.set_platform("demo", data)
        assert "demo" not in empty.platforms

    def test_malformed_template(self, empty):
        data = [{"patterns": [r"(?P<id>\w+)"], "sanitized": "https://example.com/{id"}]
        with pytest.raises(InvalidPlatformError, match="invalid 'sanitized' template"):
            empty.set_platform("demo", data)

    def test_template_with_format_spec_and_literal_braces_is_fine(self, empty):
        data = [{"patterns": [r"https?://example\.com/(?P<id>\w+)$"], "sanitized": "https://example.com/{id}?x={{1}}"}]
        empty.set_platform("demo", data)
        assert empty.sanitize("demo", "https://example.com/bob") == "https://example.com/bob?x={1}"

    def test_non_string_template(self, empty):
        data = [{"patterns": [r"(?P<id>\w+)"], "sanitized": 5}]
        with pytest.raises(InvalidPlatformError, match="no valid patterns or templates"):
            empty.set_platform("demo", data)


class TestEntryValidation:
    @pytest.mark.parametrize("entry", ["junk", 5, None, ["x"]])
    def test_non_dict_entry_raises(self, empty, entry):
        with pytest.raises(InvalidPlatformError, match="expected a dict"):
            empty.set_platform("demo", GOOD + [entry])

    @pytest.mark.parametrize("data", ["junk", {"patterns": ["x"], "sanitized": "{id}"}, [], None])
    def test_data_must_be_non_empty_list(self, empty, data):
        with pytest.raises(InvalidPlatformError, match="non-empty list"):
            empty.set_platform("demo", data)

    def test_incomplete_entry_next_to_a_valid_one_is_not_silently_skipped(self, empty):
        with pytest.raises(InvalidPlatformError, match="entry 1"):
            empty.set_platform("demo", GOOD + [{"patterns": [r"x"]}])

    @pytest.mark.parametrize("patterns", [[""], [1], ["ok", None], ""])
    def test_bad_pattern_values(self, empty, patterns):
        data = [{"patterns": patterns, "sanitized": "https://example.com/{id}"}]
        with pytest.raises(InvalidPlatformError):
            empty.set_platform("demo", data)

    def test_single_pattern_string_is_still_accepted(self, empty):
        empty.set_platform("demo", [{"patterns": r"https?://example\.com/(?P<id>\w+)$", "sanitized": "https://example.com/{id}"}])
        assert empty.is_valid("demo", "https://example.com/bob")


class TestAtomicRegistration:
    def test_failed_override_keeps_the_old_platform_intact(self):
        sl = SocialLinks()
        before_data = sl.get_platform("github")
        before_compiled = list(sl._compiled["github"])
        bad = [{"patterns": ["("], "sanitized": "https://github.com/{id}"}]
        with pytest.raises(InvalidPlatformRegexError):
            sl.set_platform("github", bad, override=True)
        assert sl.get_platform("github") is before_data
        assert sl._compiled["github"] == before_compiled
        assert sl.sanitize("github", "https://github.com/foo") == "https://github.com/foo"

    def test_failed_new_platform_is_not_listed(self, empty):
        with pytest.raises(InvalidPlatformRegexError):
            empty.set_platform("demo", [{"patterns": ["("], "sanitized": "https://x/{id}"}])
        assert empty.list_platforms() == []
        assert empty._compiled == {}

    def test_set_platforms_is_all_or_nothing(self, empty):
        batch = {
            "one": GOOD,
            "two": [{"patterns": ["("], "sanitized": "https://x/{id}"}],
        }
        with pytest.raises(InvalidPlatformRegexError):
            empty.set_platforms(batch)
        assert empty.list_platforms() == []
        assert empty._compiled == {}

    def test_set_platforms_override_failure_changes_nothing(self):
        sl = SocialLinks()
        batch = {
            "github": GOOD,
            "gitlab": [{"patterns": ["("], "sanitized": "https://x/{id}"}],
        }
        with pytest.raises(InvalidPlatformRegexError):
            sl.set_platforms(batch, override=True)
        assert sl.sanitize("github", "https://github.com/foo") == "https://github.com/foo"

    def test_set_platforms_conflict_still_raises_first(self):
        sl = SocialLinks()
        with pytest.raises(PlatformAlreadyExistsError):
            sl.set_platforms({"github": GOOD})


class TestErrorMessagesHaveContext:
    def test_mismatch_names_platform_and_url(self):
        sl = SocialLinks()
        with pytest.raises(URLMismatchError, match=r"platform 'github'.*gitlab\.com/foo"):
            sl.sanitize("github", "https://gitlab.com/foo")

    def test_empty_url_names_platform(self):
        sl = SocialLinks()
        with pytest.raises(URLMismatchError, match="URL cannot be empty.*'github'"):
            sl.sanitize("github", "  ")

    def test_long_urls_are_truncated_in_messages(self):
        sl = SocialLinks()
        with pytest.raises(URLMismatchError) as exc:
            sl.sanitize("github", "https://gitlab.com/" + "a" * 5000)
        assert len(str(exc.value)) < 400

    def test_id_extraction_error_names_platform(self):
        sl = SocialLinks(use_predefined_platforms=False)
        sl.set_platform("demo", [{"patterns": [r"https?://example\.com/(?P<id>x?)$"], "sanitized": "https://example.com/{id}"}])
        with pytest.raises(PlatformIDExtractionError, match="'demo'"):
            sl.extract_id("demo", "https://example.com/")
