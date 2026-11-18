import pytest


class TestSketchfab:
    @pytest.mark.parametrize(
        "url",
        [
            "https://sketchfab.com/3d-models/abc-123",
            "https://sketchfab.com/sketchfab/models",
        ],
    )
    def test_sketchfab_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("sketchfab", url) is False
        assert sl.detect_platform(url) != "sketchfab"
