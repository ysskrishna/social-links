"""Social Links - A tiny, fast social-link normalizer."""

from .core import SocialLinks
from .exceptions import (
    SocialLinksError,
    PlatformNotFoundError,
    PlatformAlreadyExistsError,
    InvalidPlatformError,
    InvalidPlatformRegexError,
    PlatformIDExtractionError,
    URLMismatchError,
)

__all__ = [
    "SocialLinks",
    "SocialLinksError",
    "PlatformNotFoundError",
    "PlatformAlreadyExistsError",
    "InvalidPlatformError",
    "InvalidPlatformRegexError",
    "PlatformIDExtractionError",
    "URLMismatchError",
]

