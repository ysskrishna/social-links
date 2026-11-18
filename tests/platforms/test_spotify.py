class TestSpotify:
    def test_spotify_artist_uri(self, sl):
        artist_id = "3WrFJ7ztbogyGnTHbHJFl2"
        uri = f"spotify:artist:{artist_id}"
        assert sl.detect_platform(uri) == "spotify"
        assert sl.is_valid("spotify", uri) is True
        assert sl.sanitize("spotify", uri) == f"https://open.spotify.com/artist/{artist_id}"

    def test_spotify_user(self, sl):
        user_id = "vanesamartinoficial"
        assert sl.detect_platform(f"https://open.spotify.com/user/{user_id}") == "spotify"
        assert sl.is_valid("spotify", f"https://open.spotify.com/user/{user_id}") is True
        assert sl.sanitize("spotify", f"https://open.spotify.com/user/{user_id}") == f"https://open.spotify.com/user/{user_id}"
        
    def test_spotify_user_long_id(self, sl):
        user_id = "31wwwnrvhv3i2l2z43ipcmpapoya"
        assert sl.detect_platform(f"https://open.spotify.com/user/{user_id}") == "spotify"
        assert sl.is_valid("spotify", f"https://open.spotify.com/user/{user_id}") is True
        assert sl.sanitize("spotify", f"https://open.spotify.com/user/{user_id}") == f"https://open.spotify.com/user/{user_id}"
