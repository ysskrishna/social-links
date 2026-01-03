class SocialLinksError(Exception):
    """Base exception for all social-links errors."""
    pass


# ─────────────────────────────
# Platform-related errors
# ─────────────────────────────

class PlatformError(SocialLinksError):
    """Base exception for platform-related errors."""
    pass


class PlatformNotFoundError(PlatformError):
    """Raised when a platform is not found."""
    pass


class PlatformAlreadyExistsError(PlatformError):
    """Raised when attempting to create a platform that already exists."""
    pass


class InvalidPlatformError(PlatformError):
    """Raised when a platform has an invalid configuration."""
    pass


class InvalidPlatformRegexError(InvalidPlatformError):
    """Raised when a platform defines an invalid regex pattern."""
    pass


# ─────────────────────────────
# URL parsing / matching errors
# ─────────────────────────────

class URLParsingError(SocialLinksError):
    """Base exception for URL parsing and matching errors."""
    pass


class URLMismatchError(URLParsingError):
    """Raised when a URL does not match the expected platform pattern."""
    pass


class PlatformIDExtractionError(URLParsingError):
    """Raised when a platform identifier cannot be extracted from a URL."""
    pass


