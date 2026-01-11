---
title: Basic API

description: "Convenience functions for common operations. Simple, functional API for detecting platforms, validating URLs, and sanitizing URLs using a default SocialLinks instance."

keywords:
  - basic API
  - convenience functions
  - detect platform
  - validate URL
  - sanitize URL
  - social-links
  - Python library
---

# Basic API

Convenience functions for common operations using a default `SocialLinks` instance.

This module provides simple, functional API for common operations like detecting platforms, validating URLs, and sanitizing URLs. These functions use a default `SocialLinks` instance with predefined platforms.

For advanced usage (custom platforms, regex flags, platform management), use the [`SocialLinks` class](core-api.md) directly.

::: sociallinks.basic
    options:
      show_root_heading: true
      show_source: false
      heading_level: 3
      members:
        - detect_platform
        - is_valid
        - sanitize
        - list_platforms
      members_order: source

