# Username regex for release 1.5.0

Owns one decision: which regex captures the id (username, handle, numeric id) for each 1.5.0 platform.

## Rules (as applied)

The regex is a URL-shape matcher, not a username validator. It must accept every real id and reject other URL shapes on the same host.

1. **Fixed id shape.** Numeric, hex, ORCID or `npub1` ids use a fixed-shape constant, confirmed against public docs or an indexed real profile.
2. **Documented charset only widens.** Published username rules are used to *allow* extra characters (dots in legacy Codeforces handles, `%20` in OpenStreetMap and Slashdot names). They never remove characters from `PROFILE_ID`: older accounts often break today's signup rules.
3. **Non-ASCII names** use `PROFILE_ID_UNICODE` (OpenStreetMap, XING, ResearchGate, Velog, Brunch, Slashdot, and, after the archive check below, TryHackMe, Odysee, osu!, Mixcloud, Paragraph, ShareChat, Malt, Packagist).
4. **Archive check.** Every new pattern was run against real profile URLs that the Wayback Machine captured with HTTP 200. Where a genuine id shape was rejected, the pattern was widened (rule 2): non-ASCII ids above, Primal's 64-hex `/p/{pubkey}`, Coursera's `/user/i/{id}`, Jamendo's legacy `/user/{name}`. Rejected captures that are scraped page noise (`%5C`, `%0A`, `${...}`) were ignored. Shapes seen but not confirmed (eBay `!`/`$`, Slashdot `!`, Topcoder `[...]`) are in `08-followup-ledger.md`.
5. **Default** is `PROFILE_ID` (`[A-Za-z0-9_.-]+`). Evidence says "charset not documented".

A fixed prefix (`~`, `@`, `_`) sits in the URL part of the pattern, not in the id group.

Subdomain ids (Carrd, Tistory, Hatena Blog, legacy itch.io and DeviantArt hosts) use one DNS label, `[A-Za-z0-9-]+`: a label cannot contain dots, so this does not narrow any real id.

## Constants

| Constant | Regex | Use |
|---|---|---|
| `PROFILE_ID` | `[A-Za-z0-9_.-]+` | Default |
| `PROFILE_ID_AT` | `@?[A-Za-z0-9_.-]+` | Optional `@` in the id |
| `PROFILE_ID_UNICODE` | `[\w&%'–®\.-]+` | Non-ASCII names |
| `PROFILE_ID_EXTENDED` | `-?[A-Za-z0-9_@=.\-]+` | Leading hyphen, `@`, `=` |
| `PHONE_NUMBER` | `\+?[0-9]+` | Phone ids |
| `NUMERIC_ID` (new, public) | `\d+` | Numeric ids. Promoted from core's private `_NUMERIC_ID`, which stays as an alias. |
| `HEX32_ID` (new) | `[0-9a-fA-F]{32}` | Coursera, CHZZK |
| `ORCID_ID` (new) | `\d{4}-\d{4}-\d{4}-\d{3}[\dX]` | ORCID |
| `NOSTR_NPUB` (new) | `npub1[a-z0-9]{58}` | Primal |

No `0x` constant: OpenSea accepts a username or an address on the same path, and `PROFILE_ID` already matches `0x` + 40 hex. The new constants are registered as bare-id bodies in `sociallinks/core.py`, so `detect_platform()` still returns `None` for bare ids.

## Every pattern

- ends with `/?$` (query-string platforms end with the same `(?:[&#].*)?$` tail Facebook `profile.php?id=` uses);
- has at least one negative test (second segment, reserved path, wrong or lookalike host, sub-page);
- rejects common site paths on first-segment hosts (`/about`, `/login`, `/settings`, `/explore`, `/search`, `/help`, `/pricing`, `/signup`, `/terms`, `/privacy` plus per-site paths) with a negative lookahead.

## Part 1: the original 48

