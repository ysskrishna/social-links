# API Reference

This page provides comprehensive documentation for all public APIs in the `social-links` library.


::: sociallinks.core.SocialLinks
    options:
      show_root_heading: true
      show_source: false
      heading_level: 3

::: sociallinks.constants
    options:
      show_root_heading: true
      show_source: false
      heading_level: 3
      members:
        - PlatformEntry
        - PlatformEntries
        - PROFILE_ID
        - PROFILE_ID_AT
        - PROFILE_ID_UNICODE
        - PROFILE_ID_EXTENDED
        - PHONE_NUMBER
      members_order: source

::: sociallinks.exceptions
    options:
      show_root_heading: true
      show_source: false
      heading_level: 3
      members:
        - SocialLinksError
        - PlatformError
        - PlatformNotFoundError
        - PlatformAlreadyExistsError
        - InvalidPlatformError
        - InvalidPlatformRegexError
        - URLParsingError
        - URLMismatchError
        - PlatformIDExtractionError
      members_order: source
