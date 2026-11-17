# social-links API reference

Install with `pip install social-links` and import from `sociallinks`. Signatures and descriptions below match the docstrings in `sociallinks`.

## `SocialLinks(use_predefined_platforms: bool = True, regex_flags: int = re.IGNORECASE)`

Social Media URL Sanitizer and Validator.

Python library to validate, sanitize, and detect social media URLs.
Support for LinkedIn, Instagram, TikTok, X/Twitter, GitHub, Facebook,
YouTube, and 65+ platforms. Features automatic URL normalization and
zero dependencies. Easy to use, regex-powered, and customizable.

The class uses regex patterns to match URLs against platform-specific
formats and can normalize them to canonical forms. It also supports
custom platform definitions for extensibility.

**Attributes**

- `platforms`: Dictionary of platform configurations.
- `regex_flags`: Regex flags used for pattern compilation.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
sl.detect_platform("https://linkedin.com/in/johndoe")  # 'linkedin'
sl.sanitize("linkedin", "https://www.linkedin.com/in/johndoe/")  # 'https://linkedin.com/in/johndoe'
sl = SocialLinks(use_predefined_platforms=False)
custom = [{"patterns": [r"https?://example.com/(?P<id>\w+)"],
           "sanitized": "https://example.com/{id}"}]
sl.set_platform("example", custom)
```

Custom platforms:

### `SocialLinks.detect_platform(self, url: str) -> Optional[str]`

Detect the social media platform from a URL.

Analyzes the provided URL against all registered platform patterns
and returns the first matching platform name. The URL is automatically
stripped of leading/trailing whitespace before matching. Query strings
and fragments (for example ``?utm_source=share``) are ignored unless
the platform's URL format needs them.

**Parameters**

- `url`: The URL to analyze (e.g., "https://linkedin.com/in/johndoe"). Whitespace is automatically stripped. A bare username such as "johndoe" is not enough to identify a platform, so it returns None. Prefixed shorthands such as "u/johndoe" (Reddit) are still detected. Use `is_valid()` or `sanitize()` to check a bare ID against a platform you name.

**Returns**

- The platform name (e.g., "linkedin", "github", "x") if detected, None if no platform matches.

**Raises**

- `TypeError`: If url is not a string.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
sl.detect_platform("https://linkedin.com/in/johndoe")  # 'linkedin'
sl.detect_platform("https://github.com/username")  # 'github'
sl.detect_platform("https://x.com/username")  # 'x'
sl.detect_platform("johndoe")  # None  (Username only, no URL)
sl.detect_platform("https://example.com")  # None  (Unknown platform)
sl.detect_platform("  https://instagram.com/user  ")  # 'instagram'  (Whitespace handled)
```

### `SocialLinks.is_valid(self, platform_name: str, url: str) -> bool`

Validate a URL against a specific platform.

Checks if the provided URL matches any of the patterns defined for
the specified platform. The URL is automatically stripped of
leading/trailing whitespace before validation.

**Parameters**

- `platform_name`: The name of the platform to validate against (e.g., "linkedin", "github", "x").
- `url`: The URL to validate. Can be a full URL or just a username. Whitespace is automatically stripped.

**Returns**

- True if the URL matches the platform's patterns, False otherwise. Also returns False if the platform doesn't exist.

**Raises**

- `TypeError`: If platform_name or url is not a string.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
sl.is_valid("linkedin", "https://www.linkedin.com/in/johndoe/")  # True
sl.is_valid("linkedin", "https://github.com/username")  # False
sl.is_valid("github", "https://github.com/username")  # True
sl.is_valid("unknown_platform", "https://example.com")  # False
sl.is_valid("linkedin", "johndoe")  # True  (Bare ID for a named platform)
```

### `SocialLinks.sanitize(self, platform_name: str, url: str) -> str`

Sanitize a URL to its canonical format for a specific platform.

Normalizes a URL to the canonical format defined for the platform.
Extracts the platform-specific identifier (username, profile ID, etc.)
from the URL and formats it according to the platform's sanitized
template. The URL is automatically stripped of leading/trailing
whitespace before processing.

**Parameters**

- `platform_name`: The name of the platform (e.g., "linkedin", "github", "x").
- `url`: The URL to sanitize. Must match one of the platform's patterns. Whitespace is automatically stripped.

**Returns**

- The sanitized URL in canonical format for the platform.

**Raises**

- `TypeError`: If platform_name or url is not a string.
- `PlatformNotFoundError`: If the platform doesn't exist.
- `URLMismatchError`: If the URL doesn't match any of the platform's patterns or if the URL is empty.
- `PlatformIDExtractionError`: If the platform identifier cannot be extracted from the URL.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
sl.sanitize("linkedin", "https://www.linkedin.com/in/johndoe/")  # 'https://linkedin.com/in/johndoe'
sl.sanitize("github", "http://www.github.com/username")  # 'https://github.com/username'
sl.sanitize("x", "https://twitter.com/username")  # 'https://x.com/username'
sl.sanitize("linkedin", "https://linkedin.com/in/john-doe-123")  # 'https://linkedin.com/in/john-doe-123'
```

