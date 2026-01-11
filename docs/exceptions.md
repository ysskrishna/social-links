---
title: Exceptions

description: "Exception classes for the social-links library. Comprehensive error handling with detailed exception hierarchy for platform and URL operations."

keywords:
  - exceptions
  - error handling
  - platform errors
  - URL errors
  - social-links
  - Python library
---

# Exceptions

This page documents all custom exceptions used in the `social-links` library. All exceptions inherit from `SocialLinksError`, allowing you to catch all social-links related errors with a single exception handler.

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

