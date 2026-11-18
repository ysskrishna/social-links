"""Tests for Steam platform."""


class TestSteam:
    """Test Steam platform"""

    def test_steam_profiles(self, sl):
        """Test Steam platform with /profiles/ path (numeric Steam ID)"""
        steam_id = "76561198014898339"
        assert sl.detect_platform(f"https://steamcommunity.com/profiles/{steam_id}") == "steam"
        assert sl.is_valid("steam", f"https://steamcommunity.com/profiles/{steam_id}") is True
        # Profiles path should be preserved (not converted to /id/)
        assert sl.sanitize("steam", f"https://steamcommunity.com/profiles/{steam_id}") == f"https://steamcommunity.com/profiles/{steam_id}"
