import pytest


class TestScratch:
    @pytest.mark.parametrize(
        "url",
        [
            "https://scratch.mit.edu/projects/10128407/",
            "https://scratch.mit.edu/users/griffpatch/projects/",
        ],
    )
    def test_scratch_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("scratch", url) is False
        assert sl.detect_platform(url) != "scratch"
