import re
import string
from typing import Dict, List, NamedTuple, Optional, Any, Tuple
from sociallinks.constants import (
    PHONE_NUMBER,
    PROFILE_ID,
    PROFILE_ID_AT,
    PROFILE_ID_EXTENDED,
    PROFILE_ID_UNICODE,
    PlatformEntry,
    PlatformEntries,
)
from sociallinks.platforms import PREDEFINED_PLATFORMS
from sociallinks.exceptions import (
    PlatformNotFoundError,
    PlatformAlreadyExistsError,
    InvalidPlatformError,
    InvalidPlatformRegexError,
    PlatformIDExtractionError,
    URLMismatchError,
)

_NUMERIC_ID = r"(?P<id>\d+)"  # bare numeric IDs, e.g. Apple Music artist IDs

_BARE_ID_BODIES = frozenset(
    {
        PROFILE_ID,
        PROFILE_ID_AT,
        PROFILE_ID_UNICODE,
        PROFILE_ID_EXTENDED,
        PHONE_NUMBER,
        _NUMERIC_ID,
    }
)


def _is_bare_id_pattern(pattern: str) -> bool:
    """Return True if a pattern accepts only a bare ID (``^<id>$`` or ``^@?<id>$``).

    Only patterns built from the library's own ID regexes in
    ``sociallinks.constants`` are recognised. Prefixed shorthands such as
    ``^u/<id>$`` or ``^spotify:artist:<id>$`` are not bare.
    """
    if not (pattern.startswith("^") and pattern.endswith("$")):
        return False
    body = pattern[1:-1]
    if body.startswith("@?"):
        body = body[2:]
    return body in _BARE_ID_BODIES


# Generic site paths that look like profile IDs. When a URL only matches after
# its query string or fragment was removed, these IDs are rejected so that
# links such as youtube.com/watch?v=... or x.com/search?q=... are not mistaken
# for profiles. The check is not applied to the input exactly as given.
_RESERVED_IDS = frozenset(
    {
        "about", "account", "explore", "feed", "groups", "hashtag", "help",
        "home", "intent", "live", "login", "logout", "marketplace",
        "messages", "notifications", "playlist", "pricing", "privacy",
        "profile.php", "register", "results", "search", "settings", "share",
        "sharer", "sharer.php", "shorts", "signup", "sign_up", "terms", "watch",
    }
)


class _CompiledPattern(NamedTuple):
    pattern: re.Pattern
    sanitized: str
    bare: bool


