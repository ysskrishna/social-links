"""Social Links - A tiny, fast social-link normalizer."""

from .core import SocialLinks
from .exceptions import (
    SocialLinksError,
    PlatformError,
    PlatformNotFoundError,
    PlatformAlreadyExistsError,
    InvalidPlatformError,
    InvalidPlatformRegexError,
    URLParsingError,
    URLMismatchError,
    PlatformIDExtractionError,
)

__all__ = [
    "SocialLinks",
    "SocialLinksError",
    "PlatformError",
    "PlatformNotFoundError",
    "PlatformAlreadyExistsError",
    "InvalidPlatformError",
    "InvalidPlatformRegexError",
    "URLParsingError",
    "URLMismatchError",
    "PlatformIDExtractionError",
]