### `SocialLinks.extract_id(self, platform_name: str, url: str) -> str`

Extract the platform identifier from a URL.

Extracts the platform-specific identifier (username, profile ID, etc.)
from a URL. The identifier is cleaned by stripping whitespace and
trailing slashes. The URL is automatically stripped of leading/trailing
whitespace before processing.

**Parameters**

- `platform_name`: The name of the platform (e.g., "linkedin", "github", "x").
- `url`: The URL to extract the identifier from. Must match one of the platform's patterns. Whitespace is automatically stripped.

**Returns**

- The extracted platform identifier string.

**Raises**

- `TypeError`: If platform_name or url is not a string.
- `PlatformNotFoundError`: If the platform doesn't exist.
- `URLMismatchError`: If the URL doesn't match any of the platform's patterns or if the URL is empty.
- `PlatformIDExtractionError`: If the platform identifier cannot be extracted from the URL.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
sl.extract_id("linkedin", "https://www.linkedin.com/in/johndoe/")  # 'johndoe'
sl.extract_id("github", "https://github.com/username")  # 'username'
sl.extract_id("x", "https://twitter.com/elonmusk")  # 'elonmusk'
sl.extract_id("linkedin", "https://linkedin.com/company/acme")  # 'acme'
```

### `SocialLinks.set_platform(self, name: str, data: List[Dict[str, Any]], *, override: bool = False) -> None`

Add or update a platform configuration.

Registers a new platform. If the platform already exists, updates it
only when override=True (default behavior raises an error). The platform
patterns are compiled immediately and made available for use.

**Parameters**

- `name`: The name of the platform (e.g., "custom_platform").
- `data`: Platform configuration as a list of dictionaries. Each dictionary should contain: - "patterns": A regex pattern string or list of patterns that match URLs for this platform. Patterns should use named groups like `(?P<id>...)` to capture identifiers. Patterns are matched from the start of the input (`re.match`), so a URL embedded in a longer string does not match. End a pattern with `$` to reject trailing text. - "sanitized": A template string for the canonical URL format, using `{id}` as a placeholder for the extracted identifier.
- `override`: If False (default), raises an error if the platform already exists. If True, replaces the existing platform configuration.

**Raises**

- `PlatformAlreadyExistsError`: If the platform already exists and override is False.
- `InvalidPlatformError`: If the configuration is invalid: not a non-empty list of dicts, an entry without patterns, or a "sanitized" template that does not use `{id}` as its only placeholder. Nothing is registered when this is raised.
- `InvalidPlatformRegexError`: If any regex pattern is invalid. The existing platform (if any) is left unchanged.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks(use_predefined_platforms=False)
custom = [{
    "patterns": [
        r"https?://(www\.)?example\.com/(?P<id>[A-Za-z0-9_]+)/?$",
        r"^(?P<id>[A-Za-z0-9_]+)$"
    ],
    "sanitized": "https://example.com/{id}"
}]
sl.set_platform("example", custom)
sl.detect_platform("https://example.com/user123")  # 'example'
sl.sanitize("example", "https://example.com/user123")  # 'https://example.com/user123'
# Update existing platform
sl.set_platform("example", custom, override=True)
```

### `SocialLinks.delete_platform(self, name: str) -> None`

Delete a platform configuration.

Removes a platform from the registry. The platform will no longer
be available for detection, validation, or sanitization.

**Parameters**

- `name`: The name of the platform to delete.

**Raises**

- `PlatformNotFoundError`: If the platform doesn't exist.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
"linkedin" in sl.list_platforms()  # True
sl.delete_platform("linkedin")
"linkedin" in sl.list_platforms()  # False
```

### `SocialLinks.set_platforms(self, platforms: Dict[str, List[Dict[str, Any]]], *, override: bool = False) -> None`

Add or update multiple platform configurations at once.

Bulk operation to register multiple platforms. If any platform already
exists, updates occur only when override=True (default behavior raises
an error). This is more efficient than calling `set_platform()` multiple
times.

**Parameters**

- `platforms`: Dictionary mapping platform names to their configurations. Each value should be a `PlatformEntry` (list of dictionaries with "patterns" and "sanitized" keys).
- `override`: If False (default), raises an error if any platform already exists. If True, replaces existing platform configurations.

**Raises**

- `PlatformAlreadyExistsError`: If any platform already exists and override is False.
- `InvalidPlatformError`: If any platform configuration is invalid.
- `InvalidPlatformRegexError`: If any regex pattern is invalid. The operation is all-or-nothing: if any entry raises, no platform from this call is registered.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks(use_predefined_platforms=False)
new_platforms = {
    "platform1": [{
        "patterns": [r"https?://example1.com/(?P<id>\w+)"],
        "sanitized": "https://example1.com/{id}"
    }],
    "platform2": [{
        "patterns": [r"https?://example2.com/(?P<id>\w+)"],
        "sanitized": "https://example2.com/{id}"
    }]
}
sl.set_platforms(new_platforms)
len(sl.list_platforms())  # 2
```

