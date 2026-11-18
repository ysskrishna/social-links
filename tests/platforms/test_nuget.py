import pytest


class TestNuget:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.nuget.org/packages/Newtonsoft.Json",
            "https://www.nuget.org/profiles/Microsoft/packages",
        ],
    )
    def test_nuget_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("nuget", url) is False
        assert sl.detect_platform(url) != "nuget"