| Platform | Key | Sanitized URL | Id regex | Evidence | Status |
|---|---|---|---|---|---|
| Hugging Face | `huggingface` | `https://huggingface.co/{id}` | PROFILE_ID; second segment (model/dataset) and site paths rejected | plan.md "48 that already passed"; https://beat.rip/check (letters, digits, hyphens; subset of PROFILE_ID) | done |
| Replicate | `replicate` | `https://replicate.com/{id}` | PROFILE_ID; second segment (model) rejected | plan.md "48 that already passed"; charset not documented | done |
| ClawHub | `clawhub` | `https://clawhub.ai/{id}` | PROFILE_ID; skill URLs `/{owner}/skills/{slug}` rejected | plan.md "48 that already passed"; charset not documented | done |
| Lobsters | `lobsters` | `https://lobste.rs/~{id}` | PROFILE_ID; `~` prefix in the URL part; legacy `/u/` redirects to `/~` | plan.md "48 that already passed"; charset not documented | done |
| AtCoder | `atcoder` | `https://atcoder.jp/users/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| CodeChef | `codechef` | `https://www.codechef.com/users/{id}` | PROFILE_ID (dots allowed) | plan.md "48 that already passed"; charset not documented | done |
| Topcoder | `topcoder` | `https://profiles.topcoder.com/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| TryHackMe | `tryhackme` | `https://tryhackme.com/p/{id}` | PROFILE_ID_UNICODE (widened: Cyrillic and CJK usernames appear in archived profile URLs) | plan.md "48 that already passed"; Wayback CDX captures of `tryhackme.com/p/{non-ASCII}` with status 200 | done |
| Qiita | `qiita` | `https://qiita.com/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Habr | `habr` | `https://habr.com/users/{id}` | PROFILE_ID; optional `/en/` or `/ru/` locale segment | plan.md "48 that already passed"; charset not documented | done |
| Zenn | `zenn` | `https://zenn.dev/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| RubyGems | `rubygems` | `https://rubygems.org/profiles/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| NuGet | `nuget` | `https://www.nuget.org/profiles/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| SourceForge | `sourceforge` | `https://sourceforge.net/u/{id}/profile` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| SourceHut | `sourcehut` | `https://sr.ht/~{id}` | PROFILE_ID; `~` prefix; second segment (repo/project) rejected | plan.md "48 that already passed"; charset not documented | done |
| Stack Exchange | `stack_exchange` | `https://stackexchange.com/users/{id}` | NUMERIC_ID (network account id), optional display-name slug | plan.md "48 that already passed"; Stack Exchange network profiles are `stackexchange.com/users/{numeric}`; per-site profiles use per-site ids (not matched) | done |
| Google Scholar | `google_scholar` | `https://scholar.google.com/citations?user={id}` | PROFILE_ID (widened from `[A-Za-z0-9_-]`); id is the `user=` query value | plan.md "48 that already passed"; query-string platform like Hacker News `?id=`; matched before the query is stripped | done |
| Kick | `kick` | `https://kick.com/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Stan Store | `stan_store` | `https://stan.store/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Farcaster | `farcaster` | `https://farcaster.xyz/{id}` | PROFILE_ID (dots allowed: `.eth` names); `warpcast.com` is a second host | plan.md "48 that already passed"; charset not documented | done |
| Figma | `figma` | `https://www.figma.com/@{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Douban | `douban` | `https://www.douban.com/people/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Topmate | `topmate` | `https://topmate.io/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Freelancer.com | `freelancer` | `https://www.freelancer.com/u/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| eBay | `ebay` | `https://www.ebay.com/usr/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Poshmark | `poshmark` | `https://poshmark.com/closet/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Civitai | `civitai` | `https://civitai.com/user/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| OpenSea | `opensea` | `https://opensea.io/{id}` | PROFILE_ID covers both usernames and `0x` + 40 hex addresses, so no new constant | plan.md "48 that already passed"; https://ethereum.org/en/developers/docs/accounts/ (address = 0x + 40 hex) | done |
| Hey.xyz | `hey_xyz` | `https://hey.xyz/u/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Primal | `primal` | `https://primal.net/p/{id}` | NOSTR_NPUB `npub1[a-z0-9]{58}` (63 chars), or the 64-hex public key (widened: Primal serves `/p/{hex}` too) | plan.md "48 that already passed"; https://github.com/nostr-protocol/nips/blob/master/19.md; Wayback CDX captures of `primal.net/p/{64 hex}` with status 200 | done |
| OpenStreetMap | `openstreetmap` | `https://www.openstreetmap.org/user/{id}` | PROFILE_ID_UNICODE: display names can contain spaces (`%20`) and non-ASCII letters | plan.md "48 that already passed"; https://wiki.openstreetmap.org/wiki/Display_name (any characters) | done |
| Pixelfed | `pixelfed` | `https://pixelfed.social/{id}` | PROFILE_ID; `pixelfed.social` only; `/@{u}` redirects to `/{u}` | plan.md "48 that already passed"; charset not documented | done |
| Misskey | `misskey` | `https://misskey.io/@{id}` | PROFILE_ID; `misskey.io` only (same shape as mastodon) | plan.md "48 that already passed"; charset not documented | done |
| Bilibili | `bilibili` | `https://space.bilibili.com/{id}` | NUMERIC_ID (uid) | plan.md "48 that already passed"; charset not documented | done |
| Letterboxd | `letterboxd` | `https://letterboxd.com/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Goodreads | `goodreads` | `https://www.goodreads.com/user/show/{id}` | NUMERIC_ID, optional `-slug` | plan.md "48 that already passed"; https://help.goodreads.com/s/article/Where-can-I-find-my-user-ID | done |
| Scratch | `scratch` | `https://scratch.mit.edu/users/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Discogs | `discogs` | `https://www.discogs.com/user/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| MyAnimeList | `myanimelist` | `https://myanimelist.net/profile/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| osu! | `osu` | `https://osu.ppy.sh/users/{id}` | PROFILE_ID_UNICODE (widened: usernames with spaces `%20` and non-ASCII letters exist): numeric id or username; optional ruleset segment | plan.md "48 that already passed"; Wayback CDX captures of `osu.ppy.sh/users/-%20Mia/card` and similar | done |
| itch.io | `itch_io` | `https://itch.io/profile/{id}` | PROFILE_ID; subdomain form `{u}.itch.io` (DNS label) redirects to `/profile/{u}` | plan.md "48 that already passed"; charset not documented | done |
| Speedrun.com | `speedrun` | `https://www.speedrun.com/users/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Pixiv | `pixiv` | `https://www.pixiv.net/users/{id}` | NUMERIC_ID; optional `/en/` locale; legacy `member.php?id=` | plan.md "48 that already passed"; charset not documented | done |
| Imgur | `imgur` | `https://imgur.com/user/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Odysee | `odysee` | `https://odysee.com/@{id}` | PROFILE_ID_UNICODE (widened: channel names such as `@Águila` exist); the `:claimid` suffix is dropped (the bare `@name` resolves to the winning claim) | plan.md "48 that already passed"; Wayback CDX captures of `odysee.com/@{non-ASCII}:{claim}` with status 200 | done |
| GOG | `gog` | `https://www.gog.com/u/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Modrinth | `modrinth` | `https://modrinth.com/user/{id}` | PROFILE_ID | plan.md "48 that already passed"; charset not documented | done |
| Niconico | `niconico` | `https://www.nicovideo.jp/user/{id}` | NUMERIC_ID | plan.md "48 that already passed"; charset not documented | done |

