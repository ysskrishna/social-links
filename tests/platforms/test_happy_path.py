"""Happy path for every predefined platform.

One row per platform: a profile URL, the sanitized URL it maps to, and the bare
profile id (``None`` when the platform takes no bare id). Platform-specific
cases (second hosts, query ids, legacy domains, negatives) stay in the
platform's own test file.
"""
import pytest


# (platform, bare profile id or None, url, sanitized)
HAPPY_PATH = [
    ("apple_music", "136975", "https://music.apple.com/artist/136975", "https://music.apple.com/artist/136975"),
    ("artstation", "ysskrishna", "https://www.artstation.com/ysskrishna", "https://www.artstation.com/ysskrishna"),
    ("atcoder", "tourist", "https://atcoder.jp/users/tourist", "https://atcoder.jp/users/tourist"),
    ("bandcamp", "ysskrishna", "https://ysskrishna.bandcamp.com", "https://ysskrishna.bandcamp.com"),
    ("behance", "ysskrishna", "https://behance.net/ysskrishna", "https://behance.net/ysskrishna"),
    ("bluesky", "ysskrishna.bsky.social", "https://bsky.app/profile/ysskrishna.bsky.social", "https://bsky.app/profile/ysskrishna.bsky.social"),
    ("chess_com", "ysskrishna", "https://www.chess.com/member/ysskrishna", "https://www.chess.com/member/ysskrishna"),
    ("clawhub", "steipete", "https://clawhub.ai/steipete", "https://clawhub.ai/steipete"),
    ("codechef", "gennady.korotkevich", "https://www.codechef.com/users/gennady.korotkevich", "https://www.codechef.com/users/gennady.korotkevich"),
    ("codepen", "ysskrishna", "https://codepen.io/ysskrishna", "https://codepen.io/ysskrishna"),
    ("crunchbase", None, "https://www.crunchbase.com/organization/slack", "https://www.crunchbase.com/organization/slack"),
    ("dailymotion", "ysskrishna", "https://www.dailymotion.com/ysskrishna", "https://www.dailymotion.com/ysskrishna"),
    ("dev_to", "ysskrishna", "https://dev.to/ysskrishna", "https://dev.to/ysskrishna"),
    ("discord", "ysskrishna", "https://discord.gg/ysskrishna", "https://discord.gg/ysskrishna"),
    ("dockerhub", "ysskrishna", "https://hub.docker.com/u/ysskrishna", "https://hub.docker.com/u/ysskrishna"),
    ("douyin", "MS4wLjABAAAA9yeV8IIJxpee3_u9zb_Al3_mOA8IffgD3_ueMCQUly4", "https://www.douyin.com/user/MS4wLjABAAAA9yeV8IIJxpee3_u9zb_Al3_mOA8IffgD3_ueMCQUly4", "https://www.douyin.com/user/MS4wLjABAAAA9yeV8IIJxpee3_u9zb_Al3_mOA8IffgD3_ueMCQUly4"),
    ("dribbble", "ysskrishna", "https://dribbble.com/ysskrishna", "https://dribbble.com/ysskrishna"),
    ("etsy", "MyShopName", "https://etsy.com/shop/MyShopName", "https://etsy.com/shop/MyShopName"),
    ("exercism", "ysskrishna", "https://exercism.org/profiles/ysskrishna", "https://exercism.org/profiles/ysskrishna"),
    ("facebook", "ysskrishna", "https://facebook.com/ysskrishna", "https://facebook.com/ysskrishna"),
    ("fiverr", "ysskrishna", "https://www.fiverr.com/ysskrishna", "https://www.fiverr.com/ysskrishna"),
    ("flickr", "dv-hans", "https://www.flickr.com/people/dv-hans", "https://www.flickr.com/people/dv-hans"),
    ("github", "ysskrishna", "https://github.com/ysskrishna", "https://github.com/ysskrishna"),
    ("gitlab", "ysskrishna", "https://gitlab.com/ysskrishna", "https://gitlab.com/ysskrishna"),
    ("gravatar", "ysskrishna", "https://gravatar.com/ysskrishna", "https://gravatar.com/ysskrishna"),
    ("gumroad", "ysskrishna", "https://ysskrishna.gumroad.com", "https://gumroad.com/ysskrishna"),
    ("hackernews", "pg", "https://news.ycombinator.com/user?id=pg", "https://news.ycombinator.com/user?id=pg"),
    ("hackerrank", "ysskrishna", "https://www.hackerrank.com/profile/ysskrishna", "https://www.hackerrank.com/profile/ysskrishna"),
    ("hashnode", None, "https://hashnode.com/@ysskrishna", "https://hashnode.com/@ysskrishna"),
    ("huggingface", "ysskrishna", "https://huggingface.co/ysskrishna", "https://huggingface.co/ysskrishna"),
    ("instagram", "ysskrishna", "https://instagram.com/ysskrishna", "https://instagram.com/ysskrishna"),
    ("kaggle", "ysskrishna", "https://www.kaggle.com/ysskrishna", "https://www.kaggle.com/ysskrishna"),
    ("keybase", "ysskrishna", "https://keybase.io/ysskrishna", "https://keybase.io/ysskrishna"),
    ("kuaishou", "3xxdnfw963m6abu", "https://www.kuaishou.com/profile/3xxdnfw963m6abu", "https://www.kuaishou.com/profile/3xxdnfw963m6abu"),
    ("leetcode", "ysskrishna", "https://leetcode.com/ysskrishna", "https://leetcode.com/ysskrishna"),
    ("lemmy_world", "ysskrishna", "https://lemmy.world/u/ysskrishna", "https://lemmy.world/u/ysskrishna"),
    ("lichess", "ysskrishna", "https://lichess.org/@/ysskrishna", "https://lichess.org/@/ysskrishna"),
    ("linkedin", "ysskrishna", "https://linkedin.com/in/ysskrishna", "https://linkedin.com/in/ysskrishna"),
    ("linktree", "ysskrishna", "https://linktr.ee/ysskrishna", "https://linktr.ee/ysskrishna"),
    ("lobsters", "jcs", "https://lobste.rs/~jcs", "https://lobste.rs/~jcs"),
    ("mastodon", None, "https://mastodon.social/@ysskrishna", "https://mastodon.social/@ysskrishna"),
    ("medium", None, "https://medium.com/@ysskrishna", "https://medium.com/@ysskrishna"),
    ("patreon", "ysskrishna", "https://patreon.com/ysskrishna", "https://patreon.com/ysskrishna"),
    ("pinterest", "ysskrishna", "https://pinterest.com/ysskrishna", "https://pinterest.com/ysskrishna"),
    ("producthunt", None, "https://www.producthunt.com/@ysskrishna", "https://www.producthunt.com/@ysskrishna"),
    ("pypi", "ysskrishna", "https://pypi.org/user/ysskrishna", "https://pypi.org/user/ysskrishna"),
    ("qiita", "jnchito", "https://qiita.com/jnchito", "https://qiita.com/jnchito"),
    ("quora", "Jay-Hoque", "https://www.quora.com/profile/Jay-Hoque", "https://quora.com/profile/Jay-Hoque"),
    ("reddit", "ysskrishna", "https://reddit.com/user/ysskrishna", "https://reddit.com/user/ysskrishna"),
    ("replicate", "ysskrishna", "https://replicate.com/ysskrishna", "https://replicate.com/ysskrishna"),
    ("replit", "ysskrishna", "https://replit.com/@ysskrishna", "https://replit.com/@ysskrishna"),
    ("rumble", "ysskrishna", "https://rumble.com/user/ysskrishna", "https://rumble.com/user/ysskrishna"),
    ("signal", "abc123xyz", "https://signal.me/#p/abc123xyz", "https://signal.me/#p/abc123xyz"),
    ("slideshare", "michaelyublosky", "https://www.slideshare.net/michaelyublosky", "https://www.slideshare.net/michaelyublosky"),
    ("snapchat", None, "https://snapchat.com/add/ysskrishna", "https://snapchat.com/@ysskrishna"),
    ("soundcloud", "ysskrishna", "https://soundcloud.com/ysskrishna", "https://soundcloud.com/ysskrishna"),
    ("spotify", "3WrFJ7ztbogyGnTHbHJFl2", "https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2", "https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2"),
    ("stackoverflow", "12345", "https://stackoverflow.com/users/12345", "https://stackoverflow.com/users/12345"),
    ("steam", "pepepro76561198317693716", "https://steamcommunity.com/id/pepepro76561198317693716", "https://steamcommunity.com/id/pepepro76561198317693716"),
    ("substack", "ysskrishna", "https://ysskrishna.substack.com", "https://substack.com/@ysskrishna"),
    ("telegram", "telegram", "https://t.me/telegram", "https://t.me/telegram"),
    ("threads", "ysskrishna", "https://threads.com/@ysskrishna", "https://threads.com/@ysskrishna"),
    ("tiktok", None, "https://tiktok.com/@ysskrishna", "https://tiktok.com/@ysskrishna"),
    ("topcoder", "tourist", "https://profiles.topcoder.com/tourist", "https://profiles.topcoder.com/tourist"),
    ("trello", "ysskrishna", "https://trello.com/ysskrishna", "https://trello.com/ysskrishna"),
    ("tryhackme", "tryhackme", "https://tryhackme.com/p/tryhackme", "https://tryhackme.com/p/tryhackme"),
    ("tumblr", "ysskrishna", "https://ysskrishna.tumblr.com", "https://tumblr.com/ysskrishna"),
    ("twitch", "ysskrishna", "https://twitch.tv/ysskrishna", "https://twitch.tv/ysskrishna"),
    ("unsplash", "ysskrishna", "https://unsplash.com/@ysskrishna", "https://unsplash.com/@ysskrishna"),
    ("vimeo", "ysskrishna", "https://vimeo.com/ysskrishna", "https://vimeo.com/ysskrishna"),
    ("vk", None, "https://vk.com/ysskrishna", "https://vk.com/ysskrishna"),
    ("wechat", "DutchEmbassy_BJ", "https://open.weixin.qq.com/qr/code?username=DutchEmbassy_BJ", "https://open.weixin.qq.com/qr/code?username=DutchEmbassy_BJ"),
    ("weibo", "guanzhilin", "https://weibo.com/guanzhilin", "https://weibo.com/guanzhilin"),
    ("wellfound", "ysskrishna", "https://wellfound.com/u/ysskrishna", "https://wellfound.com/u/ysskrishna"),
    ("whatsapp", "1234567890", "https://wa.me/1234567890", "https://wa.me/1234567890"),
    ("wordpress", "ysskrishna", "https://wordpress.com/people/ysskrishna", "https://wordpress.com/people/ysskrishna"),
    ("x", None, "https://x.com/ysskrishna", "https://x.com/ysskrishna"),
    ("youtube", None, "https://youtube.com/@ysskrishna", "https://youtube.com/@ysskrishna"),
]


@pytest.mark.parametrize(
    "platform,profile_id,url,sanitized", HAPPY_PATH, ids=[row[0] for row in HAPPY_PATH]
)
def test_happy_path(sl, platform, profile_id, url, sanitized):
    assert sl.detect_platform(url) == platform
    assert sl.is_valid(platform, url) is True
    assert sl.sanitize(platform, url) == sanitized
    if profile_id is not None:
        assert sl.is_valid(platform, profile_id) is True
        assert sl.sanitize(platform, profile_id) == sanitized
        assert sl.detect_platform(profile_id) is None
