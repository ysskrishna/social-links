import pytest


class TestAudioboom:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://audioboom.com/channels/4256218", "https://audioboom.com/channels/4256218"),
        ],
    )
    def test_audioboom_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "audioboom"
        assert sl.is_valid("audioboom", url) is True
        assert sl.sanitize("audioboom", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://audioboom.com/posts/123-title",
            "https://audioboom.com/channels/no-such-thing",
        ],
    )
    def test_audioboom_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("audioboom", url) is False
        assert sl.detect_platform(url) != "audioboom"
