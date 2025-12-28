from typing import Dict, List, Any

# ----------------------------------------------------------------------
# Common ID regex
# ----------------------------------------------------------------------
PROFILE_ID = r"(?P<id>[A-Za-z0-9_.-]+)"
PROFILE_ID_AT = r"(?P<id>@?[A-Za-z0-9_.-]+)" #Youtube channel links can be with or without @
PROFILE_ID_UNICODE = r"(?P<id>[\w&%'–®\.-]+)" #LinkedIn profile IDs can contain Unicode characters (e.g., ü in peter-müller-81a8), ampersand, apostrophe, en dash, and registered trademark. \w matches Unicode letters, digits, and underscore
PHONE_NUMBER = r"(?P<id>\+?[0-9]+)" #Phone numbers for WhatsApp, can optionally start with +

# ----------------------------------------------------------------------
# Predefined platforms
# ----------------------------------------------------------------------
PREDEFINED_PLATFORMS: Dict[str, List[Dict[str, Any]]] = {
    "behance": [
        {
            "patterns": [
                rf"https?://(www\.)?behance\.net/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://behance.net/{id}"
        }
    ],
    "dev_to": [
        {
            "patterns": [
                rf"https?://(www\.)?dev\.to/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://dev.to/{id}"
        }
    ],
    "dribbble": [
        {
            "patterns": [
                rf"https?://(www\.)?dribbble\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://dribbble.com/{id}"
        }
    ],
    "exercism": [
        {
            "patterns": [
                rf"https?://(www\.)?exercism\.io/profiles/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://exercism.io/profiles/{id}"
        }
    ],
    "facebook": [
        {
            "patterns": [
                rf"https?://(www\.)?facebook\.com/{PROFILE_ID}/?$",
                rf"https?://m\.facebook\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://facebook.com/{id}"
        }
    ],
    "github": [
        {
            "patterns": [
                rf"https?://(www\.)?github\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://github.com/{id}"
        }
    ],
    "instagram": [
        {
            "patterns": [
                rf"https?://(www\.)?instagram\.com/{PROFILE_ID}/?$",
                rf"https?://m\.instagram\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://instagram.com/{id}"
        }
    ],
    "keybase": [
        {
            "patterns": [
                rf"https?://(www\.)?keybase\.io/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://keybase.io/{id}"
        }
    ],
    "lemmy_world": [
        {
            "patterns": [
                rf"https?://lemmy\.world/u/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://lemmy.world/u/{id}"
        }
    ],
    "linkedin": [
        {
            "patterns": [
                # LinkedIn profile IDs can contain Unicode characters (e.g., ü in peter-müller-81a8)
                rf"https?://([a-z]{{2,3}}\.)?linkedin\.com/in/{PROFILE_ID_UNICODE}/?$",
                rf"https?://([a-z]{{2,3}}\.)?linkedin\.com/mwlite/in/{PROFILE_ID_UNICODE}/?$",
                rf"^{PROFILE_ID_UNICODE}$"
            ],
            "sanitized": "https://linkedin.com/in/{id}"
        },
        {
            "patterns": [
                rf"https?://(www\.)?linkedin\.com/company/{PROFILE_ID_UNICODE}/?$"
            ],
            "sanitized": "https://linkedin.com/company/{id}"
        }
    ],
    "linktree": [
        {
            "patterns": [
                rf"https?://(www\.)?linktr\.ee/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://linktr.ee/{id}"
        }
    ],
    "mastodon": [
        {
            "patterns": [
                rf"https?://(www\.)?mastodon\.social/@{PROFILE_ID}/?$",
                rf"https?://(www\.)?mstdn\.social/@{PROFILE_ID}/?$",
                rf"https?://(www\.)?mastodon\.world/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://mastodon.social/@{id}"
        }
    ],
    "medium": [
        {
            "patterns": [
                rf"https?://(www\.)?medium\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://medium.com/@{id}"
        }
    ],
    "patreon": [
        {
            "patterns": [
                rf"https?://(www\.)?patreon\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://patreon.com/{id}"
        }
    ],
    "pinterest": [
        {
            "patterns": [
                rf"https?://([a-z]{{1,3}}\.)?pinterest\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://pinterest.com/{id}"
        }
    ],
    "reddit": [
        {
            "patterns": [
                rf"https?://(www\.)?reddit\.com/user/{PROFILE_ID}/?$",
                rf"https?://(www\.)?reddit\.com/u/{PROFILE_ID}/?$",
                rf"https?://old\.reddit\.com/user/{PROFILE_ID}/?$",
                rf"https?://old\.reddit\.com/u/{PROFILE_ID}/?$",
                rf"^u/{PROFILE_ID}$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://reddit.com/user/{id}"
        }
    ],
    "snapchat": [
        {
            "patterns": [
                rf"https?://(www\.)?snapchat\.com/add/{PROFILE_ID}/?$",
                rf"https?://(www\.)?snapchat\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://snapchat.com/@{id}"
        }
    ],
    "apple_music": [
        {
            "patterns": [
                rf"https?://(?:itunes|music)\.apple\.com/(?:[a-z]{{2}}/)?artist/(?:[A-Za-z0-9_\-\%\.]+/)?(?:id)?(?P<id>\d+)/?$",
                rf"https?://(?:itunes|music)\.apple\.com/(?:[a-z]{{2}}/)?artist/(?P<id>\d+)/?$",
                rf"^(?P<id>\d+)$"
            ],
            "sanitized": "https://music.apple.com/artist/{id}"
        }
    ],
    "soundcloud": [
        {
            "patterns": [
                rf"https?://(www\.)?soundcloud\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://soundcloud.com/{id}"
        }
    ],
    "spotify": [
        {
            "patterns": [
                rf"https?://(open\.)?spotify\.com/artist/{PROFILE_ID}/?$",
                rf"^spotify:artist:{PROFILE_ID}$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://open.spotify.com/artist/{id}"
        }
    ],
    "stackoverflow": [
        {
            "patterns": [
                rf"https?://(www\.)?stackoverflow\.com/users/{PROFILE_ID}(/[A-Za-z0-9_\\-\\.]+)?/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://stackoverflow.com/users/{id}"
        }
    ],
    "substack": [
        {
            "patterns": [
                rf"https?://{PROFILE_ID}\.substack\.com/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://{id}.substack.com"
        }
    ],
    "telegram": [
        {
            "patterns": [
                rf"https?://(www\.)?(t\.me|telegram\.me)/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://t.me/{id}"
        }
    ],
    "tiktok": [
        {
            "patterns": [
                rf"https?://(www\.)?tiktok\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://tiktok.com/@{id}"
        }
    ],
    "tumblr": [
        {
            "patterns": [
                rf"https?://{PROFILE_ID}\.tumblr\.com/?$",
                rf"https?://(www\.)?tumblr\.com/blog/{PROFILE_ID}/?$",
                rf"https?://(www\.)?tumblr\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://tumblr.com/{id}"
        }
    ],
    "twitch": [
        {
            "patterns": [
                rf"https?://(www\.)?twitch\.tv/{PROFILE_ID}/?$",
                rf"https?://m\.twitch\.tv/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://twitch.tv/{id}"
        }
    ],
    "vk": [
        {
            "patterns": [
                rf"https?://(www\.)?vk\.com/{PROFILE_ID}/?$",
                rf"https?://m\.vk\.com/@?{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://vk.com/{id}"
        }
    ],
    "vimeo": [
        {
            "patterns": [
                rf"https?://(www\.)?vimeo\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://vimeo.com/{id}"
        }
    ],
    "whatsapp": [
        {
            "patterns": [
                rf"https?://(www\.)?wa\.me/{PHONE_NUMBER}/?$",
                rf"https?://(www\.)?whatsapp\.com/send\?phone={PHONE_NUMBER}/?$",
                rf"^{PHONE_NUMBER}$"
            ],
            "sanitized": "https://wa.me/{id}"
        }
    ],
    "x": [
        {
            "patterns": [
                rf"https?://(www\.)?twitter\.com/@?{PROFILE_ID}/?$",
                rf"https?://mobile\.twitter\.com/@?{PROFILE_ID}/?$",
                rf"https?://x\.com/@?{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://x.com/{id}"
        }
    ],
    "youtube": [
        {
            "patterns": [
                rf"https?://(www\.)?youtube\.com/{PROFILE_ID_AT}/?$",
                rf"https?://(www\.)?youtube\.com/channel/{PROFILE_ID}/?$",
                rf"https?://(www\.)?youtube\.com/user/{PROFILE_ID}/?$",
                rf"https?://(www\.)?youtube\.com/c/{PROFILE_ID}/?$",
                rf"https?://m\.youtube\.com/c/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID_AT}$"
            ],
            "sanitized": "https://youtube.com/{id}"
        }
    ]
}
