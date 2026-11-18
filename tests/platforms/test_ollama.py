import pytest


class TestOllama:
    @pytest.mark.parametrize(
        "url",
        [
            "https://ollama.com/library/llama3",
            "https://ollama.com/jmorganca/llama3",
        ],
    )
    def test_ollama_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("ollama", url) is False
        assert sl.detect_platform(url) != "ollama"
