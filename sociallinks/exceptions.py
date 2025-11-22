"""
Custom exceptions for social-links library.
"""


class SocialLinksError(Exception):
    """Base exception for all social-links errors."""
    pass


class ProfileNotFoundError(SocialLinksError):
    """Raised when a profile is not found."""
    pass


class ProfileAlreadyExistsError(SocialLinksError):
    """Raised when attempting to create a profile that already exists."""
    pass


class InvalidProfileError(SocialLinksError):
    """Raised when a profile has invalid configuration (missing patterns, templates, etc.)."""
    pass


class ProfileIDExtractionError(SocialLinksError):
    """Raised when a profile ID cannot be extracted from a URL."""
    pass


class URLMismatchError(SocialLinksError):
    """Raised when a URL does not match the expected profile pattern."""
    pass

