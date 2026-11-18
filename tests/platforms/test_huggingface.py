import pytest


class TestHuggingface:
    def test_huggingface_accepts_profile_shaped_names(self, sl):
        assert sl.is_valid("huggingface", "https://huggingface.co/settings") is True

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://huggingface.co/meta-llama/", "https://huggingface.co/meta-llama"),
        ],
    )
    def test_huggingface_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "huggingface"
        assert sl.is_valid("huggingface", url) is True
        assert sl.sanitize("huggingface", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://huggingface.co/meta-llama/Llama-3.1-8B",
            "https://huggingface.co/docs/transformers",
        ],
    )
    def test_huggingface_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("huggingface", url) is False
        assert sl.detect_platform(url) != "huggingface"
