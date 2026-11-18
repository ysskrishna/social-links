class TestFlickr:
    def test_flickr_with_at_symbol(self, sl):
        profile_id = "123456@N01"
        assert sl.is_valid("flickr", profile_id) is True
        assert sl.sanitize("flickr", profile_id) == f"https://www.flickr.com/people/{profile_id}"
