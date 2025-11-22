import re
from typing import Dict, List, Optional, Any, Tuple
from sociallinks.profiles import PREDEFINED_PROFILES
from sociallinks.exceptions import (
    ProfileNotFoundError,
    ProfileAlreadyExistsError,
    InvalidProfileError,
    ProfileIDExtractionError,
    URLMismatchError,
)


class SocialLinks:
    """
    Social media URL normalizer.
    """

    def __init__(
        self,
        use_predefined_profiles: bool = True,
        regex_flags: int = re.IGNORECASE,
    ):
        self.profiles: Dict[str, Any] = {}
        self._compiled: Dict[str, List[Tuple[re.Pattern, str]]] = {}
        self.regex_flags = regex_flags

        if use_predefined_profiles:
            self.profiles.update(PREDEFINED_PROFILES)

        # Compile all
        for name, data in self.profiles.items():
            self._compile_profile(name, data)

    # ------------------------------------------------------------------
    # Internal Helpers
    # ------------------------------------------------------------------

    def _compile_profile(self, name: str, data: Any) -> None:
        compiled_entries: List[Tuple[re.Pattern, str]] = []
        entries = data if isinstance(data, list) else [data]

        for entry in entries:
            if not isinstance(entry, dict):
                continue

            patterns = entry.get("patterns")
            sanitized = entry.get("sanitized")

            if not patterns or not sanitized:
                continue

            for p in (patterns if isinstance(patterns, list) else [patterns]):
                compiled_entries.append(
                    (re.compile(p, flags=self.regex_flags), sanitized)
                )

        if not compiled_entries:
            raise InvalidProfileError(f"Profile '{name}' has no valid patterns or templates.")

        self._compiled[name] = compiled_entries

    @staticmethod
    def _extract_id(match: re.Match) -> Optional[str]:
        if "id" in match.groupdict() and match.group("id"):
            return match.group("id")

        for g in match.groups():
            if g:
                return g
        return None

    # ------------------------------------------------------------------
    # Core API
    # ------------------------------------------------------------------

    def detect_profile(self, url: str) -> Optional[str]:
        u = url.strip()
        for name, entries in self._compiled.items():
            if any(pattern.search(u) for pattern, _ in entries):
                return name
        return None

    def is_valid(self, profile_name: str, url: str) -> bool:
        entries = self._compiled.get(profile_name)
        if not entries:
            return False
        u = url.strip()
        return any(pattern.search(u) for pattern, _ in entries)

    def sanitize(self, profile_name: str, url: str) -> str:
        entries = self._compiled.get(profile_name)
        if not entries:
            raise ProfileNotFoundError(f"Unknown profile: {profile_name}")

        u = url.strip()
        for pattern, sanitized in entries:
            m = pattern.search(u)
            if m:
                pid = self._extract_id(m)
                if not pid:
                    raise ProfileIDExtractionError("Could not extract profile ID")
                pid = pid.strip().lstrip("@").rstrip("/")
                return sanitized.format(id=pid)

        raise URLMismatchError(f"URL does not match profile '{profile_name}'")

    def get_clean_link(self, profile_name: str, profile_id: str) -> str:
        entries = self._compiled.get(profile_name)
        if not entries:
            raise ProfileNotFoundError(f"Unknown profile: {profile_name}")
        pid = profile_id.strip().lstrip("@").rstrip("/")
        sanitized = entries[0][1]
        return sanitized.format(id=pid)

    # ------------------------------------------------------------------
    # Profile CRUD (single + bulk)
    # ------------------------------------------------------------------

    def set_profile(self, name: str, data: Any, *, override: bool = False) -> None:
        """
        Unified add/override method.
        - override=False → error if exists
        - override=True → force replace
        """
        exists = name in self.profiles
        if exists and not override:
            raise ProfileAlreadyExistsError(f"Profile '{name}' already exists. Use override=True.")

        self.profiles[name] = data
        self._compile_profile(name, data)

    def delete_profile(self, name: str) -> None:
        if name not in self.profiles:
            raise ProfileNotFoundError(f"Profile '{name}' not found")
        del self.profiles[name]
        self._compiled.pop(name, None)

    def set_profiles(self, profiles: Dict[str, Any], *, override: bool = False) -> None:
        """
        Bulk add/override.
        """
        if not override:
            conflicts = [name for name in profiles if name in self.profiles]
            if conflicts:
                raise ProfileAlreadyExistsError(f"Profiles already exist: {', '.join(conflicts)}")

        for name, data in profiles.items():
            self.set_profile(name, data, override=override)

    def delete_profiles(self, names: List[str]) -> None:
        missing = [n for n in names if n not in self.profiles]
        if missing:
            raise ProfileNotFoundError(f"Profiles not found: {', '.join(missing)}")
        for n in names:
            self.delete_profile(n)

    def clear_profiles(self) -> None:
        self.profiles.clear()
        self._compiled.clear()

    def get_profile(self, name: str) -> Any:
        if name not in self.profiles:
            raise ProfileNotFoundError(f"Profile '{name}' not found")
        return self.profiles[name]

    def list_profiles(self) -> List[str]:
        return list(self.profiles.keys())
