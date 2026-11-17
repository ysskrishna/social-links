from sociallinks.constants import (
    PROFILE_ID,
    PROFILE_ID_AT,
    PROFILE_ID_UNICODE,
    PROFILE_ID_EXTENDED,
    PHONE_NUMBER,
    NUMERIC_ID,
    NOSTR_NPUB,
    ORCID_ID,
    HEX32_ID,
    PlatformEntries,
)

# ----------------------------------------------------------------------
# Predefined platforms
# ----------------------------------------------------------------------
PREDEFINED_PLATFORMS: PlatformEntries = {
    "behance": [
        {
            "patterns": [
                rf"https?://(www\.)?behance\.net/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://behance.net/{id}"
        }
    ],
    "bluesky": [
        {
            "patterns": [
                rf"https?://(www\.)?bsky\.app/profile/{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://bsky.app/profile/{id}"
        }
    ],
    "crunchbase": [
        {
            "patterns": [
                rf"https?://(www\.)?crunchbase\.com/organization/{PROFILE_ID}/?$",
                rf"https?://(www\.)?crunchbase\.com/company/{PROFILE_ID}/?$",
            ],
            "sanitized": "https://www.crunchbase.com/organization/{id}"
        },
        {
            "patterns": [
                rf"https?://(www\.)?crunchbase\.com/person/{PROFILE_ID}/?$",
            ],
            "sanitized": "https://www.crunchbase.com/person/{id}"
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
    "discord": [
        {
            "patterns": [
                rf"https?://(www\.)?discord\.gg/{PROFILE_ID}/?$",
                rf"https?://(www\.)?discord\.com/invite/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://discord.gg/{id}"
        }
    ],
    "douyin": [
        {
            "patterns": [
                rf"https?://(www\.)?douyin\.com/user/{PROFILE_ID_EXTENDED}/?$",
                rf"^{PROFILE_ID_EXTENDED}$"
            ],
            "sanitized": "https://www.douyin.com/user/{id}"
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
    "etsy": [
        {
            "patterns": [
                rf"https?://(www\.)?etsy\.com/shop/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://etsy.com/shop/{id}"
        }
    ],
    "exercism": [
        {
            "patterns": [
                rf"https?://(www\.)?exercism\.(org|io)/profiles/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://exercism.org/profiles/{id}"
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
        },
        {
            # Accounts without a vanity name: facebook.com/profile.php?id=<digits>
            "patterns": [
                r"https?://(www\.|m\.)?facebook\.com/profile\.php\?id=(?P<id>\d+)(?:[&#].*)?$"
            ],
            "sanitized": "https://facebook.com/profile.php?id={id}"
        }
    ],
    "flickr": [
        {
            "patterns": [
                rf"https?://(www\.)?flickr\.com/people/{PROFILE_ID_EXTENDED}/?$",
                rf"^{PROFILE_ID_EXTENDED}$"
            ],
            "sanitized": "https://www.flickr.com/people/{id}"
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
    "gitlab": [
        {
            "patterns": [
                rf"https?://(www\.)?gitlab\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://gitlab.com/{id}"
        }
    ],
    "gravatar": [
        {
            "patterns": [
                rf"https?://([a-z]{{2,3}}\.)?gravatar\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://gravatar.com/{id}"
        }
    ],
    "hackernews": [
        {
            "patterns": [
                rf"https?://(www\.)?news\.ycombinator\.com/user\?id={PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://news.ycombinator.com/user?id={id}"
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
    "kuaishou": [
        {
            "patterns": [
                rf"https?://(www\.)?kuaishou\.com/profile/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.kuaishou.com/profile/{id}"
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
                
                rf"https?://(www\.)?linkedin\.com/company/{PROFILE_ID_UNICODE}/?$",
                rf"https?://(www\.)?linkedin\.com/school/{PROFILE_ID_UNICODE}/?$",
            ],
            "sanitized": "https://linkedin.com/company/{id}"
        }
    ],
    "wellfound": [
        {
            "patterns": [
                rf"https?://(www\.)?wellfound\.com/u/{PROFILE_ID}/?$",
                rf"https?://(www\.)?angel\.co/u/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://wellfound.com/u/{id}"
        },
        {
            "patterns": [
                rf"https?://(www\.)?wellfound\.com/company/{PROFILE_ID}/?$",
                rf"https?://(www\.)?angel\.co/company/{PROFILE_ID}/?$",
                rf"https?://(www\.)?angel\.co/{PROFILE_ID}/?$"
            ],
            "sanitized": "https://wellfound.com/company/{id}"
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
                # Profile subdomain: <name>.medium.com (not Medium's own hosts)
                r"https?://(?!(?:www|help|blog|policy|api|miro|cdn-images-1)\.)(?P<id>[A-Za-z0-9_-]+)\.medium\.com/?$",
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
    "quora": [
        {
            "patterns": [
                rf"https?://(www\.)?quora\.com/profile/{PROFILE_ID_UNICODE}/?$",
                rf"https?://(www\.)?quora\.com/{PROFILE_ID_UNICODE}/?$",
                rf"^{PROFILE_ID_UNICODE}$"
            ],
            "sanitized": "https://quora.com/profile/{id}"
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
        },
        {
            "patterns": [
                rf"https?://(www\.)?reddit\.com/r/{PROFILE_ID}/?$",
                rf"https?://old\.reddit\.com/r/{PROFILE_ID}/?$",
                rf"^r/{PROFILE_ID}$"
            ],
            "sanitized": "https://reddit.com/r/{id}"
        }
    ],
    "signal": [
        {
            "patterns": [
                # Phone-number links look like signal.me/#p/+15555555555
                r"https?://(www\.)?signal\.me/#p/(?P<id>\+?[A-Za-z0-9_.-]+)/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://signal.me/#p/{id}"
        }
    ],
    "slideshare": [
        {
            "patterns": [
                rf"https?://(www\.)?slideshare\.net/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.slideshare.net/{id}"
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
                r"https?://(?:itunes|music)\.apple\.com/(?:[a-z]{2}/)?artist/(?:[A-Za-z0-9_\-\%\.]+/)?(?:id)?(?P<id>\d+)/?$",
                r"https?://(?:itunes|music)\.apple\.com/(?:[a-z]{2}/)?artist/(?P<id>\d+)/?$",
                r"^(?P<id>\d+)$"
            ],
            "sanitized": "https://music.apple.com/artist/{id}"
        }
    ],
    "bandcamp": [
        {
            "patterns": [
                rf"https?://{PROFILE_ID}\.bandcamp\.com/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://{id}.bandcamp.com"
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
        },
        {
            "patterns": [
                rf"https?://(open\.)?spotify\.com/user/{PROFILE_ID}/?$"
            ],
            "sanitized": "https://open.spotify.com/user/{id}"
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
    "steam": [
        {
            "patterns": [
                rf"https?://(www\.)?steamcommunity\.com/id/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://steamcommunity.com/id/{id}"
        },
        {
            "patterns": [
                rf"https?://(www\.)?steamcommunity\.com/profiles/{PROFILE_ID}/?$"
            ],
            "sanitized": "https://steamcommunity.com/profiles/{id}"
        }
    ],
    "substack": [
        {
            "patterns": [
                rf"https?://{PROFILE_ID}\.substack\.com/?$",
                rf"https?://(www\.)?substack\.com/@{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://substack.com/@{id}"
        }
    ],
    "telegram": [
        {
            "patterns": [
                rf"https?://(www\.)?(t\.me|telegram\.me|telegram\.dog)/{PROFILE_ID_EXTENDED}/?$",
                rf"https?://(www\.)?web\.telegram\.org/[ak]/#@?{PROFILE_ID_EXTENDED}/?$",
                rf"^{PROFILE_ID_EXTENDED}$"
            ],
            "sanitized": "https://t.me/{id}"
        }
    ],
    "threads": [
        {
            "patterns": [
                rf"https?://(www\.)?threads\.(com|net)/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://threads.com/@{id}"
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
    "wechat": [
        {
            "patterns": [
                rf"https?://open\.weixin\.qq\.com/qr/code\?username={PROFILE_ID}$",
                rf"weixin://dl/chat\?{PROFILE_ID}$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://open.weixin.qq.com/qr/code?username={id}"
        }
    ],
    "weibo": [
        {
            "patterns": [
                rf"https?://(www\.)?weibo\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://weibo.com/{id}"
        },
        {
            "patterns": [
                rf"https?://(www\.)?weibo\.com/u/{PROFILE_ID}/?$"
            ],
            "sanitized": "https://weibo.com/u/{id}"
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
                rf"https?://(www\.)?youtube\.com/user/{PROFILE_ID}/?$",
                rf"https?://(www\.)?youtube\.com/c/{PROFILE_ID}/?$",
                rf"https?://m\.youtube\.com/c/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID_AT}$"
            ],
            "sanitized": "https://youtube.com/{id}"
        },
        {
            # Channel IDs (UC...) only resolve under /channel/, unlike handles,
            # /user/ and /c/ names which resolve at the root.
            "patterns": [
                rf"https?://(www\.)?youtube\.com/channel/{PROFILE_ID}/?$"
            ],
            "sanitized": "https://youtube.com/channel/{id}"
        }
    ],
    "producthunt": [
        {
            "patterns": [
                rf"https?://(www\.)?producthunt\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://www.producthunt.com/@{id}"
        }
    ],
    "gumroad": [
        {
            "patterns": [
                rf"https?://{PROFILE_ID}\.gumroad\.com/?$",
                rf"https?://(www\.)?gumroad\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://gumroad.com/{id}"
        }
    ],
    "hashnode": [
        {
            "patterns": [
                rf"https?://(www\.)?hashnode\.com/@{PROFILE_ID}/?$",
                rf"https?://{PROFILE_ID}\.hashnode\.dev/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://hashnode.com/@{id}"
        }
    ],
    "leetcode": [
        {
            "patterns": [
                rf"https?://(www\.)?leetcode\.com/{PROFILE_ID}/?$",
                rf"https?://(www\.)?leetcode\.com/u/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://leetcode.com/{id}"
        }
    ],
    "hackerrank": [
        {
            "patterns": [
                rf"https?://(www\.)?hackerrank\.com/profile/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.hackerrank.com/profile/{id}"
        }
    ],
    "codepen": [
        {
            "patterns": [
                rf"https?://(www\.)?codepen\.io/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://codepen.io/{id}"
        }
    ],
    "kaggle": [
        {
            "patterns": [
                rf"https?://(www\.)?kaggle\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.kaggle.com/{id}"
        }
    ],
    "pypi": [
        {
            "patterns": [
                rf"https?://(www\.)?pypi\.org/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://pypi.org/user/{id}"
        }
    ],
    "dockerhub": [
        {
            "patterns": [
                rf"https?://(www\.)?hub\.docker\.com/u/{PROFILE_ID}/?$",
                rf"https?://(www\.)?docker\.com/u/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://hub.docker.com/u/{id}"
        }
    ],
    "replit": [
        {
            "patterns": [
                rf"https?://(www\.)?replit\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://replit.com/@{id}"
        }
    ],
    "unsplash": [
        {
            "patterns": [
                rf"https?://(www\.)?unsplash\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://unsplash.com/@{id}"
        }
    ],
    "fiverr": [
        {
            "patterns": [
                rf"https?://(www\.)?fiverr\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.fiverr.com/{id}"
        }
    ],
    "wordpress": [
        {
            "patterns": [
                rf"https?://(www\.)?wordpress\.com/people/{PROFILE_ID}/?$",
                rf"https?://{PROFILE_ID}\.wordpress\.com/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://wordpress.com/people/{id}"
        }
    ],
    "artstation": [
        {
            "patterns": [
                rf"https?://(www\.)?artstation\.com/{PROFILE_ID}/?$",
                rf"https?://{PROFILE_ID}\.artstation\.com/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.artstation.com/{id}"
        }
    ],
    "chess_com": [
        {
            "patterns": [
                rf"https?://(www\.)?chess\.com/member/{PROFILE_ID}/?$",
                rf"https?://(www\.)?chess\.com/play/online/new\?opponent={PROFILE_ID}$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.chess.com/member/{id}"
        }
    ],
    "lichess": [
        {
            "patterns": [
                rf"https?://(www\.)?lichess\.org/@/{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://lichess.org/@/{id}"
        }
    ],
    "dailymotion": [
        {
            "patterns": [
                rf"https?://(www\.)?dailymotion\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.dailymotion.com/{id}"
        }
    ],
    "rumble": [
        {
            "patterns": [
                rf"https?://(www\.)?rumble\.com/user/{PROFILE_ID}/?$",
                rf"https?://(www\.)?rumble\.com/c/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://rumble.com/user/{id}"
        }
    ],
    "trello": [
        {
            "patterns": [
                rf"https?://(www\.)?trello\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://trello.com/{id}"
        }
    ],
    "huggingface": [
        {
            "patterns": [
                rf"https?://(www\.)?huggingface\.co/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://huggingface.co/{id}"
        }
    ],
    "replicate": [
        {
            "patterns": [
                rf"https?://(www\.)?replicate\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://replicate.com/{id}"
        }
    ],
    "clawhub": [
        {
            "patterns": [
                rf"https?://(www\.)?clawhub\.ai/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://clawhub.ai/{id}"
        }
    ],
    "lobsters": [
        {
            "patterns": [
                rf"https?://lobste\.rs/~{PROFILE_ID}/?$",
                rf"https?://lobste\.rs/u/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://lobste.rs/~{id}"
        }
    ],
    "atcoder": [
        {
            "patterns": [
                rf"https?://(www\.)?atcoder\.jp/users/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://atcoder.jp/users/{id}"
        }
    ],
    "codechef": [
        {
            "patterns": [
                rf"https?://(www\.)?codechef\.com/users/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.codechef.com/users/{id}"
        }
    ],
    "topcoder": [
        {
            "patterns": [
                rf"https?://profiles\.topcoder\.com/{PROFILE_ID}/?$",
                rf"https?://(www\.)?topcoder\.com/members/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://profiles.topcoder.com/{id}"
        }
    ],
    "tryhackme": [
        {
            "patterns": [
                rf"https?://(www\.)?tryhackme\.com/p/{PROFILE_ID_UNICODE}/?$",
                rf"https?://(www\.)?tryhackme\.com/r/p/{PROFILE_ID_UNICODE}/?$",
                rf"^{PROFILE_ID_UNICODE}$"
            ],
            "sanitized": "https://tryhackme.com/p/{id}"
        }
    ],
    "qiita": [
        {
            "patterns": [
                rf"https?://(www\.)?qiita\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://qiita.com/{id}"
        }
    ],
    "habr": [
        {
            "patterns": [
                rf"https?://(www\.)?habr\.com/(?:(?:en|ru)/)?users/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://habr.com/users/{id}"
        }
    ],
    "zenn": [
        {
            "patterns": [
                rf"https?://(www\.)?zenn\.dev/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://zenn.dev/{id}"
        }
    ],
    "rubygems": [
        {
            "patterns": [
                rf"https?://(www\.)?rubygems\.org/profiles/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://rubygems.org/profiles/{id}"
        }
    ],
    "nuget": [
        {
            "patterns": [
                rf"https?://(www\.)?nuget\.org/profiles/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.nuget.org/profiles/{id}"
        }
    ],
    "sourceforge": [
        {
            "patterns": [
                rf"https?://(www\.)?sourceforge\.net/u/{PROFILE_ID}(?:/profile)?/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://sourceforge.net/u/{id}/profile"
        }
    ],
    "sourcehut": [
        {
            "patterns": [
                rf"https?://((git|hg|todo|lists|man|builds|paste|meta)\.)?sr\.ht/~{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://sr.ht/~{id}"
        }
    ],
    "stack_exchange": [
        {
            "patterns": [
                rf"https?://(www\.)?stackexchange\.com/users/{NUMERIC_ID}(?:/[^/?#]+)?/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://stackexchange.com/users/{id}"
        }
    ],
    "google_scholar": [
        {
            "patterns": [
                rf"https?://scholar\.google\.(?:com|[a-z][a-z]|co\.[a-z][a-z]|com\.[a-z][a-z])/citations\?(?:[^#]*&)?user={PROFILE_ID}(?:[&#].*)?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://scholar.google.com/citations?user={id}"
        }
    ],
    "kick": [
        {
            "patterns": [
                rf"https?://(www\.)?kick\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://kick.com/{id}"
        }
    ],
    "stan_store": [
        {
            "patterns": [
                rf"https?://(www\.)?stan\.store/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://stan.store/{id}"
        }
    ],
    "farcaster": [
        {
            "patterns": [
                rf"https?://(www\.)?(?:farcaster\.xyz|warpcast\.com)/{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://farcaster.xyz/{id}"
        }
    ],
    "figma": [
        {
            "patterns": [
                rf"https?://(www\.)?figma\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://www.figma.com/@{id}"
        }
    ],
    "douban": [
        {
            "patterns": [
                rf"https?://(www\.)?douban\.com/people/{PROFILE_ID}/?$",
                rf"https?://m\.douban\.com/people/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.douban.com/people/{id}"
        }
    ],
    "topmate": [
        {
            "patterns": [
                rf"https?://(www\.)?topmate\.io/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://topmate.io/{id}"
        }
    ],
    "freelancer": [
        {
            "patterns": [
                rf"https?://(www\.)?freelancer\.(?:com|in|ca|de|es|fr|ie|ph|pk|sg|hk|my|mx|cl|co\.uk|com\.au|co\.nz|co\.za|co\.id|com\.bd|com\.jm|com\.ar|com\.pe)/u/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.freelancer.com/u/{id}"
        }
    ],
    "ebay": [
        {
            "patterns": [
                rf"https?://(www\.)?(?:m\.)?ebay\.(?:com|ca|de|fr|it|es|ie|at|ch|nl|be|pl|ph|co\.uk|com\.au|com\.sg|com\.my|com\.hk)/usr/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.ebay.com/usr/{id}"
        }
    ],
    "poshmark": [
        {
            "patterns": [
                rf"https?://(www\.)?poshmark\.(?:com|ca)/closet/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://poshmark.com/closet/{id}"
        }
    ],
    "civitai": [
        {
            "patterns": [
                rf"https?://(www\.)?civitai\.com/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://civitai.com/user/{id}"
        }
    ],
    "opensea": [
        {
            "patterns": [
                rf"https?://(www\.)?opensea\.io/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://opensea.io/{id}"
        }
    ],
    "hey_xyz": [
        {
            "patterns": [
                rf"https?://(www\.)?hey\.xyz/u/{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://hey.xyz/u/{id}"
        }
    ],
    "primal": [
        {
            "patterns": [
                rf"https?://(www\.)?primal\.net/p/{NOSTR_NPUB}/?$",
                r"https?://(www\.)?primal\.net/p/(?P<id>[0-9a-fA-F]{64})/?$",
                rf"^{NOSTR_NPUB}$"
            ],
            "sanitized": "https://primal.net/p/{id}"
        }
    ],
    "openstreetmap": [
        {
            "patterns": [
                rf"https?://(www\.)?openstreetmap\.org/user/{PROFILE_ID_UNICODE}/?$",
                rf"^{PROFILE_ID_UNICODE}$"
            ],
            "sanitized": "https://www.openstreetmap.org/user/{id}"
        }
    ],
    "pixelfed": [
        {
            "patterns": [
                rf"https?://(www\.)?pixelfed\.social/@{PROFILE_ID}/?$",
                rf"https?://(www\.)?pixelfed\.social/{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://pixelfed.social/{id}"
        }
    ],
    "misskey": [
        {
            "patterns": [
                rf"https?://(www\.)?misskey\.io/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://misskey.io/@{id}"
        }
    ],
    "bilibili": [
        {
            "patterns": [
                rf"https?://space\.bilibili\.com/(?:en/)?{NUMERIC_ID}/?$",
                rf"https?://m\.bilibili\.com/space/{NUMERIC_ID}/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://space.bilibili.com/{id}"
        }
    ],
    "letterboxd": [
        {
            "patterns": [
                rf"https?://(www\.)?letterboxd\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://letterboxd.com/{id}"
        }
    ],
    "goodreads": [
        {
            "patterns": [
                rf"https?://(www\.)?goodreads\.com/user/show/{NUMERIC_ID}(?:-[^/?#]*)?/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://www.goodreads.com/user/show/{id}"
        }
    ],
    "scratch": [
        {
            "patterns": [
                rf"https?://(www\.)?scratch\.mit\.edu/users/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://scratch.mit.edu/users/{id}"
        }
    ],
    "discogs": [
        {
            "patterns": [
                rf"https?://(www\.)?discogs\.com/(?:[a-z][a-z]/)?user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.discogs.com/user/{id}"
        }
    ],
    "myanimelist": [
        {
            "patterns": [
                rf"https?://(www\.)?myanimelist\.net/profile/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://myanimelist.net/profile/{id}"
        }
    ],
    "osu": [
        {
            "patterns": [
                rf"https?://osu\.ppy\.sh/(?:users|u)/{PROFILE_ID_UNICODE}(?:/(?:osu|taiko|fruits|mania))?/?$",
                rf"^{PROFILE_ID_UNICODE}$"
            ],
            "sanitized": "https://osu.ppy.sh/users/{id}"
        }
    ],
    "itch_io": [
        {
            "patterns": [
                rf"https?://(www\.)?itch\.io/profile/{PROFILE_ID}/?$",
                r"https?://(?!www\.)(?P<id>[A-Za-z0-9-]+)\.itch\.io/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://itch.io/profile/{id}"
        }
    ],
    "speedrun": [
        {
            "patterns": [
                rf"https?://(www\.)?speedrun\.com/(?:users|user)/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.speedrun.com/users/{id}"
        }
    ],
    "pixiv": [
        {
            "patterns": [
                rf"https?://(www\.)?pixiv\.net/(?:[a-z][a-z]/)?users/{NUMERIC_ID}/?$",
                rf"https?://(www\.)?pixiv\.net/member\.php\?id={NUMERIC_ID}(?:[&#].*)?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://www.pixiv.net/users/{id}"
        }
    ],
    "imgur": [
        {
            "patterns": [
                rf"https?://(www\.)?imgur\.com/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://imgur.com/user/{id}"
        }
    ],
    "odysee": [
        {
            "patterns": [
                rf"https?://(www\.)?odysee\.com/@{PROFILE_ID_UNICODE}(?::[0-9A-Fa-f]+)?/?$",
                rf"^@?{PROFILE_ID_UNICODE}$"
            ],
            "sanitized": "https://odysee.com/@{id}"
        }
    ],
    "gog": [
        {
            "patterns": [
                rf"https?://(www\.)?gog\.com/(?:[a-z][a-z]/)?u/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.gog.com/u/{id}"
        }
    ],
    "modrinth": [
        {
            "patterns": [
                rf"https?://(www\.)?modrinth\.com/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://modrinth.com/user/{id}"
        }
    ],
    "niconico": [
        {
            "patterns": [
                rf"https?://(www\.)?nicovideo\.jp/user/{NUMERIC_ID}/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://www.nicovideo.jp/user/{id}"
        }
    ],
    "roblox": [
        {
            "patterns": [
                rf"https?://(www\.)?(?:web\.)?roblox\.com/(?:[a-z][a-z]/)?users/{NUMERIC_ID}(?:/profile)?/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://www.roblox.com/users/{id}/profile"
        }
    ],
    "truth_social": [
        {
            "patterns": [
                rf"https?://(www\.)?truthsocial\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://truthsocial.com/@{id}"
        }
    ],
    "buymeacoffee": [
        {
            "patterns": [
                rf"https?://(www\.)?buymeacoffee\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://buymeacoffee.com/{id}"
        }
    ],
    "ko_fi": [
        {
            "patterns": [
                rf"https?://(www\.)?ko-fi\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://ko-fi.com/{id}"
        }
    ],
    "lastfm": [
        {
            "patterns": [
                rf"https?://(www\.)?last\.fm/(?:[a-z][a-z]/)?user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.last.fm/user/{id}"
        }
    ],
    "orcid": [
        {
            "patterns": [
                rf"https?://(www\.)?orcid\.org/{ORCID_ID}/?$",
                rf"^{ORCID_ID}$"
            ],
            "sanitized": "https://orcid.org/{id}"
        }
    ],
    "npm": [
        {
            "patterns": [
                rf"https?://(www\.)?npmjs\.com/~{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.npmjs.com/~{id}"
        }
    ],
    "beacons": [
        {
            "patterns": [
                rf"https?://(www\.)?beacons\.ai/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://beacons.ai/{id}"
        }
    ],
    "codeforces": [
        {
            "patterns": [
                rf"https?://(www\.)?(?:m[0-9]\.)?codeforces\.com/profile/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://codeforces.com/profile/{id}"
        }
    ],
    "codewars": [
        {
            "patterns": [
                rf"https?://(www\.)?codewars\.com/users/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.codewars.com/users/{id}"
        }
    ],
    "codeberg": [
        {
            "patterns": [
                rf"https?://(www\.)?codeberg\.org/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://codeberg.org/{id}"
        }
    ],
    "crates_io": [
        {
            "patterns": [
                rf"https?://(www\.)?crates\.io/users/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://crates.io/users/{id}"
        }
    ],
    "gitee": [
        {
            "patterns": [
                rf"https?://(www\.)?gitee\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://gitee.com/{id}"
        }
    ],
    "wattpad": [
        {
            "patterns": [
                rf"https?://(www\.)?wattpad\.com/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.wattpad.com/user/{id}"
        }
    ],
    "anilist": [
        {
            "patterns": [
                rf"https?://(www\.)?anilist\.co/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://anilist.co/user/{id}"
        }
    ],
    "deviantart": [
        {
            "patterns": [
                rf"https?://(www\.)?deviantart\.com/{PROFILE_ID}/?$",
                r"https?://(?!www\.)(?P<id>[A-Za-z0-9-]+)\.deviantart\.com/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.deviantart.com/{id}"
        }
    ],
    "pexels": [
        {
            "patterns": [
                rf"https?://(www\.)?pexels\.com/(?:[a-z][a-z](?:-[a-z][a-z])?/)?@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://www.pexels.com/@{id}"
        }
    ],
    "xiaohongshu": [
        {
            "patterns": [
                rf"https?://(www\.)?(?:xiaohongshu|rednote)\.com/user/profile/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.rednote.com/user/profile/{id}"
        }
    ],
    "genius": [
        {
            "patterns": [
                rf"https?://(www\.)?genius\.com/(?![^/?#]*-(?:lyrics|annotated)/?$){PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://genius.com/{id}"
        }
    ],
    "lemon8": [
        {
            "patterns": [
                rf"https?://(www\.)?lemon8-app\.com/(?:[a-z][a-z](?:-[a-z][a-z])?/)?@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://www.lemon8-app.com/@{id}"
        }
    ],
    "airbnb": [
        {
            "patterns": [
                rf"https?://(www\.)?airbnb\.(?:com|ca|de|fr|es|it|nl|ie|jp|be|at|ch|dk|se|no|fi|pt|pl|gr|mx|cl|co\.uk|co\.in|co\.nz|co\.kr|com\.au|com\.br|com\.sg|com\.hk|com\.mx|com\.ar|com\.co)/users/show/{NUMERIC_ID}/?$",
                rf"https?://(www\.)?airbnb\.(?:com|ca|de|fr|es|it|nl|ie|jp|be|at|ch|dk|se|no|fi|pt|pl|gr|mx|cl|co\.uk|co\.in|co\.nz|co\.kr|com\.au|com\.br|com\.sg|com\.hk|com\.mx|com\.ar|com\.co)/users/profile/{NUMERIC_ID}/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://www.airbnb.com/users/show/{id}"
        }
    ],
    "trustpilot": [
        {
            "patterns": [
                rf"https?://(?:(?:www|[a-z][a-z])\.)?trustpilot\.com/users/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.trustpilot.com/users/{id}"
        }
    ],
    "carrd": [
        {
            "patterns": [
                r"https?://(?!www\.)(?P<id>[A-Za-z0-9-]+)\.carrd\.co/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://{id}.carrd.co"
        }
    ],
    "blogger": [
        {
            "patterns": [
                rf"https?://(www\.)?blogger\.com/profile/{NUMERIC_ID}/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://www.blogger.com/profile/{id}"
        }
    ],
    "tistory": [
        {
            "patterns": [
                r"https?://(?!www\.)(?P<id>[A-Za-z0-9-]+)\.tistory\.com/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://{id}.tistory.com"
        }
    ],
    "untappd": [
        {
            "patterns": [
                rf"https?://(www\.)?untappd\.com/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://untappd.com/user/{id}"
        }
    ],
    "storygraph": [
        {
            "patterns": [
                rf"https?://(?:app\.)?thestorygraph\.com/profile/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://app.thestorygraph.com/profile/{id}"
        }
    ],
    "rateyourmusic": [
        {
            "patterns": [
                rf"https?://(www\.)?rateyourmusic\.com/~{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://rateyourmusic.com/~{id}"
        }
    ],
    "flipboard": [
        {
            "patterns": [
                rf"https?://(www\.)?flipboard\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://flipboard.com/@{id}"
        }
    ],
    "character_ai": [
        {
            "patterns": [
                rf"https?://(www\.)?character\.ai/profile/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://character.ai/profile/{id}"
        }
    ],
    "ollama": [
        {
            "patterns": [
                rf"https?://(www\.)?ollama\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://ollama.com/{id}"
        }
    ],
    "depop": [
        {
            "patterns": [
                rf"https?://(www\.)?depop\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.depop.com/{id}"
        }
    ],
    "launchpad": [
        {
            "patterns": [
                rf"https?://(www\.)?launchpad\.net/~{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://launchpad.net/~{id}"
        }
    ],
    "codesandbox": [
        {
            "patterns": [
                rf"https?://(www\.)?codesandbox\.io/u/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://codesandbox.io/u/{id}"
        }
    ],
    "juejin": [
        {
            "patterns": [
                rf"https?://(www\.)?juejin\.cn/user/{NUMERIC_ID}(?:/posts)?/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://juejin.cn/user/{id}"
        }
    ],
    "csdn": [
        {
            "patterns": [
                rf"https?://blog\.csdn\.net/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://blog.csdn.net/{id}"
        }
    ],
    "wandb": [
        {
            "patterns": [
                rf"https?://forge\.coreweave\.com/profile/{PROFILE_ID}/?$",
                rf"https?://(www\.)?wandb\.ai/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://forge.coreweave.com/profile/{id}"
        }
    ],
    "chub_ai": [
        {
            "patterns": [
                rf"https?://(www\.)?chub\.ai/users/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://chub.ai/users/{id}"
        }
    ],
    "coursera": [
        {
            "patterns": [
                rf"https?://(www\.)?coursera\.org/user/{HEX32_ID}/?$",
                rf"https?://(www\.)?coursera\.org/user/i/{HEX32_ID}/?$",
                rf"^{HEX32_ID}$"
            ],
            "sanitized": "https://www.coursera.org/user/{id}"
        }
    ],
    "udemy": [
        {
            "patterns": [
                rf"https?://(www\.)?udemy\.com/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.udemy.com/user/{id}"
        }
    ],
    "khan_academy": [
        {
            "patterns": [
                rf"https?://(www\.)?khanacademy\.org/profile/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.khanacademy.org/profile/{id}"
        }
    ],
    "codecademy": [
        {
            "patterns": [
                rf"https?://(www\.)?codecademy\.com/profiles/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.codecademy.com/profiles/{id}"
        }
    ],
    "freecodecamp": [
        {
            "patterns": [
                rf"https?://forum\.freecodecamp\.org/u/{PROFILE_ID}(?:/summary)?/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://forum.freecodecamp.org/u/{id}"
        }
    ],
    "semantic_scholar": [
        {
            "patterns": [
                rf"https?://(www\.)?semanticscholar\.org/author/(?:[^/?#]+/)?{NUMERIC_ID}/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://www.semanticscholar.org/author/{id}"
        }
    ],
    "osf": [
        {
            "patterns": [
                rf"https?://(www\.)?osf\.io/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://osf.io/user/{id}"
        }
    ],
    "inaturalist": [
        {
            "patterns": [
                rf"https?://(www\.)?inaturalist\.org/people/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.inaturalist.org/people/{id}"
        }
    ],
    "faceit": [
        {
            "patterns": [
                rf"https?://(www\.)?faceit\.com/(?:[a-z][a-z](?:-[a-z][a-z])?/)?players/{PROFILE_ID}(?:/stats(?:/[a-z0-9]+)?)?/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.faceit.com/en/players/{id}"
        }
    ],
    "gamejolt": [
        {
            "patterns": [
                rf"https?://(www\.)?gamejolt\.com/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://gamejolt.com/@{id}"
        }
    ],
    "start_gg": [
        {
            "patterns": [
                rf"https?://(www\.)?(?:start|smash)\.gg/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.start.gg/user/{id}"
        }
    ],
    "curseforge": [
        {
            "patterns": [
                rf"https?://(www\.)?curseforge\.com/members/{PROFILE_ID}(?:/projects)?/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.curseforge.com/members/{id}"
        }
    ],
    "xda": [
        {
            "patterns": [
                r"https?://(?:xdaforums\.com|forum\.xda-developers\.com)/m/(?P<id>[A-Za-z0-9_.-]+\.[0-9]+)/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://xdaforums.com/m/{id}"
        }
    ],
    "chzzk": [
        {
            "patterns": [
                rf"https?://chzzk\.naver\.com/(?:live/)?{HEX32_ID}/?$",
                rf"^{HEX32_ID}$"
            ],
            "sanitized": "https://chzzk.naver.com/{id}"
        }
    ],
    "huya": [
        {
            "patterns": [
                rf"https?://(www\.)?huya\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.huya.com/{id}"
        }
    ],
    "douyu": [
        {
            "patterns": [
                rf"https?://(www\.)?douyu\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.douyu.com/{id}"
        }
    ],
    "rutube": [
        {
            "patterns": [
                rf"https?://(www\.)?rutube\.ru/channel/{NUMERIC_ID}(?:/(?:videos|about))?/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://rutube.ru/channel/{id}"
        }
    ],
    "soop": [
        {
            "patterns": [
                rf"https?://(www\.)?sooplive\.com/station/{PROFILE_ID}/?$",
                rf"https?://ch\.sooplive\.co\.kr/{PROFILE_ID}/?$",
                rf"https?://(?:bj|ch)\.afreecatv\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.sooplive.com/station/{id}"
        }
    ],
    "nimo_tv": [
        {
            "patterns": [
                rf"https?://(www\.)?nimo\.tv/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.nimo.tv/{id}"
        }
    ],
    "audioboom": [
        {
            "patterns": [
                rf"https?://(www\.)?audioboom\.com/channels/{NUMERIC_ID}(?:-[^/?#]*)?/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://audioboom.com/channels/{id}"
        }
    ],
    "jamendo": [
        {
            "patterns": [
                rf"https?://(www\.)?jamendo\.com/user/{NUMERIC_ID}(?:/[^/?#]+)?/?$",
                rf"https?://(www\.)?jamendo\.com/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.jamendo.com/user/{id}"
        }
    ],
    "bio_link": [
        {
            "patterns": [
                rf"https?://(www\.)?bio\.link/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://bio.link/{id}"
        }
    ],
    "taplink": [
        {
            "patterns": [
                rf"https?://(www\.)?taplink\.(?:cc|at|ws|me)/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://taplink.cc/{id}"
        }
    ],
    "solo_to": [
        {
            "patterns": [
                rf"https?://(www\.)?solo\.to/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://solo.to/{id}"
        }
    ],
    "hoo_be": [
        {
            "patterns": [
                rf"https?://(www\.)?hoo\.be/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://hoo.be/{id}"
        }
    ],
    "throne": [
        {
            "patterns": [
                rf"https?://(www\.)?throne\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://throne.com/{id}"
        }
    ],
    "fanfix": [
        {
            "patterns": [
                rf"https?://app\.fanfix\.io/@{PROFILE_ID}/?$",
                rf"^@?{PROFILE_ID}$"
            ],
            "sanitized": "https://app.fanfix.io/@{id}"
        }
    ],
    "campsite_bio": [
        {
            "patterns": [
                rf"https?://(www\.)?campsite\.bio/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://campsite.bio/{id}"
        }
    ],
    "500px": [
        {
            "patterns": [
                rf"https?://(www\.)?500px\.com/p/{PROFILE_ID}(?:/galleries)?/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://500px.com/p/{id}"
        }
    ],
    "redbubble": [
        {
            "patterns": [
                rf"https?://(www\.)?redbubble\.com/(?:[a-z][a-z]/)?people/{PROFILE_ID}(?:/(?:shop|explore|portfolio))?/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.redbubble.com/people/{id}"
        }
    ],
    "cara": [
        {
            "patterns": [
                rf"https?://(www\.)?cara\.app/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://cara.app/{id}"
        }
    ],
    "sketchfab": [
        {
            "patterns": [
                rf"https?://(www\.)?sketchfab\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://sketchfab.com/{id}"
        }
    ],
    "thingiverse": [
        {
            "patterns": [
                rf"https?://(www\.)?thingiverse\.com/{PROFILE_ID}(?:/designs)?/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.thingiverse.com/{id}"
        }
    ],
    "furaffinity": [
        {
            "patterns": [
                rf"https?://(www\.)?furaffinity\.net/user/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.furaffinity.net/user/{id}"
        }
    ],
    "toyhouse": [
        {
            "patterns": [
                rf"https?://(www\.)?toyhou\.se/(?![0-9]+\.){PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://toyhou.se/{id}"
        }
    ],
    "are_na": [
        {
            "patterns": [
                rf"https?://(www\.)?are\.na/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://www.are.na/{id}"
        }
    ],
    "buttondown": [
        {
            "patterns": [
                rf"https?://(www\.)?buttondown\.(?:com|email)/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://buttondown.com/{id}"
        }
    ],
    "paragraph": [
        {
            "patterns": [
                rf"https?://(www\.)?paragraph\.(?:com|xyz)/@{PROFILE_ID_UNICODE}/?$",
                rf"^@?{PROFILE_ID_UNICODE}$"
            ],
            "sanitized": "https://paragraph.com/@{id}"
        }
    ],
    "royal_road": [
        {
            "patterns": [
                rf"https?://(www\.)?royalroad\.com/profile/{NUMERIC_ID}/?$",
                rf"^{NUMERIC_ID}$"
            ],
            "sanitized": "https://www.royalroad.com/profile/{id}"
        }
    ],
    "scribd": [
        {
            "patterns": [
                r"https?://(www\.)?scribd\.com/user/(?P<id>[0-9]+/[A-Za-z0-9_.-]+)/?$"
            ],
            "sanitized": "https://www.scribd.com/user/{id}"
        }
    ],
    "issuu": [
        {
            "patterns": [
                rf"https?://(www\.)?issuu\.com/{PROFILE_ID}/?$",
                rf"^{PROFILE_ID}$"
            ],
            "sanitized": "https://issuu.com/{id}"
        }
    ],
    "velog": [
        {
            "patterns": [
                rf"https?://(www\.)?velog\.io/@{PROFILE_ID_UNICODE}(?:/posts)?/?$",
                rf"^@?{PROFILE_ID_UNICODE}$"
            ],
            "sanitized": "https://velog.io/@{id}"
        }
    ]
}