### `SocialLinks.delete_platforms(self, names: List[str]) -> None`

Delete multiple platform configurations at once.

Bulk operation to remove multiple platforms. This is more efficient
than calling `delete_platform()` multiple times.

**Parameters**

- `names`: List of platform names to delete.

**Raises**

- `PlatformNotFoundError`: If any of the specified platforms don't exist. The error message includes all missing platforms.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
sl.delete_platforms(["linkedin", "github"])
"linkedin" in sl.list_platforms()  # False
"github" in sl.list_platforms()  # False
```

### `SocialLinks.clear_platforms(self) -> None`

Remove all platform configurations.

Clears both the platform registry and compiled patterns. After calling
this method, no platforms will be available until new ones are added.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
len(sl.list_platforms()) > 0  # True
sl.clear_platforms()
sl.list_platforms()  # []
```

### `SocialLinks.get_platform(self, name: str) -> List[Dict[str, Any]]`

Get the configuration for a specific platform.

Retrieves the platform configuration, which can be useful for
inspection or modification before re-adding with `set_platform()`.

**Parameters**

- `name`: The name of the platform.

**Returns**

- The platform configuration as a `PlatformEntry` (list of dictionaries with "patterns" and "sanitized" keys).

**Raises**

- `PlatformNotFoundError`: If the platform doesn't exist.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
config = sl.get_platform("github")
isinstance(config, list)  # True
"patterns" in config[0]  # True
"sanitized" in config[0]  # True
```

### `SocialLinks.list_platforms(self) -> List[str]`

List all registered platform names.

Returns a list of all platform names that are currently registered
and available for use.

**Returns**

- A list of platform names (strings) in no particular order.

**Example**

```python
from sociallinks import SocialLinks

sl = SocialLinks()
platforms = sl.list_platforms()
isinstance(platforms, list)  # True
"linkedin" in platforms  # True
"github" in platforms  # True
len(platforms) > 50  # True
```

## `detect_platform(url: str) -> Optional[str]`

Detect the social media platform from a URL.

This is a convenience function that uses a default SocialLinks instance
with predefined platforms. For custom configurations (regex flags, custom
platforms), use the SocialLinks class directly.

**Parameters**

- `url`: The URL to analyze (e.g., "https://linkedin.com/in/johndoe"). Whitespace is automatically stripped. A bare username such as "johndoe" cannot identify a platform, so it returns None. Use `is_valid()` or `sanitize()` to check a bare ID against a platform you name.

**Returns**

- The platform name (e.g., "linkedin", "github", "x") if detected, None if no platform matches.

**Raises**

- `TypeError`: If url is not a string.

**Example**

```python
from sociallinks import detect_platform

from sociallinks import detect_platform
detect_platform("https://linkedin.com/in/johndoe")  # 'linkedin'
detect_platform("https://github.com/username")  # 'github'
detect_platform("https://example.com")  # None
```

## `is_valid(platform_name: str, url: str) -> bool`

Validate a URL against a specific platform.

This is a convenience function that uses a default SocialLinks instance
with predefined platforms. For custom configurations, use the SocialLinks
class directly.

**Parameters**

- `platform_name`: The name of the platform to validate against (e.g., "linkedin", "github", "x").
- `url`: The URL to validate. Can be a full URL or just a username. Whitespace is automatically stripped.

**Returns**

- True if the URL matches the platform's patterns, False otherwise. Also returns False if the platform doesn't exist.

**Raises**

- `TypeError`: If platform_name or url is not a string.

**Example**

```python
from sociallinks import is_valid

from sociallinks import is_valid
is_valid("linkedin", "https://www.linkedin.com/in/johndoe/")  # True
is_valid("linkedin", "https://github.com/username")  # False
is_valid("github", "https://github.com/username")  # True
```

## `sanitize(platform_name: str, url: str) -> str`

Sanitize a URL to its canonical format for a specific platform.

This is a convenience function that uses a default SocialLinks instance
with predefined platforms. For custom configurations, use the SocialLinks
class directly.

**Parameters**

- `platform_name`: The name of the platform (e.g., "linkedin", "github", "x").
- `url`: The URL to sanitize. Must match one of the platform's patterns. Whitespace is automatically stripped.

**Returns**

- The sanitized URL in canonical format for the platform.

**Raises**

- `TypeError`: If platform_name or url is not a string.
- `PlatformNotFoundError`: If the platform doesn't exist.
- `URLMismatchError`: If the URL doesn't match any of the platform's patterns or if the URL is empty.
- `PlatformIDExtractionError`: If the platform identifier cannot be extracted from the URL.

**Example**

```python
from sociallinks import sanitize

