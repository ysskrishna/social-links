#!/usr/bin/env python3
"""Keep the platform list and platform counts in the docs in sync with the code.

Source of truth: ``PREDEFINED_PLATFORMS`` in ``sociallinks/platforms.py``.

What it updates:
  * the platform table in ``README.md`` between the markers
    ``<!-- platforms:start -->`` and ``<!-- platforms:end -->``;
  * hand-written counts such as ``65+ platforms`` in the README, docs,
    ``pyproject.toml``, ``mkdocs.yml`` and ``sociallinks/core.py``.

Usage:
    python scripts/gen_platform_docs.py            # rewrite files
    python scripts/gen_platform_docs.py --check    # exit 1 if anything is stale

When adding a platform to ``platforms.py``, also add its display name and
homepage to ``PLATFORM_META`` below. The script fails if the two disagree.
"""
import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from sociallinks.platforms import PREDEFINED_PLATFORMS  # noqa: E402

START = "<!-- platforms:start -->"
END = "<!-- platforms:end -->"
COLUMNS = 3

# key -> (display name, homepage, optional note)
PLATFORM_META: Dict[str, Tuple[str, str, Optional[str]]] = {
    "apple_music": ("Apple Music", "https://music.apple.com", None),
    "artstation": ("ArtStation", "https://artstation.com", None),
    "bandcamp": ("Bandcamp", "https://bandcamp.com", None),
    "behance": ("Behance", "https://behance.net", None),
    "bluesky": ("Bluesky", "https://bsky.app", None),
    "chess_com": ("Chess.com", "https://chess.com", None),
    "codepen": ("CodePen", "https://codepen.io", None),
    "crunchbase": ("Crunchbase", "https://crunchbase.com", None),
    "dailymotion": ("Dailymotion", "https://dailymotion.com", None),
    "dev_to": ("Dev.to", "https://dev.to", None),
    "discord": ("Discord", "https://discord.com", None),
    "dockerhub": ("Docker Hub", "https://hub.docker.com", None),
    "douyin": ("Douyin", "https://douyin.com", None),
    "dribbble": ("Dribbble", "https://dribbble.com", None),
    "etsy": ("Etsy", "https://etsy.com", None),
    "exercism": ("Exercism", "https://exercism.org", None),
    "facebook": ("Facebook", "https://facebook.com", None),
    "fiverr": ("Fiverr", "https://fiverr.com", None),
    "flickr": ("Flickr", "https://flickr.com", None),
    "github": ("GitHub", "https://github.com", None),
    "gitlab": ("GitLab", "https://gitlab.com", None),
    "gravatar": ("Gravatar", "https://gravatar.com", None),
    "gumroad": ("Gumroad", "https://gumroad.com", None),
    "hackerrank": ("HackerRank", "https://hackerrank.com", None),
    "hackernews": ("Hacker News", "https://news.ycombinator.com", None),
    "hashnode": ("Hashnode", "https://hashnode.com", None),
    "instagram": ("Instagram", "https://instagram.com", None),
    "kaggle": ("Kaggle", "https://kaggle.com", None),
    "keybase": ("Keybase", "https://keybase.io", None),
    "kuaishou": ("Kuaishou", "https://kuaishou.com", None),
    "leetcode": ("LeetCode", "https://leetcode.com", None),
    "lemmy_world": ("Lemmy World", "https://lemmy.world", None),
    "lichess": ("Lichess", "https://lichess.org", None),
    "linkedin": ("LinkedIn", "https://linkedin.com", "(personal & company)"),
    "linktree": ("Linktree", "https://linktr.ee", None),
    "mastodon": ("Mastodon", "https://mastodon.social", None),
    "medium": ("Medium", "https://medium.com", None),
    "patreon": ("Patreon", "https://patreon.com", None),
    "pinterest": ("Pinterest", "https://pinterest.com", None),
    "producthunt": ("Product Hunt", "https://producthunt.com", None),
    "pypi": ("PyPI", "https://pypi.org", None),
    "quora": ("Quora", "https://quora.com", None),
    "reddit": ("Reddit", "https://reddit.com", None),
    "replit": ("Replit", "https://replit.com", None),
    "rumble": ("Rumble", "https://rumble.com", None),
    "signal": ("Signal", "https://signal.me", None),
    "slideshare": ("SlideShare", "https://slideshare.net", None),
    "snapchat": ("Snapchat", "https://snapchat.com", None),
    "soundcloud": ("SoundCloud", "https://soundcloud.com", None),
    "spotify": ("Spotify", "https://spotify.com", None),
    "stackoverflow": ("Stack Overflow", "https://stackoverflow.com", None),
    "steam": ("Steam", "https://steamcommunity.com", None),
    "substack": ("Substack", "https://substack.com", None),
    "telegram": ("Telegram", "https://telegram.org", None),
    "threads": ("Threads", "https://threads.com", None),
    "tiktok": ("TikTok", "https://tiktok.com", None),
    "trello": ("Trello", "https://trello.com", None),
    "tumblr": ("Tumblr", "https://tumblr.com", None),
    "twitch": ("Twitch", "https://twitch.tv", None),
    "unsplash": ("Unsplash", "https://unsplash.com", None),
    "vimeo": ("Vimeo", "https://vimeo.com", None),
    "vk": ("VK", "https://vk.com", None),
    "wechat": ("WeChat", "https://weixin.qq.com", None),
    "weibo": ("Weibo", "https://weibo.com", None),
    "wellfound": ("Wellfound (AngelList)", "https://wellfound.com", None),
    "whatsapp": ("WhatsApp", "https://whatsapp.com", None),
    "wordpress": ("WordPress", "https://wordpress.com", None),
    "x": ("X (Twitter)", "https://x.com", None),
    "youtube": ("YouTube", "https://youtube.com", None),
}