## Part 2: newly ADD from the reverify pass

| Platform | Key | Sanitized URL | Id regex | Evidence | Status |
|---|---|---|---|---|---|
| Roblox | `roblox` | `https://www.roblox.com/users/{id}/profile` | NUMERIC_ID | batch 01; https://create.roblox.com/docs/cloud/auth/oauth2-reference (profile `users/{user_id}/profile`) | done |
| Truth Social | `truth_social` | `https://truthsocial.com/@{id}` | PROFILE_ID | batch 01; charset not documented | done |
| Buy Me a Coffee | `buymeacoffee` | `https://buymeacoffee.com/{id}` | PROFILE_ID | batch 01; charset not documented | done |
| Ko-fi | `ko_fi` | `https://ko-fi.com/{id}` | PROFILE_ID | batch 01; https://beat.rip/check/kofi-username (letters, digits, `_`, `-`; subset of PROFILE_ID) | done |
| Last.fm | `lastfm` | `https://www.last.fm/user/{id}` | PROFILE_ID | batch 01; charset not documented | done |
| ORCID | `orcid` | `https://orcid.org/{id}` | ORCID_ID `\d{4}-\d{4}-\d{4}-\d{3}[\dX]` | batch 01; https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier | done |
| npm | `npm` | `https://www.npmjs.com/~{id}` | PROFILE_ID (npm: lowercase, digits, `-`; legacy names keep `_` and `.`) | batch 01; https://docs.npmjs.com/creating-a-new-npm-user-account/ | done |
| Beacons | `beacons` | `https://beacons.ai/{id}` | PROFILE_ID | batch 02; charset not documented | done |
| Codeforces | `codeforces` | `https://codeforces.com/profile/{id}` | PROFILE_ID (letters, digits, `_`, `-`; legacy handles contain dots) | batch 02; https://codeforces.me/blog/entry/17078 (register rule + legacy dot handles) | done |
| Codewars | `codewars` | `https://www.codewars.com/users/{id}` | PROFILE_ID | batch 02; charset not documented | done |
| Codeberg | `codeberg` | `https://codeberg.org/{id}` | PROFILE_ID | batch 02; charset not documented | done |
| crates.io | `crates_io` | `https://crates.io/users/{id}` | PROFILE_ID | batch 02; crates.io logins are GitHub logins: https://doc.rust-lang.org/cargo/reference/publishing.html | done |
| Gitee | `gitee` | `https://gitee.com/{id}` | PROFILE_ID | batch 03; charset not documented | done |
| Wattpad | `wattpad` | `https://www.wattpad.com/user/{id}` | PROFILE_ID | batch 03; https://support.wattpad.com/hc/en-us/articles/201461324-Creating-an-account (letters, digits, `_`) | done |
| AniList | `anilist` | `https://anilist.co/user/{id}` | PROFILE_ID | batch 03; charset not documented | done |
| DeviantArt | `deviantart` | `https://www.deviantart.com/{id}` | PROFILE_ID; legacy `{u}.deviantart.com` host | batch 03; charset not documented | done |
| Pexels | `pexels` | `https://www.pexels.com/@{id}` | PROFILE_ID | batch 03; charset not documented | done |
| Xiaohongshu (RedNote) | `xiaohongshu` | `https://www.rednote.com/user/profile/{id}` | PROFILE_ID (ids are 24 hex; PROFILE_ID is wider) | batch 03; charset not documented | done |
| Genius | `genius` | `https://genius.com/{id}` | PROFILE_ID; `*-lyrics` / `*-annotated` song slugs rejected | batch 04; charset not documented | done |
| Lemon8 | `lemon8` | `https://www.lemon8-app.com/@{id}` | PROFILE_ID | batch 04; charset not documented | done |
| Airbnb | `airbnb` | `https://www.airbnb.com/users/show/{id}` | NUMERIC_ID; any listed `airbnb.*` country host | batch 05; charset not documented | done |
| Trustpilot | `trustpilot` | `https://www.trustpilot.com/users/{id}` | PROFILE_ID (ids are 24 hex) | batch 05; charset not documented | done |
| Carrd | `carrd` | `https://{id}.carrd.co` | DNS label `[A-Za-z0-9-]+` in the host (a label cannot hold dots) | batch 05; charset not documented | done |
| Blogger | `blogger` | `https://www.blogger.com/profile/{id}` | NUMERIC_ID (20-digit profile id) | batch 05; charset not documented | done |
| Tistory | `tistory` | `https://{id}.tistory.com` | DNS label in the host | batch 05; charset not documented | done |
| Untappd | `untappd` | `https://untappd.com/user/{id}` | PROFILE_ID | batch 05; charset not documented | done |
| The StoryGraph | `storygraph` | `https://app.thestorygraph.com/profile/{id}` | PROFILE_ID | batch 06; charset not documented | done |
| RateYourMusic | `rateyourmusic` | `https://rateyourmusic.com/~{id}` | PROFILE_ID | batch 06; charset not documented | done |
| Flipboard | `flipboard` | `https://flipboard.com/@{id}` | PROFILE_ID | batch 06; charset not documented | done |
| Character.AI | `character_ai` | `https://character.ai/profile/{id}` | PROFILE_ID | batch 06; charset not documented | done |
| Ollama | `ollama` | `https://ollama.com/{id}` | PROFILE_ID; second segment (model) rejected | batch 06; charset not documented | done |
| Depop | `depop` | `https://www.depop.com/{id}` | PROFILE_ID | batch 07; charset not documented | done |
| Launchpad | `launchpad` | `https://launchpad.net/~{id}` | PROFILE_ID | batch 07; charset not documented | done |
| CodeSandbox | `codesandbox` | `https://codesandbox.io/u/{id}` | PROFILE_ID | batch 07; charset not documented | done |
| Juejin | `juejin` | `https://juejin.cn/user/{id}` | NUMERIC_ID | batch 07; https://github.com/SuperHuangXu/juejin-post-action/blob/main/README.md | done |
| CSDN | `csdn` | `https://blog.csdn.net/{id}` | PROFILE_ID | batch 07; charset not documented | done |
| Weights & Biases | `wandb` | `https://forge.coreweave.com/profile/{id}` | PROFILE_ID; `wandb.ai/{entity}` input alias | batch 07; charset not documented | done |
| Chub.ai | `chub_ai` | `https://chub.ai/users/{id}` | PROFILE_ID | batch 07; charset not documented | done |
| Coursera | `coursera` | `https://www.coursera.org/user/{id}` | HEX32_ID (32 hex); the legacy `/user/i/{id}` form is also accepted | batch 08; https://www.coursera.org/user/85dca6cc1c1ccacdb8d6cbc3853c8eff (indexed profile); `/user/i/` form documented at webpolicy.org/2014/09/04 and used in public resumes | done |
| Udemy | `udemy` | `https://www.udemy.com/user/{id}` | PROFILE_ID | batch 08; charset not documented | done |
| Khan Academy | `khan_academy` | `https://www.khanacademy.org/profile/{id}` | PROFILE_ID | batch 08; charset not documented | done |
| Codecademy | `codecademy` | `https://www.codecademy.com/profiles/{id}` | PROFILE_ID | batch 08; charset not documented | done |
| freeCodeCamp | `freecodecamp` | `https://forum.freecodecamp.org/u/{id}` | PROFILE_ID | batch 08; charset not documented | done |
| Semantic Scholar | `semantic_scholar` | `https://www.semanticscholar.org/author/{id}` | NUMERIC_ID; optional name segment before it | batch 08; https://www.semanticscholar.org/faq (author ids are numeric) | done |
| OSF | `osf` | `https://osf.io/user/{id}` | PROFILE_ID (GUIDs are 5 alphanumerics; PROFILE_ID is wider) | batch 09; charset not documented | done |
| iNaturalist | `inaturalist` | `https://www.inaturalist.org/people/{id}` | PROFILE_ID: login or numeric id | batch 09; charset not documented | done |
| FACEIT | `faceit` | `https://www.faceit.com/en/players/{id}` | PROFILE_ID | batch 09; charset not documented | done |
| Game Jolt | `gamejolt` | `https://gamejolt.com/@{id}` | PROFILE_ID | batch 09; charset not documented | done |
| start.gg | `start_gg` | `https://www.start.gg/user/{id}` | PROFILE_ID (slugs are 8 hex); legacy `smash.gg` host | batch 09; charset not documented | done |
| CurseForge | `curseforge` | `https://www.curseforge.com/members/{id}` | PROFILE_ID | batch 10; charset not documented | done |
| XDA Forums | `xda` | `https://xdaforums.com/m/{id}` | `{username}.{digits}` (XenForo member slug; username may contain dots) | batch 10; charset not documented | done |
| CHZZK | `chzzk` | `https://chzzk.naver.com/{id}` | HEX32_ID (channel id is 32 hex) | batch 10; https://ssapi.kr/docs/additional/platform/chzzk-channel | done |
| Huya | `huya` | `https://www.huya.com/{id}` | PROFILE_ID: vanity name or numeric room | batch 10; charset not documented | done |
| Douyu | `douyu` | `https://www.douyu.com/{id}` | PROFILE_ID: numeric room or vanity; `dyshid` query dropped | batch 10; charset not documented | done |
| Rutube | `rutube` | `https://rutube.ru/channel/{id}` | NUMERIC_ID | batch 11; charset not documented | done |
| SOOP (AfreecaTV) | `soop` | `https://www.sooplive.com/station/{id}` | PROFILE_ID; legacy `bj.afreecatv.com` and `ch.sooplive.co.kr` hosts | batch 11; charset not documented | done |
| Nimo TV | `nimo_tv` | `https://www.nimo.tv/{id}` | PROFILE_ID | batch 11; charset not documented | done |
| Audioboom | `audioboom` | `https://audioboom.com/channels/{id}` | NUMERIC_ID, optional `-slug` | batch 11; charset not documented | done |
| Jamendo | `jamendo` | `https://www.jamendo.com/user/{id}` | NUMERIC_ID with optional name segment, or a legacy username (`/user/{name}`) | batch 11; Wayback CDX captures of legacy `jamendo.com/user/{name}` with status 200 | done |
| Bio.link | `bio_link` | `https://bio.link/{id}` | PROFILE_ID | batch 11; charset not documented | done |
| Taplink | `taplink` | `https://taplink.cc/{id}` | PROFILE_ID | batch 12; charset not documented | done |
| solo.to | `solo_to` | `https://solo.to/{id}` | PROFILE_ID | batch 12; charset not documented | done |
| Hoo.be | `hoo_be` | `https://hoo.be/{id}` | PROFILE_ID | batch 12; charset not documented | done |
| Throne | `throne` | `https://throne.com/{id}` | PROFILE_ID | batch 12; charset not documented | done |
| Fanfix | `fanfix` | `https://app.fanfix.io/@{id}` | PROFILE_ID | batch 12; charset not documented | done |
| Campsite.bio | `campsite_bio` | `https://campsite.bio/{id}` | PROFILE_ID | batch 12; charset not documented | done |
| 500px | `500px` | `https://500px.com/p/{id}` | PROFILE_ID | batch 13; charset not documented | done |
| Redbubble | `redbubble` | `https://www.redbubble.com/people/{id}` | PROFILE_ID | batch 13; charset not documented | done |
| Cara | `cara` | `https://cara.app/{id}` | PROFILE_ID | batch 13; charset not documented | done |
| Sketchfab | `sketchfab` | `https://sketchfab.com/{id}` | PROFILE_ID | batch 13; charset not documented | done |
| Thingiverse | `thingiverse` | `https://www.thingiverse.com/{id}` | PROFILE_ID | batch 13; charset not documented | done |
| Fur Affinity | `furaffinity` | `https://www.furaffinity.net/user/{id}` | PROFILE_ID | batch 13; charset not documented | done |
| Toyhouse | `toyhouse` | `https://toyhou.se/{id}` | PROFILE_ID | batch 14; charset not documented | done |
| Are.na | `are_na` | `https://www.are.na/{id}` | PROFILE_ID | batch 14; charset not documented | done |
| Buttondown | `buttondown` | `https://buttondown.com/{id}` | PROFILE_ID | batch 14; charset not documented | done |
| Paragraph | `paragraph` | `https://paragraph.com/@{id}` | PROFILE_ID_UNICODE (widened: Cyrillic, Arabic and Georgian handles appear in archived URLs) | batch 14; charset not documented | done |
| Royal Road | `royal_road` | `https://www.royalroad.com/profile/{id}` | NUMERIC_ID | batch 14; charset not documented | done |
| Scribd | `scribd` | `https://www.scribd.com/user/{id}` | `{numericId}/{username}` composite (both segments are required by the canonical URL); no bare id | batch 14; charset not documented | done |
| Issuu | `issuu` | `https://issuu.com/{id}` | PROFILE_ID; `ps` query dropped | batch 14; charset not documented | done |
| Velog | `velog` | `https://velog.io/@{id}` | PROFILE_ID_UNICODE (widened; Korean names appear in shared links) | batch 14; charset not documented | done |
| Brunch | `brunch` | `https://brunch.co.kr/@{id}` | PROFILE_ID_UNICODE | batch 15; charset not documented | done |
| Ameba Blog | `ameblo` | `https://ameblo.jp/{id}` | PROFILE_ID | batch 15; charset not documented | done |
| Hatena Blog | `hatena_blog` | `https://{id}.hatenablog.com` | DNS label in the host; `hatenablog.jp`, `hateblo.jp`, `hatenadiary.*` hosts | batch 15; charset not documented | done |
| Dzen | `dzen` | `https://dzen.ru/{id}` | PROFILE_ID | batch 15; charset not documented | done |
| OK.ru | `ok_ru` | `https://ok.ru/profile/{id}` | NUMERIC_ID (vanity slugs are ambiguous with groups, not matched) | batch 15; charset not documented | done |
| ShareChat | `sharechat` | `https://sharechat.com/profile/{id}` | PROFILE_ID_UNICODE (widened from numeric: handles, numeric ids and Devanagari handles appear) | batch 15; charset not documented | done |
| Mercari | `mercari` | `https://jp.mercari.com/user/profile/{id}` | NUMERIC_ID | batch 15; charset not documented | done |
| Vinted | `vinted` | `https://www.vinted.com/member/{id}` | NUMERIC_ID, optional `-slug`; country TLD varies | batch 15; charset not documented | done |
| XING | `xing` | `https://www.xing.com/profile/{id}` | PROFILE_ID_UNICODE | batch 16; charset not documented | done |
| Malt | `malt` | `https://www.malt.fr/profile/{id}` | PROFILE_ID_UNICODE (widened: slugs with accents and Cyrillic appear) | batch 16; charset not documented | done |
| Komoot | `komoot` | `https://www.komoot.com/user/{id}` | PROFILE_ID: numeric id or slug | batch 16; charset not documented | done |
| note | `note_com` | `https://note.com/{id}` | PROFILE_ID | batch 16; charset not documented | done |
| Naver Blog | `naver_blog` | `https://blog.naver.com/{id}` | PROFILE_ID; prologue/PostList `blogId=` query form | batch 16; charset not documented | done |
| Mixcloud | `mixcloud` | `https://www.mixcloud.com/{id}` | PROFILE_ID_UNICODE (widened: slugs such as `màu-trầm` exist) | batch 16; Wikidata P9509 (Mixcloud ID); Wayback CDX captures with non-ASCII slugs | done |
| Audiomack | `audiomack` | `https://audiomack.com/{id}` | PROFILE_ID | batch 17; charset not documented | done |
| BitChute | `bitchute` | `https://www.bitchute.com/channel/{id}` | PROFILE_ID | batch 17; charset not documented | done |
| LINE | `line` | `https://page.line.me/{id}` | PROFILE_ID; `@` only in the entry URL (official accounts) | batch 17; charset not documented | done |
| KakaoTalk Channel | `kakaotalk_channel` | `https://pf.kakao.com/_{id}` | PROFILE_ID; the leading `_` is in the URL part, not the id | batch 17; charset not documented | done |
| Tripadvisor | `tripadvisor` | `https://www.tripadvisor.com/Profile/{id}` | PROFILE_ID | batch 17; charset not documented | done |
| Contra | `contra` | `https://contra.com/{id}` | PROFILE_ID | batch 17; charset not documented | done |
| Codementor | `codementor` | `https://www.codementor.io/@{id}` | PROFILE_ID | batch 17; charset not documented | done |
| Trakt | `trakt` | `https://app.trakt.tv/profile/{id}` | PROFILE_ID | batch 18; charset not documented | done |
| Minds | `minds` | `https://www.minds.com/{id}` | PROFILE_ID | batch 18; charset not documented | done |
| Kickstarter | `kickstarter` | `https://www.kickstarter.com/profile/{id}` | PROFILE_ID | batch 18; charset not documented | done |
| Packagist | `packagist` | `https://packagist.org/users/{id}` | PROFILE_ID_UNICODE (widened: Chinese usernames appear) | batch 18; Wikidata P11531; Wayback CDX captures of `packagist.org/users/{CJK}` | done |
| Slashdot | `slashdot` | `https://slashdot.org/~{id}` | PROFILE_ID_UNICODE (widened: nicknames contain spaces, `%20` in URLs) | batch 18; charset not documented | done |
| ResearchGate | `researchgate` | `https://www.researchgate.net/profile/{id}` | PROFILE_ID_UNICODE (widened: names with diacritics appear) | batch 19; charset not documented | done |

