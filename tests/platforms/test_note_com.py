import pytest


class TestNoteCom:
    @pytest.mark.parametrize(
        "url",
        [
            "https://note.com/info/n/n1234abcd",
            "https://note.com/hashtag/note",
        ],
    )
    def test_note_com_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("note_com", url) is False
        assert sl.detect_platform(url) != "note_com"
