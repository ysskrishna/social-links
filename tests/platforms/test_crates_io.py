import pytest


class TestCratesIo:
    @pytest.mark.parametrize(
        "url",
        [
            "https://crates.io/crates/serde",
            "https://crates.io/teams/github:rust-lang:core",
        ],
    )
    def test_crates_io_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("crates_io", url) is False
        assert sl.detect_platform(url) != "crates_io"
