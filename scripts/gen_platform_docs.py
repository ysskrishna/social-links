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
    "500px": ("500px", "https://500px.com", None),
    "airbnb": ("Airbnb", "https://airbnb.com", None),
    "ameblo": ("Ameba Blog", "https://ameblo.jp", None),
    "anilist": ("AniList", "https://anilist.co", None),
    "apple_music": ("Apple Music", "https://music.apple.com", None),
    "are_na": ("Are.na", "https://are.na", None),
    "artstation": ("ArtStation", "https://artstation.com", None),
    "atcoder": ("AtCoder", "https://atcoder.jp", None),
    "audioboom": ("Audioboom", "https://audioboom.com", None),
    "audiomack": ("Audiomack", "https://audiomack.com", None),
    "bandcamp": ("Bandcamp", "https://bandcamp.com", None),
    "beacons": ("Beacons", "https://beacons.ai", None),
    "behance": ("Behance", "https://behance.net", None),
    "bilibili": ("Bilibili", "https://bilibili.com", None),
    "bio_link": ("Bio.link", "https://bio.link", None),
    "bitchute": ("BitChute", "https://bitchute.com", None),
    "blogger": ("Blogger", "https://blogger.com", None),
    "bluesky": ("Bluesky", "https://bsky.app", None),
    "brunch": ("Brunch", "https://brunch.co.kr", None),
    "buttondown": ("Buttondown", "https://buttondown.com", None),
    "buymeacoffee": ("Buy Me a Coffee", "https://buymeacoffee.com", None),
    "campsite_bio": ("Campsite.bio", "https://campsite.bio", None),
    "cara": ("Cara", "https://cara.app", None),
    "carrd": ("Carrd", "https://carrd.co", None),
    "character_ai": ("Character.AI", "https://character.ai", None),
    "chess_com": ("Chess.com", "https://chess.com", None),
    "chub_ai": ("Chub.ai", "https://chub.ai", "(NSFW)"),
    "chzzk": ("CHZZK", "https://chzzk.naver.com", None),
    "civitai": ("Civitai", "https://civitai.com", None),
    "clawhub": ("ClawHub", "https://clawhub.ai", None),
    "codeberg": ("Codeberg", "https://codeberg.org", None),
    "codecademy": ("Codecademy", "https://codecademy.com", None),
    "codechef": ("CodeChef", "https://codechef.com", None),
    "codeforces": ("Codeforces", "https://codeforces.com", None),
    "codementor": ("Codementor", "https://codementor.io", None),
    "codepen": ("CodePen", "https://codepen.io", None),
    "codesandbox": ("CodeSandbox", "https://codesandbox.io", None),
    "codewars": ("Codewars", "https://codewars.com", None),
    "contra": ("Contra", "https://contra.com", None),
    "coursera": ("Coursera", "https://coursera.org", None),
    "crates_io": ("crates.io", "https://crates.io", None),
    "crunchbase": ("Crunchbase", "https://crunchbase.com", None),
    "csdn": ("CSDN", "https://csdn.net", None),
    "curseforge": ("CurseForge", "https://curseforge.com", None),
    "dailymotion": ("Dailymotion", "https://dailymotion.com", None),
    "depop": ("Depop", "https://depop.com", None),
    "dev_to": ("Dev.to", "https://dev.to", None),
    "deviantart": ("DeviantArt", "https://deviantart.com", None),
    "discogs": ("Discogs", "https://discogs.com", None),
    "discord": ("Discord", "https://discord.com", None),
    "dockerhub": ("Docker Hub", "https://hub.docker.com", None),
    "douban": ("Douban", "https://douban.com", None),
    "douyin": ("Douyin", "https://douyin.com", None),
    "douyu": ("Douyu", "https://douyu.com", None),
    "dribbble": ("Dribbble", "https://dribbble.com", None),
    "dzen": ("Dzen", "https://dzen.ru", None),
    "ebay": ("eBay", "https://ebay.com", None),
    "etsy": ("Etsy", "https://etsy.com", None),
    "exercism": ("Exercism", "https://exercism.org", None),
    "facebook": ("Facebook", "https://facebook.com", None),
    "faceit": ("FACEIT", "https://faceit.com", None),
    "fanfix": ("Fanfix", "https://fanfix.io", "(NSFW)"),
    "farcaster": ("Farcaster", "https://farcaster.xyz", None),
    "figma": ("Figma", "https://figma.com", None),
    "fiverr": ("Fiverr", "https://fiverr.com", None),
    "flickr": ("Flickr", "https://flickr.com", None),
    "flipboard": ("Flipboard", "https://flipboard.com", None),
    "freecodecamp": ("freeCodeCamp", "https://freecodecamp.org", None),
    "freelancer": ("Freelancer.com", "https://freelancer.com", None),
    "furaffinity": ("Fur Affinity", "https://furaffinity.net", "(NSFW)"),
    "gamejolt": ("Game Jolt", "https://gamejolt.com", None),
    "genius": ("Genius", "https://genius.com", None),
    "gitee": ("Gitee", "https://gitee.com", None),
    "github": ("GitHub", "https://github.com", None),
    "gitlab": ("GitLab", "https://gitlab.com", None),
    "gog": ("GOG", "https://gog.com", None),
    "goodreads": ("Goodreads", "https://goodreads.com", None),
    "google_scholar": ("Google Scholar", "https://scholar.google.com", None),
    "gravatar": ("Gravatar", "https://gravatar.com", None),
    "gumroad": ("Gumroad", "https://gumroad.com", None),
    "habr": ("Habr", "https://habr.com", None),
    "hackerrank": ("HackerRank", "https://hackerrank.com", None),
    "hackernews": ("Hacker News", "https://news.ycombinator.com", None),
    "hashnode": ("Hashnode", "https://hashnode.com", None),
    "hatena_blog": ("Hatena Blog", "https://hatenablog.com", None),
    "hey_xyz": ("Hey.xyz", "https://hey.xyz", None),
    "hoo_be": ("Hoo.be", "https://hoo.be", None),
    "huggingface": ("Hugging Face", "https://huggingface.co", None),
    "huya": ("Huya", "https://huya.com", None),
    "imgur": ("Imgur", "https://imgur.com", None),
    "inaturalist": ("iNaturalist", "https://inaturalist.org", None),
    "instagram": ("Instagram", "https://instagram.com", None),
    "instructables": ("Instructables", "https://instructables.com", None),
    "issuu": ("Issuu", "https://issuu.com", None),
    "itch_io": ("itch.io", "https://itch.io", None),
    "jamendo": ("Jamendo", "https://jamendo.com", None),
    "juejin": ("Juejin", "https://juejin.cn", None),
    "kaggle": ("Kaggle", "https://kaggle.com", None),
    "kakaotalk_channel": ("KakaoTalk Channel", "https://pf.kakao.com", None),
    "keybase": ("Keybase", "https://keybase.io", None),
    "khan_academy": ("Khan Academy", "https://khanacademy.org", None),
    "kick": ("Kick", "https://kick.com", None),
    "kickstarter": ("Kickstarter", "https://kickstarter.com", None),
    "ko_fi": ("Ko-fi", "https://ko-fi.com", None),
    "komoot": ("Komoot", "https://komoot.com", None),
    "kuaishou": ("Kuaishou", "https://kuaishou.com", None),
    "lastfm": ("Last.fm", "https://last.fm", None),
    "launchpad": ("Launchpad", "https://launchpad.net", None),
    "leetcode": ("LeetCode", "https://leetcode.com", None),
    "lemmy_world": ("Lemmy World", "https://lemmy.world", None),
    "lemon8": ("Lemon8", "https://lemon8-app.com", None),
    "letterboxd": ("Letterboxd", "https://letterboxd.com", None),
    "liberapay": ("Liberapay", "https://liberapay.com", None),
    "lichess": ("Lichess", "https://lichess.org", None),
    "line": ("LINE", "https://line.me", None),
    "linkedin": ("LinkedIn", "https://linkedin.com", "(personal & company)"),
    "linktree": ("Linktree", "https://linktr.ee", None),
    "lobsters": ("Lobsters", "https://lobste.rs", None),
    "malt": ("Malt", "https://malt.com", None),
    "mastodon": ("Mastodon", "https://mastodon.social", None),
    "medium": ("Medium", "https://medium.com", None),
    "mercari": ("Mercari", "https://jp.mercari.com", None),
    "minds": ("Minds", "https://minds.com", None),
    "misskey": ("Misskey", "https://misskey.io", None),
    "mixcloud": ("Mixcloud", "https://mixcloud.com", None),
    "modrinth": ("Modrinth", "https://modrinth.com", None),
    "myanimelist": ("MyAnimeList", "https://myanimelist.net", None),
    "naver_blog": ("Naver Blog", "https://blog.naver.com", None),
    "niconico": ("Niconico", "https://nicovideo.jp", None),
    "nimo_tv": ("Nimo TV", "https://nimo.tv", None),
    "note_com": ("note", "https://note.com", None),
    "npm": ("npm", "https://npmjs.com", None),
    "nuget": ("NuGet", "https://nuget.org", None),
    "odysee": ("Odysee", "https://odysee.com", None),
    "ok_ru": ("OK.ru", "https://ok.ru", None),
    "ollama": ("Ollama", "https://ollama.com", None),
    "onlyfans": ("OnlyFans", "https://onlyfans.com", "(NSFW)"),
    "opencollective": ("Open Collective", "https://opencollective.com", None),
    "opensea": ("OpenSea", "https://opensea.io", None),
    "openstreetmap": ("OpenStreetMap", "https://openstreetmap.org", None),
    "orcid": ("ORCID", "https://orcid.org", None),
    "osf": ("OSF", "https://osf.io", None),
    "osu": ("osu!", "https://osu.ppy.sh", None),
    "packagist": ("Packagist", "https://packagist.org", None),
    "paragraph": ("Paragraph", "https://paragraph.com", None),
    "patreon": ("Patreon", "https://patreon.com", None),
    "pexels": ("Pexels", "https://pexels.com", None),
    "pinterest": ("Pinterest", "https://pinterest.com", None),
    "pixelfed": ("Pixelfed", "https://pixelfed.social", None),
    "pixiv": ("Pixiv", "https://pixiv.net", None),
    "poshmark": ("Poshmark", "https://poshmark.com", None),
    "primal": ("Primal", "https://primal.net", None),
    "producthunt": ("Product Hunt", "https://producthunt.com", None),
    "pypi": ("PyPI", "https://pypi.org", None),
    "qiita": ("Qiita", "https://qiita.com", None),
    "quora": ("Quora", "https://quora.com", None),
    "rateyourmusic": ("RateYourMusic", "https://rateyourmusic.com", None),
    "redbubble": ("Redbubble", "https://redbubble.com", None),
    "reddit": ("Reddit", "https://reddit.com", None),
    "replicate": ("Replicate", "https://replicate.com", None),
    "replit": ("Replit", "https://replit.com", None),
    "researchgate": ("ResearchGate", "https://researchgate.net", None),
    "roblox": ("Roblox", "https://roblox.com", None),
    "royal_road": ("Royal Road", "https://royalroad.com", None),
    "rubygems": ("RubyGems", "https://rubygems.org", None),
    "rumble": ("Rumble", "https://rumble.com", None),
    "rutube": ("Rutube", "https://rutube.ru", None),
    "scratch": ("Scratch", "https://scratch.mit.edu", None),
    "scribd": ("Scribd", "https://scribd.com", None),
    "semantic_scholar": ("Semantic Scholar", "https://semanticscholar.org", None),
    "sharechat": ("ShareChat", "https://sharechat.com", None),
    "signal": ("Signal", "https://signal.me", None),
    "sketchfab": ("Sketchfab", "https://sketchfab.com", None),
    "slashdot": ("Slashdot", "https://slashdot.org", None),
    "slideshare": ("SlideShare", "https://slideshare.net", None),
    "snapchat": ("Snapchat", "https://snapchat.com", None),
    "solo_to": ("solo.to", "https://solo.to", None),
    "soop": ("SOOP (AfreecaTV)", "https://sooplive.com", None),
    "soundcloud": ("SoundCloud", "https://soundcloud.com", None),
    "sourceforge": ("SourceForge", "https://sourceforge.net", None),
    "sourcehut": ("SourceHut", "https://sr.ht", None),
    "speedrun": ("Speedrun.com", "https://speedrun.com", None),
    "spotify": ("Spotify", "https://spotify.com", None),
    "stack_exchange": ("Stack Exchange", "https://stackexchange.com", None),
    "stackoverflow": ("Stack Overflow", "https://stackoverflow.com", None),
    "stan_store": ("Stan Store", "https://stan.store", None),
    "start_gg": ("start.gg", "https://start.gg", None),
    "steam": ("Steam", "https://steamcommunity.com", None),
    "storygraph": ("The StoryGraph", "https://thestorygraph.com", None),
    "substack": ("Substack", "https://substack.com", None),
    "taplink": ("Taplink", "https://taplink.cc", None),
    "telegram": ("Telegram", "https://telegram.org", None),
    "thingiverse": ("Thingiverse", "https://thingiverse.com", None),
    "threads": ("Threads", "https://threads.com", None),
    "throne": ("Throne", "https://throne.com", "(NSFW)"),
    "tiktok": ("TikTok", "https://tiktok.com", None),
    "tistory": ("Tistory", "https://tistory.com", None),
    "topcoder": ("Topcoder", "https://topcoder.com", None),
    "topmate": ("Topmate", "https://topmate.io", None),
    "toyhouse": ("Toyhouse", "https://toyhou.se", None),
    "trakt": ("Trakt", "https://trakt.tv", None),
    "trello": ("Trello", "https://trello.com", None),
    "tripadvisor": ("Tripadvisor", "https://tripadvisor.com", None),
    "trustpilot": ("Trustpilot", "https://trustpilot.com", None),
    "truth_social": ("Truth Social", "https://truthsocial.com", None),
    "tryhackme": ("TryHackMe", "https://tryhackme.com", None),
    "tumblr": ("Tumblr", "https://tumblr.com", None),
    "twitch": ("Twitch", "https://twitch.tv", None),
    "udemy": ("Udemy", "https://udemy.com", None),
    "unsplash": ("Unsplash", "https://unsplash.com", None),
    "untappd": ("Untappd", "https://untappd.com", None),
    "velog": ("Velog", "https://velog.io", None),
    "vimeo": ("Vimeo", "https://vimeo.com", None),
    "vinted": ("Vinted", "https://vinted.com", None),
    "vk": ("VK", "https://vk.com", None),
    "wandb": ("Weights & Biases", "https://wandb.ai", None),
    "wattpad": ("Wattpad", "https://wattpad.com", None),
    "wechat": ("WeChat", "https://weixin.qq.com", None),
    "weibo": ("Weibo", "https://weibo.com", None),
    "wellfound": ("Wellfound (AngelList)", "https://wellfound.com", None),
    "whatsapp": ("WhatsApp", "https://whatsapp.com", None),
    "wordpress": ("WordPress", "https://wordpress.com", None),
    "wordpress_org": ("WordPress.org", "https://profiles.wordpress.org", None),
    "x": ("X (Twitter)", "https://x.com", None),
    "xda": ("XDA Forums", "https://xdaforums.com", None),
    "xiaohongshu": ("Xiaohongshu (RedNote)", "https://www.xiaohongshu.com", None),
    "xing": ("XING", "https://xing.com", None),
    "youtube": ("YouTube", "https://youtube.com", None),
    "zenn": ("Zenn", "https://zenn.dev", None),
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
