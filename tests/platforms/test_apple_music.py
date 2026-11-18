class TestAppleMusic:
    def test_apple_music(self, sl):
        
        
        test_cases = [
            ('https://music.apple.com/us/artist/the-beatles/136975', 'https://music.apple.com/artist/136975'),
            ('https://music.apple.com/us/artist/beatles/136975', 'https://music.apple.com/artist/136975'),
            ('https://music.apple.com/artist/beatles/136975', 'https://music.apple.com/artist/136975'),
            ('https://music.apple.com/artist/136975', 'https://music.apple.com/artist/136975'),
            ('https://itunes.apple.com/us/artist/id136975', 'https://music.apple.com/artist/136975'),
        ]
        for source, expected in test_cases:
            assert sl.is_valid("apple_music", source) is True
            assert sl.sanitize("apple_music", source) == expected
