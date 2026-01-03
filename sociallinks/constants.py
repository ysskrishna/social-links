from typing import List, Dict, Any

# ----------------------------------------------------------------------
# Type Aliases
# ----------------------------------------------------------------------

PlatformEntry = List[Dict[str, Any]]
PlatformEntries = Dict[str, PlatformEntry]


# ----------------------------------------------------------------------
# Common ID regex patterns
# ----------------------------------------------------------------------

# Standard profile ID pattern: alphanumeric, underscore, period, hyphen
PROFILE_ID = r"(?P<id>[A-Za-z0-9_.-]+)"

# Profile ID with optional @ prefix (e.g., YouTube channels)
PROFILE_ID_AT = r"(?P<id>@?[A-Za-z0-9_.-]+)"

# Profile ID supporting Unicode characters (e.g., LinkedIn: peter-müller-81a8)
# Supports: Unicode letters, digits, underscore, ampersand, percent, apostrophe,
# en dash, registered trademark, period, hyphen
PROFILE_ID_UNICODE = r"(?P<id>[\w&%'–®\.-]+)"

# Extended profile ID supporting:
# - Optional negative prefix (Telegram groups)
# - @ symbol (Flickr)
# - Equals sign (Douyin base64)
# - Standard alphanumeric characters
PROFILE_ID_EXTENDED = r"(?P<id>-?[A-Za-z0-9_@=.\-]+)"

# Phone number pattern for WhatsApp (can optionally start with +)
PHONE_NUMBER = r"(?P<id>\+?[0-9]+)"

