# Social Links

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Tests](https://github.com/ysskrishna/social-links/actions/workflows/test.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
[![PyPI](https://img.shields.io/pypi/v/social-links)](https://pypi.org/project/social-links/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/social-links?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/social-links)
[![Documentation](https://img.shields.io/badge/docs-ysskrishna.github.io%2Fsocial--links-blue.svg)](https://ysskrishna.github.io/social-links/)
[![Interactive Demo](https://img.shields.io/badge/demo-Try%20it%20now!-green.svg)](https://ysskrishna.github.io/social-links/demo/)

A lightweight, zero-dependency Python library for detecting, validating, and sanitizing social media profile URLs. Supports 50+ platforms out of the box with automatic URL normalization, username extraction, and customizable regex patterns for extensibility.

> 🚀 **Try it interactively in your browser!** Test the library with our [Interactive Demo](https://ysskrishna.github.io/social-links/demo/) - no installation required.

![OG Image](https://raw.githubusercontent.com/ysskrishna/social-links/main/media/og.png)

## Features

- 🔍 **Auto-detect** social media platforms from URLs
- ✅ **Validate** URLs against specific platforms
- 🧹 **Sanitize** URLs to canonical format
- 🎯 **50+ predefined platforms** (LinkedIn, GitHub, Twitter/X, Facebook, Instagram, YouTube, and more)
- 🔧 **Customizable** - Add your own platforms with regex patterns
- 🚀 **Zero dependencies** - Pure Python, no external libraries

## Installation

```bash
pip install social-links
```

Or using `uv`:

```bash
uv pip install social-links
```

## Quick Start

```python
from sociallinks import detect_platform, sanitize, is_valid, list_platforms

# Detect platform from URL
platform = detect_platform("https://www.linkedin.com/in/ysskrishna/")
print(platform)  # "linkedin"

# Validate URL for a specific platform
is_valid_url = is_valid("linkedin", "https://www.linkedin.com/in/ysskrishna/")
print(is_valid_url)  # True

# Sanitize URL to canonical format
sanitized = sanitize("linkedin", "https://www.linkedin.com/in/ysskrishna/")
print(sanitized)  # "https://linkedin.com/in/ysskrishna"

# List all supported platforms
platforms = list_platforms()
print(f"Supported platforms: {len(platforms)}")  # Supported platforms: 50+
```

That's it! For most use cases, you don't need anything more. See [Basic Usage](#basic-usage) for more examples, or [Advanced Usage](#advanced-usage) if you need custom platforms or configurations.

## Supported Platforms

The library comes with 50+ predefined platforms:

| Predefined Platforms| | |
|---|---|---|
| [Apple Music](https://music.apple.com) | [Bandcamp](https://bandcamp.com) | [Behance](https://behance.net) |
| [Bluesky](https://bsky.app) | [Crunchbase](https://crunchbase.com) | [Dev.to](https://dev.to) |
| [Discord](https://discord.com) | [Douyin](https://douyin.com) | [Dribbble](https://dribbble.com) |
| [Etsy](https://etsy.com) | [Exercism](https://exercism.io) | [Facebook](https://facebook.com) |
| [Flickr](https://flickr.com) | [GitHub](https://github.com) | [GitLab](https://gitlab.com) |
| [Gravatar](https://gravatar.com) | [Gumroad](https://gumroad.com) | [Hacker News](https://news.ycombinator.com) |
| [Hashnode](https://hashnode.com) | [Instagram](https://instagram.com) | [Keybase](https://keybase.io) |
| [Kuaishou](https://kuaishou.com) | [Lemmy World](https://lemmy.world) | [LinkedIn](https://linkedin.com) (personal & company) |
| [Linktree](https://linktr.ee) | [Mastodon](https://mastodon.social) | [Medium](https://medium.com) |
| [Patreon](https://patreon.com) | [Pinterest](https://pinterest.com) | [Product Hunt](https://producthunt.com) |
| [Quora](https://quora.com) | [Reddit](https://reddit.com) | [Signal](https://signal.me) |
| [SlideShare](https://slideshare.net) | [Snapchat](https://snapchat.com) | [SoundCloud](https://soundcloud.com) |
| [Spotify](https://spotify.com) | [Stack Overflow](https://stackoverflow.com) | [Steam](https://steamcommunity.com) |
| [Substack](https://substack.com) | [Telegram](https://telegram.org) | [Threads](https://threads.net) |
| [TikTok](https://tiktok.com) | [Tumblr](https://tumblr.com) | [Twitch](https://twitch.tv) |
| [Vimeo](https://vimeo.com) | [VK](https://vk.com) | [WeChat](https://weixin.qq.com) |
| [Weibo](https://weibo.com) | [Wellfound (AngelList)](https://wellfound.com) | [WhatsApp](https://whatsapp.com) |
| [X (Twitter)](https://x.com) | [YouTube](https://youtube.com) | |

## Basic Usage

The simplest way to use social-links is with module-level functions. These work out of the box with 50+ predefined platforms - no configuration needed!

### Detect Platform

```python
from sociallinks import detect_platform

# Detect from full URL
detect_platform("https://github.com/ysskrishna")  # "github"
detect_platform("https://x.com/ysskrishna")      # "x"
detect_platform("https://example.com")           # None

# Works with various URL formats
detect_platform("http://linkedin.com/in/ysskrishna")
detect_platform("www.facebook.com/ysskrishna")
detect_platform("  https://instagram.com/ysskrishna  ")  # Handles whitespace
```

### Validate URLs

```python
from sociallinks import is_valid

# Validate against specific platform
is_valid("linkedin", "https://www.linkedin.com/in/ysskrishna/")  # True
is_valid("linkedin", "https://example.com")                   # False
is_valid("github", "https://github.com/ysskrishna")             # True
```

### Sanitize URLs

```python
from sociallinks import sanitize

# Normalize to canonical format
sanitize("linkedin", "https://www.linkedin.com/in/ysskrishna/")
# Returns: "https://linkedin.com/in/ysskrishna"

sanitize("github", "http://www.github.com/ysskrishna")
# Returns: "https://github.com/ysskrishna"

sanitize("x", "https://twitter.com/ysskrishna")
# Returns: "https://x.com/ysskrishna"
```

### List Platforms

```python
from sociallinks import list_platforms

# Get all available platforms
platforms = list_platforms()
# Returns: ["behance", "dev_to", "dribbble", "github", "linkedin", ...]
print(f"Supported platforms: {len(platforms)}")  # 50+
```

---

## Advanced Usage

For custom configurations, custom platforms, or platform management, use the `SocialLinks` class directly.

### Using the Class API

The class API provides the same methods as the module-level functions, but with more control:

```python
from sociallinks import SocialLinks

sl = SocialLinks()

# Same methods as module functions
sl.detect_platform("https://github.com/ysskrishna")  # "github"
sl.is_valid("linkedin", "https://linkedin.com/in/user")  # True
sl.sanitize("github", "https://github.com/user")  # "https://github.com/user"
sl.list_platforms()  # ["behance", "dev_to", ...]
```

> **Note:** You can configure the `SocialLinks` instance during initialization:
> - `use_predefined_platforms=False` - Start with an empty platform list (useful for custom platforms only)
> - `regex_flags=re.IGNORECASE | re.MULTILINE` - Configure regex compilation flags

### Custom Platforms

Add your own platform definitions with custom regex patterns. This is useful when you need to support platforms not included in the predefined list, or when you want to customize how existing platforms are detected and sanitized.

#### Platform Configuration Structure

A platform configuration is a **list of dictionaries**, where each dictionary defines URL patterns and a sanitization template. Multiple dictionaries allow different URL formats to be handled with potentially different sanitization templates (e.g., personal profiles vs. company pages).

```python
# Single dictionary with multiple patterns (same sanitization template)
custom_platform = [{
    "patterns": [
        r"https?://(www\.)?example\.com/(?P<id>[A-Za-z0-9_]+)/?$",
        r"https?://example\.com/user/(?P<id>[A-Za-z0-9_]+)/?$"
    ],
    "sanitized": "https://example.com/{id}"
}]

# Multiple dictionaries (different URL formats, same or different sanitization)
custom_platform = [
    {
        "patterns": [r"https?://example\.com/user/(?P<id>[A-Za-z0-9_]+)"],
        "sanitized": "https://example.com/user/{id}"
    },
    {
        "patterns": [r"https?://example\.com/u/(?P<id>[A-Za-z0-9_]+)"],
        "sanitized": "https://example.com/user/{id}"  # Normalize to same format
    }
]
```

**Configuration Fields:**

- **`patterns`** (list of strings): Regex patterns that match URLs for this platform. 
  - Use named groups like `(?P<id>...)` to capture identifiers (username, ID, etc.)
  - Multiple patterns allow matching different URL formats (e.g., with/without `www`, different URL paths)
  - **Pattern matching behavior:**
    - For `detect_platform()`: All patterns are checked (order-independent for detection result)
    - For `sanitize()`: Patterns are checked in order, and the **first matching pattern** is used for sanitization (order-dependent)

- **`sanitized`** (string): Template for the canonical URL format
    - Use `{id}` (or other named groups from patterns) as placeholders
    - This is the format URLs will be normalized to when using `sanitize()`

**Example Usage:**

```python
from sociallinks import SocialLinks

sl = SocialLinks(use_predefined_platforms=False)

# Example 1: Single dictionary with multiple patterns
custom_platform = [{
    "patterns": [
        r"https?://(www\.)?example\.com/(?P<id>[A-Za-z0-9_]+)/?$",
        r"https?://example\.com/user/(?P<id>[A-Za-z0-9_]+)/?$"
    ],
    "sanitized": "https://example.com/{id}"
}]

sl.set_platform("example", custom_platform)
sl.detect_platform("https://example.com/user123")  # "example"
sl.sanitize("example", "https://www.example.com/user123/")  # "https://example.com/user123"

# Example 2: Multiple dictionaries for different URL formats
platform_with_variants = [
    {
        "patterns": [r"https?://example\.com/user/(?P<id>[A-Za-z0-9_]+)"],
        "sanitized": "https://example.com/user/{id}"
    },
    {
        "patterns": [r"https?://example\.com/u/(?P<id>[A-Za-z0-9_]+)"],
        "sanitized": "https://example.com/user/{id}"  # Normalize /u/ to /user/
    }
]

sl.set_platform("example_v2", platform_with_variants)
sl.sanitize("example_v2", "https://example.com/u/johndoe")  # "https://example.com/user/johndoe"
```

**Viewing and Editing Existing Platforms:**

You can also view or modify existing platform configurations:

```python
from sociallinks import SocialLinks

sl = SocialLinks()

# Get existing platform configuration
github_config = sl.get_platform("github")
print(github_config)  # See the patterns and sanitized template

# Override an existing platform with custom configuration
custom_github = [{
    "patterns": [r"https?://github\.com/(?P<id>[A-Za-z0-9_]+)/?$"],
    "sanitized": "https://github.com/{id}"
}]
sl.set_platform("github", custom_github, override=True)
```

### Platform Management

Manage platforms programmatically:

```python
from sociallinks import SocialLinks

sl = SocialLinks()

# List all platforms
platforms = sl.list_platforms()
# Returns: ["behance", "dev_to", "dribbble", ...]

# Get platform configuration
config = sl.get_platform("github")

# Add a new platform (raises error if platform already exists)
custom_platform = [{
    "patterns": [r"https?://example.com/(?P<id>[A-Za-z0-9_]+)"],
    "sanitized": "https://example.com/{id}"
}]
sl.set_platform("example", custom_platform)

# Override an existing platform (including predefined ones)
sl.set_platform("github", custom_platform, override=True)

# Add multiple platforms at once
new_platforms = {
    "platform1": [{
        "patterns": [r"https?://example1.com/(?P<id>[A-Za-z0-9_]+)"],
        "sanitized": "https://example1.com/{id}"
    }],
    "platform2": [{
        "patterns": [r"https?://example2.com/(?P<id>[A-Za-z0-9_]+)"],
        "sanitized": "https://example2.com/{id}"
    }]
}
sl.set_platforms(new_platforms, override=False)  # Raises error if any exist
sl.set_platforms(new_platforms, override=True)   # Overrides existing platforms

# Delete platforms
sl.delete_platform("custom_platform")
sl.delete_platforms(["platform1", "platform2"])

# Clear all platforms
sl.clear_platforms()
```

## Changelog

See [CHANGELOG.md](https://github.com/ysskrishna/social-links/blob/main/CHANGELOG.md) for a detailed list of changes and version history.

## Roadmap

The following improvements are planned for upcoming releases:

- [ ] Add method to configure custom sanitization patterns
- [ ] Integrate development tools (flake8, black, isort) for code quality
- [ ] Add code coverage reporting with pytest-cov
- [ ] Refactor platform entries using dataclasses for better structure

## Contributing

Contributions are welcome! Please read our [Contributing Guide](https://github.com/ysskrishna/social-links/blob/main/CONTRIBUTING.md) for details on our code of conduct, development setup, and the process for submitting pull requests.

## Support

If you find this library useful, please consider:

- ⭐ **Starring** the repository on GitHub to help others discover it.

- 💖 **Sponsoring** to support ongoing maintenance and development.

[Become a Sponsor on GitHub](https://github.com/sponsors/ysskrishna) | [Support on Patreon](https://patreon.com/ysskrishna)

## Links

- **Documentation**: [ysskrishna.github.io/social-links](https://ysskrishna.github.io/social-links/)

- **Interactive Demo**: [ysskrishna.github.io/social-links/demo/](https://ysskrishna.github.io/social-links/demo/)

- **PyPI**: [pypi.org/project/social-links](https://pypi.org/project/social-links/)

- **Homepage**: [github.com/ysskrishna/social-links](https://github.com/ysskrishna/social-links)

- **Repository**: [github.com/ysskrishna/social-links.git](https://github.com/ysskrishna/social-links.git)

- **Issues**: [github.com/ysskrishna/social-links/issues](https://github.com/ysskrishna/social-links/issues)


## License

MIT License - see [LICENSE](https://github.com/ysskrishna/social-links/blob/main/LICENSE) file for details.

## Author

**Y. Siva Sai Krishna**

- GitHub: [@ysskrishna](https://github.com/ysskrishna)

- LinkedIn: [ysskrishna](https://linkedin.com/in/ysskrishna)
