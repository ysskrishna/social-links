"""Social Links - A tiny, fast social-link normalizer."""

from .core import SocialLinks
from .exceptions import (
    SocialLinksError,
    ProfileNotFoundError,
    ProfileAlreadyExistsError,
    InvalidProfileError,
    ProfileIDExtractionError,
    URLMismatchError,
)

__all__ = [
    "SocialLinks",
    "SocialLinksError",
    "ProfileNotFoundError",
    "ProfileAlreadyExistsError",
    "InvalidProfileError",
    "ProfileIDExtractionError",
    "URLMismatchError",
]