## Part 3: extra platforms

| Platform | Key | Sanitized URL | Id regex | Evidence | Status |
|---|---|---|---|---|---|
| OnlyFans | `onlyfans` | `https://onlyfans.com/{id}` | PROFILE_ID; `/my/...`, tracking `/{u}/c12` and site paths rejected | live page checked with curl (title names the account); https://fanstracker.com/tools/onlyfans-link-checker/ (profile `onlyfans.com/{username}`) | done |
| Open Collective | `opencollective` | `https://opencollective.com/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://opencollective.com/webpack (title "webpack - Open Collective") | done |
| Liberapay | `liberapay` | `https://liberapay.com/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://liberapay.com/about/ (user pages at `liberapay.com/{username}`; Cloudflare blocks curl) | done |
| WordPress.org | `wordpress_org` | `https://profiles.wordpress.org/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://profiles.wordpress.org/matt/ (title "Matt Mullenweg (@matt) – WordPress user profile") | done |
| Instructables | `instructables` | `https://www.instructables.com/member/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://www.instructables.com/member/randofo/ (title "randofo") | done |
| TMDB | `tmdb` | `https://www.themoviedb.org/u/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://www.themoviedb.org/u/travisbell (title "Travis Bell's Profile") | done |
| Hex | `hex_pm` | `https://hex.pm/users/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://hex.pm/users/josevalim (title "josevalim / Hex") | done |
| MetaCPAN | `metacpan` | `https://metacpan.org/author/{id}` | PROFILE_ID (PAUSE ids are uppercase letters and digits; PROFILE_ID is wider) | live page checked with curl (title names the account); https://metacpan.org/about/faq (author pages at `metacpan.org/author/PAUSEID`) | done |
| Indie Hackers | `indiehackers` | `https://www.indiehackers.com/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://www.indiehackers.com/csallen (title "Courtland Allen (@csallen) on Indie Hackers") | done |
| HackerEarth | `hackerearth` | `https://www.hackerearth.com/@{id}` | PROFILE_ID | live page checked with curl (title names the account); https://www.hackerearth.com/@sachin/ (title "Sachin Gupta / Developer Profile on HackerEarth") | done |
| Myspace | `myspace` | `https://myspace.com/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://myspace.com/tom (title "Tom Anderson (tom) on Myspace") | done |
| About.me | `about_me` | `https://about.me/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://about.me/tonyconrad (title "Tony Conrad - San Francisco, ...") | done |
| GeeksforGeeks | `geeksforgeeks` | `https://www.geeksforgeeks.org/profile/{id}` | PROFILE_ID; legacy `/user/` and `auth.` host redirect to `/profile/` | live page checked with curl (title names the account); https://www.geeksforgeeks.org/user/sandeepjainlinkedin/ redirects to `/profile/sandeepjainlinkedin` | done |
| HackerOne | `hackerone` | `https://hackerone.com/{id}` | PROFILE_ID (company program pages share the same shape) | live page checked with curl (title names the account); https://docs.hackerone.com/en/articles/8390060-badges (`hackerone.com/[hacker-name]`) | done |
| Bugcrowd | `bugcrowd` | `https://bugcrowd.com/h/{id}` | PROFILE_ID | live page checked with curl (title names the account); https://bugcrowd.com/h/nahamsec (200; researcher profiles live under `/h/`) | done |
| Anaconda.org | `anaconda` | `https://anaconda.org/{id}` | PROFILE_ID (user or channel name); second segment (package) rejected | live page checked with curl (title names the account); https://anaconda.org/conda-forge (title "conda-forge / Anaconda.org") | done |

## Not shipped

| Platform | Why |
|---|---|
| Academia.edu | Profile URL is `{affiliation}.academia.edu/{Name}`: two variables, one in the host. A sanitized template has exactly one `{id}`, so the URL cannot be rebuilt from an id. Ledgered in `08-followup-ledger.md`. |

