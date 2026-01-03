from typing import List, Dict, Any

# ----------------------------------------------------------------------
# Type Aliases
# ----------------------------------------------------------------------

PlatformEntry = List[Dict[str, Any]]
"""Type alias for a platform entry, representing a list of dictionaries
containing platform-specific configuration data."""

PlatformEntries = Dict[str, PlatformEntry]
"""Type alias for platform entries, mapping platform names to their
respective PlatformEntry configurations."""


# ----------------------------------------------------------------------
# Common ID regex patterns
# ----------------------------------------------------------------------

PROFILE_ID = r"(?P<id>[A-Za-z0-9_.-]+)"
"""Standard profile ID pattern matching alphanumeric characters,
underscores, periods, and hyphens."""

PROFILE_ID_AT = r"(?P<id>@?[A-Za-z0-9_.-]+)"
"""Profile ID pattern with optional @ prefix (e.g., YouTube channels)."""

PROFILE_ID_UNICODE = r"(?P<id>[\w&%'–®\.-]+)"
"""Profile ID pattern supporting Unicode characters (e.g., LinkedIn: peter-müller-81a8).
Supports Unicode letters, digits, underscore, ampersand, percent, apostrophe,
en dash, registered trademark, period, and hyphen."""

PROFILE_ID_EXTENDED = r"(?P<id>-?[A-Za-z0-9_@=.\-]+)"
"""Extended profile ID pattern supporting:
- Optional negative prefix (Telegram groups)
- @ symbol (Flickr)
- Equals sign (Douyin base64)
- Standard alphanumeric characters
"""

PHONE_NUMBER = r"(?P<id>\+?[0-9]+)"
"""Phone number pattern for WhatsApp (can optionally start with +)."""