from sociallinks import sanitize
sanitize("linkedin", "https://www.linkedin.com/in/johndoe/")  # 'https://linkedin.com/in/johndoe'
sanitize("github", "http://www.github.com/username")  # 'https://github.com/username'
sanitize("x", "https://twitter.com/username")  # 'https://x.com/username'
```

## `extract_id(platform_name: str, url: str) -> str`

Extract the platform identifier from a URL.

This is a convenience function that uses a default SocialLinks instance
with predefined platforms. For custom configurations, use the SocialLinks
class directly.

**Parameters**

- `platform_name`: The name of the platform (e.g., "linkedin", "github", "x").
- `url`: The URL to extract the identifier from. Must match one of the platform's patterns. Whitespace is automatically stripped.

**Returns**

- The extracted platform identifier string.

**Raises**

- `TypeError`: If platform_name or url is not a string.
- `PlatformNotFoundError`: If the platform doesn't exist.
- `URLMismatchError`: If the URL doesn't match any of the platform's patterns or if the URL is empty.
- `PlatformIDExtractionError`: If the platform identifier cannot be extracted from the URL.

**Example**

```python
from sociallinks import extract_id

from sociallinks import extract_id
extract_id("linkedin", "https://www.linkedin.com/in/johndoe/")  # 'johndoe'
extract_id("github", "https://github.com/username")  # 'username'
extract_id("x", "https://twitter.com/elonmusk")  # 'elonmusk'
```

## `list_platforms() -> List[str]`

List all registered platform names.

This is a convenience function that uses a default SocialLinks instance
with predefined platforms. Returns all platforms available for detection,
validation, and sanitization.

**Returns**

- A list of platform names (strings) in no particular order.

**Example**

```python
from sociallinks import list_platforms

from sociallinks import list_platforms
platforms = list_platforms()
"linkedin" in platforms  # True
"github" in platforms  # True
len(platforms) > 50  # True
```

## `SocialLinksError`

Exception class (subclass of `Exception`).

Base exception for all social-links errors.

All custom exceptions in the social-links library inherit from this class,
allowing you to catch all social-links related errors with a single
exception handler.

## `PlatformError`

Exception class (subclass of `SocialLinksError`).

Base exception for platform-related errors.

This exception serves as the base class for all errors related to platform
management, including platform registration, configuration, and lookup.
All platform-specific errors inherit from this class.

## `PlatformNotFoundError`

Exception class (subclass of `PlatformError`).

Raised when a platform is not found.

This exception is raised when attempting to access, modify, or delete a
platform that does not exist in the platform registry.

## `PlatformAlreadyExistsError`

Exception class (subclass of `PlatformError`).

Raised when attempting to create a platform that already exists.

This exception is raised when trying to register a platform with a name
that is already in use. To replace an existing platform, use the ``override=True``
parameter with `SocialLinks.set_platform` or `SocialLinks.set_platforms`.

## `InvalidPlatformError`

Exception class (subclass of `PlatformError`).

Raised when a platform has an invalid configuration.

This exception is raised when a platform configuration is missing required
fields or has invalid structure. A valid platform entry must be a list
of dictionaries, each containing both `patterns` and `sanitized` keys.
Entries missing either field are skipped, but at least one complete entry
is required for the platform to be valid.

## `InvalidPlatformRegexError`

Exception class (subclass of `InvalidPlatformError`).

Raised when a platform defines an invalid regex pattern.

This exception is raised when a regex pattern in a platform configuration
cannot be compiled, typically due to syntax errors in the pattern string.

## `URLParsingError`

Exception class (subclass of `SocialLinksError`).

Base exception for URL parsing and matching errors.

This exception serves as the base class for all errors related to URL
parsing, validation, and matching operations. All URL-related errors
inherit from this class.

## `URLMismatchError`

Exception class (subclass of `URLParsingError`).

Raised when a URL does not match the expected platform pattern.

This exception is raised when attempting to validate or sanitize a URL
that doesn't match any of the patterns defined for the specified platform.

## `PlatformIDExtractionError`

Exception class (subclass of `URLParsingError`).

Raised when a platform identifier cannot be extracted from a URL.

This exception is raised when a URL matches a platform pattern but the
platform identifier (username, ID, etc.) cannot be extracted, typically
due to a missing or incorrectly named capture group in the regex pattern.

