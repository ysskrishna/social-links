"""Tests for Exercism platform."""


class TestExercism:
    """Test Exercism platform"""

    def test_exercism_legacy_io_domain(self, sl):
        """exercism.io redirects (301) to exercism.org and is still accepted as input"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://exercism.io/profiles/{profile_id}") == "exercism"
        assert sl.is_valid("exercism", f"https://www.exercism.io/profiles/{profile_id}") is True
        assert sl.sanitize("exercism", f"https://exercism.io/profiles/{profile_id}") == f"https://exercism.org/profiles/{profile_id}"
