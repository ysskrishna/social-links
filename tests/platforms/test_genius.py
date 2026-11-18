import pytest


class TestGenius:
    @pytest.mark.parametrize(
        "url",
        [
            "https://genius.com/Kendrick-lamar-humble-lyrics",
            "https://genius.com/artists/Kendrick-lamar",
            "https://genius.com/albums/Kendrick-lamar/Damn",
            "https://genius.com/Drake-gods-plan-annotated",
        ],
    )
    def test_genius_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("genius", url) is False
        assert sl.detect_platform(url) != "genius"