# Files that contain hand-written "N+ platforms" counts.
COUNT_FILES = [
    "README.md",
    "docs/index.md",
    "docs/basic-api.md",
    "docs/demo.md",
    "pyproject.toml",
    "mkdocs.yml",
    "sociallinks/core.py",
]

# "65+ platforms", "65+ predefined ...", "65+ supported ..." and the trailing
# "# 65+" comments in README code samples.
COUNT_PATTERNS = [
    re.compile(r"\b\d+\+(?= (?:platforms|predefined|supported)\b)"),
    re.compile(r"(?<=Supported platforms: )\d+\+"),
    re.compile(r"(?<=\)  # )\d+\+$", re.MULTILINE),
]


def platform_count() -> int:
    return len(PREDEFINED_PLATFORMS)


def count_label(n: int) -> str:
    """Round down to a multiple of 5 and add '+', e.g. 69 -> '65+'."""
    return f"{(n // 5) * 5}+"


def check_meta() -> None:
    missing = sorted(set(PREDEFINED_PLATFORMS) - set(PLATFORM_META))
    extra = sorted(set(PLATFORM_META) - set(PREDEFINED_PLATFORMS))
    if missing or extra:
        raise SystemExit(
            "PLATFORM_META is out of sync with PREDEFINED_PLATFORMS.\n"
            f"  missing in PLATFORM_META: {missing}\n"
            f"  not in platforms.py:      {extra}"
        )


def render_table() -> str:
    """Render the platform cells as rows of ``COLUMNS`` markdown table cells."""
    check_meta()
    cells: List[str] = []
    for key in sorted(PLATFORM_META, key=lambda k: PLATFORM_META[k][0].lower()):
        name, url, note = PLATFORM_META[key]
        cell = f"[{name}]({url})"
        if note:
            cell += f" {note}"
        cells.append(cell)
    while len(cells) % COLUMNS:
        cells.append("")
    rows = [
        "| " + " | ".join(cells[i : i + COLUMNS]) + " |"
        for i in range(0, len(cells), COLUMNS)
    ]
    return "\n".join(rows)


def sync_table(text: str) -> str:
    start = text.find(START)
    end = text.find(END)
    if start == -1 or end == -1 or end < start:
        raise SystemExit(f"README.md must contain {START} and {END}")
    body_start = start + len(START)
    header = "\n\n| Predefined Platforms | | |\n|---|---|---|\n"
    return text[:body_start] + header + render_table() + "\n\n" + text[end:]


def sync_counts(text: str) -> str:
    label = count_label(platform_count())
    for pattern in COUNT_PATTERNS:
        text = pattern.sub(label, text)
    return text


def run(check: bool) -> List[str]:
    """Return the list of files that are (or were) out of date."""
    changed: List[str] = []
    for rel in COUNT_FILES:
        path = ROOT / rel
        old = path.read_text(encoding="utf-8")
        new = sync_counts(old)
        if rel == "README.md":
            new = sync_table(new)
        if new != old:
            changed.append(rel)
            if not check:
                path.write_text(new, encoding="utf-8")
    return changed


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="exit 1 if files are stale")
    args = parser.parse_args(argv)
    changed = run(check=args.check)
    if changed:
        verb = "stale" if args.check else "updated"
        print(f"{verb}: " + ", ".join(changed))
        return 1 if args.check else 0
    print("platform docs are up to date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
