# social-links

Python library that detects, validates, sanitizes, and extracts IDs from social profile URLs. Distribution name `social-links`, import name `sociallinks`. Runtime dependencies: none. Requires Python 3.8+. MIT. Version lives in `pyproject.toml`.

Public docs: https://ysskrishna.github.io/social-links/

## Layout

| Path | Role |
| --- | --- |
| `sociallinks/__init__.py` | Public exports. Do not export anything else. |
| `sociallinks/basic.py` | Module functions: `detect_platform`, `is_valid`, `sanitize`, `extract_id`, `list_platforms`. They share one lazy default `SocialLinks()`. |
| `sociallinks/core.py` | `SocialLinks`. Custom platforms and platform add/remove go here. |
| `sociallinks/platforms.py` | `PREDEFINED_PLATFORMS`. Source of truth for built-in platforms. |
| `sociallinks/constants.py` | ID regexes (`PROFILE_ID` and the rest) and `PlatformEntry` / `PlatformEntries`. |
| `sociallinks/exceptions.py` | `SocialLinksError` and subclasses. |
| `tests/platforms/test_happy_path.py` | One row per platform: key, bare id or `None`, profile URL, sanitized URL. |
| `tests/platforms/test_<key>.py` | Extra cases only: second hosts, query ids, legacy domains, rejections. |
| `tests/platforms/test_common_patterns.py` | www, http, and trailing slash, derived from the first entry of each platform. |
| `tests/platforms/conftest.py` | `sl` fixture: `SocialLinks()` with predefined platforms. |
| `scripts/gen_platform_docs.py` | Rewrites the README platform table and the "N+" counts. `PLATFORM_META` must match `PREDEFINED_PLATFORMS`. |
| `docs/` | MkDocs Material. `docs/CONTRIBUTING.md`, `docs/CHANGELOG.md`, and `docs/LICENSE.md` snippet the repo-root files. |

`CONTRIBUTING.md` still says to copy `tests/platforms/test_github.py`. That file does not exist. Follow this file for tests.

## Commands

```bash
uv sync --group dev
uv run pytest
uv run ruff check .
uv run python scripts/gen_platform_docs.py          # rewrite README and counts
uv run python scripts/gen_platform_docs.py --check  # fail if docs are stale
uv run mkdocs serve
uv build
```

CI (`.github/workflows/test.yml`) runs `uv sync --group dev`, then pytest on Python 3.8 through 3.13, and `ruff check .`. Docs and PyPI publish on `v*` tags.

## Behavior agents get wrong

- `detect_platform` returns `None` for an unknown URL and for a bare username. A bare id is valid only when the caller names the platform (`is_valid`, `sanitize`, `extract_id`).
- `is_valid` returns `False` when the platform is missing or the URL does not match. `sanitize` and `extract_id` raise (`PlatformNotFoundError`, `URLMismatchError`, `PlatformIDExtractionError`).
- Patterns are matched from the start of the input. End a URL pattern with `/?$`. Query strings and fragments are stripped when the raw input does not match, so do not add them unless the platform needs them (for example `?id=`).
- Every ID pattern must expose a named group `id`. The sanitized template contains `{id}` and no other placeholder.
- A platform is a list of entries. The first entry is the main profile form. Use another entry when the sanitized URL differs (YouTube channels, Facebook `profile.php`).
- Reuse an ID regex from `sociallinks/constants.py`. Add a new constant only when none of the existing ones match the real profile id.
- Confirm the URL on the live site, including the URL after redirects, before writing the pattern.
- Do not call `set_platform` on the module-level default instance. Tests and callers that need a custom registry construct `SocialLinks()`.

## Adding a platform

1. Add the key to `PREDEFINED_PLATFORMS` in `sociallinks/platforms.py`.
2. Add one row to `HAPPY_PATH` in `tests/platforms/test_happy_path.py`: `(key, bare_id_or_None, profile_url, sanitized_url)`.
3. Put only the unusual cases in `tests/platforms/test_<key>.py`, using the `sl` fixture.
4. Add `(display name, homepage, optional note)` to `PLATFORM_META` in `scripts/gen_platform_docs.py`, then run the generator. `tests/test_docs_sync.py` fails if the table or the counts are stale. Do not edit the table between `<!-- platforms:start -->` and `<!-- platforms:end -->` by hand.
5. Record the platform in `CHANGELOG.md` under the upcoming version.

## API and compatibility

- Stay on the Python 3.8 syntax already used in `sociallinks/`: `Optional`, `List`, `Dict`, `Tuple` from `typing`. No `list[str]`, no `X | Y`, no `match`.
- Do not add a runtime dependency. Dev tools stay in `[dependency-groups] dev`.
- Public behavior changes need a test, a Google-style docstring update, a changelog entry, and a README change when the examples change. Do not bump `pyproject.toml` version unless the task is a release.
- Keep a Changelog headings. Semantic versioning.

## Style

- Ruff selects `E` and `F` and ignores `E501`. Regexes and URLs may be long.
- Type hints on public functions. The package ships `py.typed`.
- Google docstrings (`Args`, `Returns`, `Raises`, `Examples`). MkDocs renders them with mkdocstrings. Keep examples that doctest would execute accurate.

## Comments and docstrings

- Prefer descriptive names and code over comments or test docstrings that repeat them. Remove redundant comments when editing nearby code.
- Keep comments that explain non-obvious behavior, constraints, or decisions.
- Preserve source docstrings used by MkDocs, and update them when the documented behavior changes.

## Boundaries

- Do not commit secrets, tokens, or local environment files.
- Do not publish a release, push a tag, or change the GitHub Actions publish flow unless asked.
- Do not weaken URL anchoring or make `detect_platform` guess a platform from a bare id.