class SocialLinks:
    """Social Media URL Sanitizer and Validator.

    Python library to validate, sanitize, and detect social media URLs.
    Support for LinkedIn, Instagram, TikTok, X/Twitter, GitHub, Facebook,
    YouTube, and 65+ platforms. Features automatic URL normalization and
    zero dependencies. Easy to use, regex-powered, and customizable.

    The class uses regex patterns to match URLs against platform-specific
    formats and can normalize them to canonical forms. It also supports
    custom platform definitions for extensibility.

    Attributes:
        platforms: Dictionary of platform configurations.
        regex_flags: Regex flags used for pattern compilation.

    Examples:
        Basic usage with predefined platforms:

        >>> sl = SocialLinks()
        >>> sl.detect_platform("https://linkedin.com/in/johndoe")
        'linkedin'
        >>> sl.sanitize("linkedin", "https://www.linkedin.com/in/johndoe/")
        'https://linkedin.com/in/johndoe'

        Custom platforms:

        >>> sl = SocialLinks(use_predefined_platforms=False)
        >>> custom = [{"patterns": [r"https?://example.com/(?P<id>\\w+)"],
        ...            "sanitized": "https://example.com/{id}"}]
        >>> sl.set_platform("example", custom)
    """

    def __init__(
        self,
        use_predefined_platforms: bool = True,
        regex_flags: int = re.IGNORECASE,
    ):
        """Initialize the SocialLinks instance.

        Args:
            use_predefined_platforms: If True, loads 65+ predefined social
                media platforms (LinkedIn, GitHub, Twitter/X, etc.). If False,
                starts with an empty platform list. Defaults to True.
            regex_flags: Regex flags to use for pattern compilation. Defaults
                to `re.IGNORECASE`. Can be combined with other flags like
                `re.MULTILINE` using bitwise OR (|).

        Examples:
            >>> # Use predefined platforms (default)
            >>> sl = SocialLinks()
            >>> len(sl.list_platforms()) > 65
            True

            >>> # Start with empty platform list
            >>> sl = SocialLinks(use_predefined_platforms=False)
            >>> sl.list_platforms()
            []

            >>> # Use custom regex flags
            >>> import re
            >>> sl = SocialLinks(regex_flags=re.IGNORECASE | re.MULTILINE)
        """
        self.platforms: PlatformEntries = {}
        self._compiled: Dict[str, List[_CompiledPattern]] = {}
        self.regex_flags: int = regex_flags

        if use_predefined_platforms:
            self.platforms.update(PREDEFINED_PLATFORMS)

        # Compile all
        for name, data in self.platforms.items():
            self._compiled[name] = self._compile_platform(name, data)

    # ------------------------------------------------------------------
    # Internal Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _short(value: str, limit: int = 200) -> str:
        """Shorten a string for use in an error message."""
        return value if len(value) <= limit else value[:limit] + "..."

    def _compile_platform(self, name: str, data: PlatformEntry) -> List[_CompiledPattern]:
        """Validate and compile the regex patterns of a platform.

        Internal method. It does not modify the instance, so callers can
        compile first and only then register the platform, which keeps
        ``platforms`` and the compiled patterns consistent when it raises.

        Args:
            name: Platform name.
            data: Platform configuration.

        Returns:
            The compiled patterns with their sanitized templates.

        Raises:
            InvalidPlatformError: If the configuration is not a list of
                entries, an entry has no patterns, or its ``sanitized``
                template is missing, is not a string, or does not use
                ``{id}`` as its only placeholder.
            InvalidPlatformRegexError: If any regex pattern is invalid.
        """
        if not isinstance(data, list) or not data:
            raise InvalidPlatformError(
                f"Platform '{name}' has no valid patterns or templates: "
                "expected a non-empty list of entries."
            )

        compiled_entries: List[_CompiledPattern] = []

        for index, entry in enumerate(data):
            where = f"Platform '{name}' entry {index}"
            if not isinstance(entry, dict):
                raise InvalidPlatformError(
                    f"{where} has no valid patterns or templates: "
                    f"expected a dict, got {type(entry).__name__}."
                )

            patterns = entry.get("patterns")
            sanitized = entry.get("sanitized")
            pattern_list = patterns if isinstance(patterns, list) else [patterns]

            if (
                not patterns
                or not isinstance(sanitized, str)
                or not sanitized
                or not all(isinstance(p, str) and p for p in pattern_list)
            ):
                raise InvalidPlatformError(
                    f"{where} has no valid patterns or templates: "
                    "'patterns' must be a non-empty regex string or list of strings "
                    "and 'sanitized' a non-empty string."
                )

            try:
                fields = [f for _, f, _, _ in string.Formatter().parse(sanitized) if f is not None]
            except ValueError as e:
                raise InvalidPlatformError(
                    f"{where} has an invalid 'sanitized' template {sanitized!r}: {e}"
                ) from e
            if "id" not in fields or any(f != "id" for f in fields):
                raise InvalidPlatformError(
                    f"{where} 'sanitized' template {sanitized!r} must contain "
                    "{id} and no other placeholders."
                )

            for p in pattern_list:
                try:
                    compiled_entries.append(
                        _CompiledPattern(
                            re.compile(p, flags=self.regex_flags),
                            sanitized,
                            _is_bare_id_pattern(p),
                        )
                    )
                except re.error as e:
                    raise InvalidPlatformRegexError(
                        f"Invalid regex pattern for platform '{name}': {p}"
                    ) from e

        return compiled_entries

    @staticmethod
    def _id_from_match(match: re.Match) -> Optional[str]:
        """Extract platform identifier from a regex match.

        Attempts to extract the identifier using a named group "id",
        or falls back to the first non-empty capturing group.

        Args:
            match: Regex match object.

        Returns:
            Extracted identifier string, or None if not found.
        """
        if "id" in match.groupdict() and match.group("id"):
            return match.group("id")

        for g in match.groups():
            if g:
                return g
        return None

    @staticmethod
    def _strip_query_fragment(u: str) -> str:
        """Return ``u`` without its query string and fragment."""
        cuts = [i for i in (u.find("?"), u.find("#")) if i != -1]
        return u[: min(cuts)] if cuts else u

    def _find_match(
        self,
        entries: List[_CompiledPattern],
        u: str,
        *,
        for_detection: bool = False,
    ) -> Optional[Tuple[_CompiledPattern, "re.Match"]]:
        """Find the first pattern that matches ``u``.

        The input is tried as given first, so platforms whose URLs need a
        query string or fragment (Hacker News ``?id=``, Signal ``#p/``) keep
        working. If nothing matches, it is tried again without the query
        string and fragment, so share links such as ``?utm_source=share``
        are accepted. Bare-ID patterns are not used on that second pass, and
        generic site paths (``watch``, ``search``, ``profile.php``, ...) are
        rejected there, see ``_RESERVED_IDS``.

        Args:
            entries: Compiled patterns of one platform.
            u: The stripped input string.
            for_detection: If True, bare-ID patterns are skipped (used by
                ``detect_platform``).

        Returns:
            The matching compiled pattern and its match object, or None.
        """
        for compiled in entries:
            if for_detection and compiled.bare:
                continue
            m = compiled.pattern.match(u)
            if m:
                return compiled, m

        stripped = self._strip_query_fragment(u)
        if stripped and stripped != u:
            for compiled in entries:
                if compiled.bare:
                    continue
                m = compiled.pattern.match(stripped)
                if m and (self._id_from_match(m) or "").lower() not in _RESERVED_IDS:
                    return compiled, m
        return None

    def _match_url(self, platform_name: str, url: str) -> Tuple[str, str]:
        """Match a URL against a platform's patterns and extract the ID.

        Shared logic for sanitize() and extract_id(). Validates inputs,
        looks up the platform, matches the URL, and extracts/cleans the ID.

        Args:
            platform_name: The name of the platform.
            url: The URL to match.

        Returns:
            A tuple of (cleaned_id, sanitized_template).

        Raises:
            TypeError: If platform_name or url is not a string.
            PlatformNotFoundError: If the platform doesn't exist.
            URLMismatchError: If the URL doesn't match or is empty.
            PlatformIDExtractionError: If the ID cannot be extracted.
        """
        if not isinstance(platform_name, str):
            raise TypeError(f"platform_name must be str, not {type(platform_name).__name__}")
        if not isinstance(url, str):
            raise TypeError(f"url must be str, not {type(url).__name__}")

        entries = self._compiled.get(platform_name)
        if not entries:
            raise PlatformNotFoundError(f"Unknown platform: {platform_name}")

        u = url.strip()
        if not u:
            raise URLMismatchError(f"URL cannot be empty (platform '{platform_name}')")

        found = self._find_match(entries, u)
        if found:
            compiled, m = found
            pid = self._id_from_match(m)
            if not pid:
                raise PlatformIDExtractionError(
                    f"Could not extract platform ID for '{platform_name}' from {self._short(u)!r}"
                )
            pid = pid.strip().rstrip("/")
            return pid, compiled.sanitized

        raise URLMismatchError(
            f"URL does not match platform '{platform_name}': {self._short(u)!r}"
        )

    # ------------------------------------------------------------------
    # Core API
    # ------------------------------------------------------------------

    def detect_platform(self, url: str) -> Optional[str]:
        """Detect the social media platform from a URL.

        Analyzes the provided URL against all registered platform patterns
        and returns the first matching platform name. The URL is automatically
        stripped of leading/trailing whitespace before matching. Query strings
        and fragments (for example ``?utm_source=share``) are ignored unless
        the platform's URL format needs them.

        Args:
            url: The URL to analyze (e.g., "https://linkedin.com/in/johndoe").
                Whitespace is automatically stripped. A bare username such as
                "johndoe" is not enough to identify a platform, so it returns
                None. Prefixed shorthands such as "u/johndoe" (Reddit) are
                still detected. Use `is_valid()` or `sanitize()` to check a
                bare ID against a platform you name.

        Returns:
            The platform name (e.g., "linkedin", "github", "x") if detected,
            None if no platform matches.

        Raises:
            TypeError: If url is not a string.

        Examples:
            >>> sl = SocialLinks()
            >>> sl.detect_platform("https://linkedin.com/in/johndoe")
            'linkedin'
            >>> sl.detect_platform("https://github.com/username")
            'github'
            >>> sl.detect_platform("https://x.com/username")
            'x'
            >>> sl.detect_platform("johndoe")  # Username only, no URL
            None
            >>> sl.detect_platform("https://example.com")  # Unknown platform
            None
            >>> sl.detect_platform("  https://instagram.com/user  ")  # Whitespace handled
            'instagram'
        """
        if not isinstance(url, str):
            raise TypeError(f"url must be str, not {type(url).__name__}")
        
        u = url.strip()
        if not u:
            return None
        
        for name, entries in self._compiled.items():
            if self._find_match(entries, u, for_detection=True):
                return name
        return None

    def is_valid(self, platform_name: str, url: str) -> bool:
        """Validate a URL against a specific platform.

        Checks if the provided URL matches any of the patterns defined for
        the specified platform. The URL is automatically stripped of
        leading/trailing whitespace before validation.

        Args:
            platform_name: The name of the platform to validate against
                (e.g., "linkedin", "github", "x").
            url: The URL to validate. Can be a full URL or just a username.
                Whitespace is automatically stripped.

        Returns:
            True if the URL matches the platform's patterns, False otherwise.
            Also returns False if the platform doesn't exist.

        Raises:
            TypeError: If platform_name or url is not a string.

        Examples:
            >>> sl = SocialLinks()
            >>> sl.is_valid("linkedin", "https://www.linkedin.com/in/johndoe/")
            True
            >>> sl.is_valid("linkedin", "https://github.com/username")
            False
            >>> sl.is_valid("github", "https://github.com/username")
            True
            >>> sl.is_valid("unknown_platform", "https://example.com")
            False
            >>> sl.is_valid("linkedin", "johndoe")  # Bare ID for a named platform
            True
        """
        if not isinstance(platform_name, str):
            raise TypeError(f"platform_name must be str, not {type(platform_name).__name__}")
        if not isinstance(url, str):
            raise TypeError(f"url must be str, not {type(url).__name__}")
        
        entries = self._compiled.get(platform_name)
        if not entries:
            return False
        
        u = url.strip()
        if not u:
            return False
        
        return self._find_match(entries, u) is not None

    def sanitize(self, platform_name: str, url: str) -> str:
        """Sanitize a URL to its canonical format for a specific platform.

        Normalizes a URL to the canonical format defined for the platform.
        Extracts the platform-specific identifier (username, profile ID, etc.)
        from the URL and formats it according to the platform's sanitized
        template. The URL is automatically stripped of leading/trailing
        whitespace before processing.

        Args:
            platform_name: The name of the platform (e.g., "linkedin",
                "github", "x").
            url: The URL to sanitize. Must match one of the platform's
                patterns. Whitespace is automatically stripped.

        Returns:
            The sanitized URL in canonical format for the platform.

        Raises:
            TypeError: If platform_name or url is not a string.
            PlatformNotFoundError: If the platform doesn't exist.
            URLMismatchError: If the URL doesn't match any of the platform's
                patterns or if the URL is empty.
            PlatformIDExtractionError: If the platform identifier cannot be
                extracted from the URL.

        Examples:
            >>> sl = SocialLinks()
            >>> sl.sanitize("linkedin", "https://www.linkedin.com/in/johndoe/")
            'https://linkedin.com/in/johndoe'
            >>> sl.sanitize("github", "http://www.github.com/username")
            'https://github.com/username'
            >>> sl.sanitize("x", "https://twitter.com/username")
            'https://x.com/username'
            >>> sl.sanitize("linkedin", "https://linkedin.com/in/john-doe-123")
            'https://linkedin.com/in/john-doe-123'
        """
        pid, sanitized_template = self._match_url(platform_name, url)
        return sanitized_template.format(id=pid)

    def extract_id(self, platform_name: str, url: str) -> str:
        """Extract the platform identifier from a URL.

        Extracts the platform-specific identifier (username, profile ID, etc.)
        from a URL. The identifier is cleaned by stripping whitespace and
        trailing slashes. The URL is automatically stripped of leading/trailing
        whitespace before processing.

        Args:
            platform_name: The name of the platform (e.g., "linkedin",
                "github", "x").
            url: The URL to extract the identifier from. Must match one of
                the platform's patterns. Whitespace is automatically stripped.

        Returns:
            The extracted platform identifier string.

        Raises:
            TypeError: If platform_name or url is not a string.
            PlatformNotFoundError: If the platform doesn't exist.
            URLMismatchError: If the URL doesn't match any of the platform's
                patterns or if the URL is empty.
            PlatformIDExtractionError: If the platform identifier cannot be
                extracted from the URL.

        Examples:
            >>> sl = SocialLinks()
            >>> sl.extract_id("linkedin", "https://www.linkedin.com/in/johndoe/")
            'johndoe'
            >>> sl.extract_id("github", "https://github.com/username")
            'username'
            >>> sl.extract_id("x", "https://twitter.com/elonmusk")
            'elonmusk'
            >>> sl.extract_id("linkedin", "https://linkedin.com/company/acme")
            'acme'
        """
        pid, _ = self._match_url(platform_name, url)
        return pid

    # ------------------------------------------------------------------
    # Platform CRUD (single + bulk)
    # ------------------------------------------------------------------

    def set_platform(self, name: str, data: PlatformEntry, *, override: bool = False) -> None:
        """Add or update a platform configuration.

        Registers a new platform. If the platform already exists, updates it
        only when override=True (default behavior raises an error). The platform
        patterns are compiled immediately and made available for use.

        Args:
            name: The name of the platform (e.g., "custom_platform").
            data: Platform configuration as a list of dictionaries. Each
                dictionary should contain:
                - "patterns": A regex pattern string or list of patterns
                  that match URLs for this platform. Patterns should use
                  named groups like `(?P<id>...)` to capture identifiers.
                  Patterns are matched from the start of the input
                  (`re.match`), so a URL embedded in a longer string does
                  not match. End a pattern with `$` to reject trailing text.
                - "sanitized": A template string for the canonical URL format,
                  using `{id}` as a placeholder for the extracted identifier.
            override: If False (default), raises an error if the platform
                already exists. If True, replaces the existing platform
                configuration.

        Raises:
            PlatformAlreadyExistsError: If the platform already exists and
                override is False.
            InvalidPlatformError: If the configuration is invalid: not a
                non-empty list of dicts, an entry without patterns, or a
                "sanitized" template that does not use `{id}` as its only
                placeholder. Nothing is registered when this is raised.
            InvalidPlatformRegexError: If any regex pattern is invalid.
                The existing platform (if any) is left unchanged.

        Examples:
            >>> sl = SocialLinks(use_predefined_platforms=False)
            >>> custom = [{
            ...     "patterns": [
            ...         r"https?://(www\\.)?example\\.com/(?P<id>[A-Za-z0-9_]+)/?$",
            ...         r"^(?P<id>[A-Za-z0-9_]+)$"
            ...     ],
            ...     "sanitized": "https://example.com/{id}"
            ... }]
            >>> sl.set_platform("example", custom)
            >>> sl.detect_platform("https://example.com/user123")
            'example'
            >>> sl.sanitize("example", "https://example.com/user123")
            'https://example.com/user123'

            >>> # Update existing platform
            >>> sl.set_platform("example", custom, override=True)
        """
        exists = name in self.platforms
        if exists and not override:
            raise PlatformAlreadyExistsError(f"Platform '{name}' already exists. Use override=True.")

        compiled = self._compile_platform(name, data)
        self.platforms[name] = data
        self._compiled[name] = compiled

    def delete_platform(self, name: str) -> None:
        """Delete a platform configuration.

        Removes a platform from the registry. The platform will no longer
        be available for detection, validation, or sanitization.

        Args:
            name: The name of the platform to delete.

        Raises:
            PlatformNotFoundError: If the platform doesn't exist.

        Examples:
            >>> sl = SocialLinks()
            >>> "linkedin" in sl.list_platforms()
            True
            >>> sl.delete_platform("linkedin")
            >>> "linkedin" in sl.list_platforms()
            False
        """
        if name not in self.platforms:
            raise PlatformNotFoundError(f"Platform '{name}' not found")
        del self.platforms[name]
        self._compiled.pop(name, None)

    def set_platforms(self, platforms: PlatformEntries, *, override: bool = False) -> None:
        """Add or update multiple platform configurations at once.

        Bulk operation to register multiple platforms. If any platform already
        exists, updates occur only when override=True (default behavior raises
        an error). This is more efficient than calling `set_platform()` multiple
        times.

        Args:
            platforms: Dictionary mapping platform names to their
                configurations. Each value should be a `PlatformEntry` (list
                of dictionaries with "patterns" and "sanitized" keys).
            override: If False (default), raises an error if any platform
                already exists. If True, replaces existing platform
                configurations.

        Raises:
            PlatformAlreadyExistsError: If any platform already exists and
                override is False.
            InvalidPlatformError: If any platform configuration is invalid.
            InvalidPlatformRegexError: If any regex pattern is invalid.
                The operation is all-or-nothing: if any entry raises, no
                platform from this call is registered.

        Examples:
            >>> sl = SocialLinks(use_predefined_platforms=False)
            >>> new_platforms = {
            ...     "platform1": [{
            ...         "patterns": [r"https?://example1.com/(?P<id>\\w+)"],
            ...         "sanitized": "https://example1.com/{id}"
            ...     }],
            ...     "platform2": [{
            ...         "patterns": [r"https?://example2.com/(?P<id>\\w+)"],
            ...         "sanitized": "https://example2.com/{id}"
            ...     }]
            ... }
            >>> sl.set_platforms(new_platforms)
            >>> len(sl.list_platforms())
            2
        """
        if not override:
            conflicts = [name for name in platforms if name in self.platforms]
            if conflicts:
                raise PlatformAlreadyExistsError(f"Platforms already exist: {', '.join(conflicts)}")

        # Compile everything first so a bad entry leaves the instance unchanged.
        compiled = {
            name: self._compile_platform(name, data) for name, data in platforms.items()
        }
        for name, data in platforms.items():
            self.platforms[name] = data
            self._compiled[name] = compiled[name]

    def delete_platforms(self, names: List[str]) -> None:
        """Delete multiple platform configurations at once.

        Bulk operation to remove multiple platforms. This is more efficient
        than calling `delete_platform()` multiple times.

        Args:
            names: List of platform names to delete.

        Raises:
            PlatformNotFoundError: If any of the specified platforms don't
                exist. The error message includes all missing platforms.

        Examples:
            >>> sl = SocialLinks()
            >>> sl.delete_platforms(["linkedin", "github"])
            >>> "linkedin" in sl.list_platforms()
            False
            >>> "github" in sl.list_platforms()
            False
        """
        missing = [n for n in names if n not in self.platforms]
        if missing:
            raise PlatformNotFoundError(f"Platforms not found: {', '.join(missing)}")
        for n in names:
            self.delete_platform(n)

    def clear_platforms(self) -> None:
        """Remove all platform configurations.

        Clears both the platform registry and compiled patterns. After calling
        this method, no platforms will be available until new ones are added.

        Examples:
            >>> sl = SocialLinks()
            >>> len(sl.list_platforms()) > 0
            True
            >>> sl.clear_platforms()
            >>> sl.list_platforms()
            []
        """
        self.platforms.clear()
        self._compiled.clear()

    def get_platform(self, name: str) -> PlatformEntry:
        """Get the configuration for a specific platform.

        Retrieves the platform configuration, which can be useful for
        inspection or modification before re-adding with `set_platform()`.

        Args:
            name: The name of the platform.

        Returns:
            The platform configuration as a `PlatformEntry` (list of
            dictionaries with "patterns" and "sanitized" keys).

        Raises:
            PlatformNotFoundError: If the platform doesn't exist.

        Examples:
            >>> sl = SocialLinks()
            >>> config = sl.get_platform("github")
            >>> isinstance(config, list)
            True
            >>> "patterns" in config[0]
            True
            >>> "sanitized" in config[0]
            True
        """
        if name not in self.platforms:
            raise PlatformNotFoundError(f"Platform '{name}' not found")
        return self.platforms[name]

    def list_platforms(self) -> List[str]:
        """List all registered platform names.

        Returns a list of all platform names that are currently registered
        and available for use.

        Returns:
            A list of platform names (strings) in no particular order.

        Examples:
            >>> sl = SocialLinks()
            >>> platforms = sl.list_platforms()
            >>> isinstance(platforms, list)
            True
            >>> "linkedin" in platforms
            True
            >>> "github" in platforms
            True
            >>> len(platforms) > 50
            True
        """
        return list(self.platforms.keys())
