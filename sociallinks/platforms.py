from typing import Dict, List, Any

PREDEFINED_PLATFORMS: Dict[str, List[Dict[str, Any]]] = {
    "behance": [
        {
            "patterns": [
                "https?://(www\\.)?behance\\.net/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://behance.net/{id}"
        }
    ],
    "dev_to": [
        {
            "patterns": [
                "https?://(www\\.)?dev\\.to/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://dev.to/{id}"
        }
    ],
    "dribbble": [
        {
            "patterns": [
                "https?://(www\\.)?dribbble\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://dribbble.com/{id}"
        }
    ],
    "exercism": [
        {
            "patterns": [
                "https?://(www\\.)?exercism\\.io/profiles/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://exercism.io/profiles/{id}"
        }
    ],
    "facebook": [
        {
            "patterns": [
                "https?://(www\\.)?facebook\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://m\\.facebook\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://facebook.com/{id}"
        }
    ],
    "github": [
        {
            "patterns": [
                "https?://(www\\.)?github\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://github.com/{id}"
        }
    ],
    "instagram": [
        {
            "patterns": [
                "https?://(www\\.)?instagram\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://m\\.instagram\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://instagram.com/{id}"
        }
    ],
    "keybase": [
        {
            "patterns": [
                "https?://(www\\.)?keybase\\.io/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://keybase.io/{id}"
        }
    ],
    "lemmy_world": [
        {
            "patterns": [
                "https?://lemmy\\.world/u/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://lemmy.world/u/{id}"
        }
    ],
    "linkedin": [
        {
            "patterns": [
                "https?://([a-z]{2,3}\\.)?linkedin\\.com/in/(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://([a-z]{2,3}\\.)?linkedin\\.com/mwlite/in/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://linkedin.com/in/{id}"
        },
        {
            "patterns": [
                "https?://(www\\.)?linkedin\\.com/company/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://www.linkedin.com/company/{id}/"
        }
    ],
    "linktree": [
        {
            "patterns": [
                "https?://(www\\.)?linktr\\.ee/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://linktr.ee/{id}"
        }
    ],
    "mastodon": [
        {
            "patterns": [
                "https?://(www\\.)?mastodon\\.social/@(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://(www\\.)?mstdn\\.social/@(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://(www\\.)?mastodon\\.world/@(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://mastodon.social/@{id}"
        }
    ],
    "medium": [
        {
            "patterns": [
                "https?://(www\\.)?medium\\.com/@(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://medium.com/@{id}"
        }
    ],
    "patreon": [
        {
            "patterns": [
                "https?://(www\\.)?patreon\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://patreon.com/{id}"
        }
    ],
    "pinterest": [
        {
            "patterns": [
                "https?://([a-z]{1,3}\\.)?pinterest\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://pinterest.com/{id}"
        }
    ],
    "soundcloud": [
        {
            "patterns": [
                "https?://(www\\.)?soundcloud\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://soundcloud.com/{id}"
        }
    ],
    "spotify": [
        {
            "patterns": [
                "https?://(open\\.)?spotify\\.com/artist/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://open.spotify.com/artist/{id}"
        }
    ],
    "stackoverflow": [
        {
            "patterns": [
                "https?://(www\\.)?stackoverflow\\.com/users/(?P<id>[A-Za-z0-9_.-]+)(/[A-Za-z0-9_\\-\\.]+)?/?$"
            ],
            "sanitized": "https://stackoverflow.com/users/{id}"
        }
    ],
    "substack": [
        {
            "patterns": [
                "https?://(?P<id>[A-Za-z0-9_.-]+)\\.substack\\.com/?$"
            ],
            "sanitized": "https://{id}.substack.com"
        }
    ],
    "telegram": [
        {
            "patterns": [
                "https?://(www\\.)?(t\\.me|telegram\\.me)/(?P<id>[a-z0-9_]{5,32})/?$"
            ],
            "sanitized": "https://t.me/{id}"
        }
    ],
    "tiktok": [
        {
            "patterns": [
                "https?://(www\\.)?tiktok\\.com/@(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://tiktok.com/@{id}"
        }
    ],
    "twitch": [
        {
            "patterns": [
                "https?://(www\\.)?twitch\\.tv/(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://m\\.twitch\\.tv/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://twitch.tv/{id}"
        }
    ],
    "vk": [
        {
            "patterns": [
                "https?://(www\\.)?vk\\.com/(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://m\\.vk\\.com/@?(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://vk.com/{id}"
        }
    ],
    "x": [
        {
            "patterns": [
                "https?://(www\\.)?twitter\\.com/@?(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://mobile\\.twitter\\.com/@?(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://x\\.com/@?(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://x.com/{id}"
        }
    ],
    "youtube": [
        {
            "patterns": [
                "https?://(www\\.)?youtube\\.com/@?(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://(www\\.)?youtube\\.com/channel/(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://(www\\.)?youtube\\.com/user/(?P<id>[A-Za-z0-9_.-]+)/?$",
                "https?://m\\.youtube\\.com/c/(?P<id>[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://youtube.com/@{id}"
        }
    ]
}
