class TestReddit:
    def test_reddit_u_path(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://reddit.com/u/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"https://reddit.com/u/{profile_id}") is True
        assert sl.sanitize("reddit", f"https://reddit.com/u/{profile_id}") == f"https://reddit.com/user/{profile_id}"

    def test_reddit_old(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://old.reddit.com/user/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"https://old.reddit.com/user/{profile_id}") is True
        assert sl.sanitize("reddit", f"https://old.reddit.com/user/{profile_id}") == f"https://reddit.com/user/{profile_id}"
        assert sl.detect_platform(f"https://old.reddit.com/u/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"https://old.reddit.com/u/{profile_id}") is True
        assert sl.sanitize("reddit", f"https://old.reddit.com/u/{profile_id}") == f"https://reddit.com/user/{profile_id}"

    def test_reddit_u_prefix(self, sl):
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"u/{profile_id}") == "reddit"
        assert sl.is_valid("reddit", f"u/{profile_id}") is True
        assert sl.sanitize("reddit", f"u/{profile_id}") == f"https://reddit.com/user/{profile_id}"

    def test_reddit_subreddit(self, sl):
        subreddit_name = "python"
        assert sl.detect_platform(f"https://reddit.com/r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"https://reddit.com/r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"https://reddit.com/r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"

    def test_reddit_subreddit_variations(self, sl):
        subreddit_name = "learnprogramming"
        
        assert sl.detect_platform(f"https://www.reddit.com/r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"https://www.reddit.com/r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"https://www.reddit.com/r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"
        
        assert sl.detect_platform(f"https://old.reddit.com/r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"https://old.reddit.com/r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"https://old.reddit.com/r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"
        
        assert sl.is_valid("reddit", f"https://reddit.com/r/{subreddit_name}/") is True
        assert sl.sanitize("reddit", f"https://reddit.com/r/{subreddit_name}/") == f"https://reddit.com/r/{subreddit_name}"
        
        assert sl.detect_platform(f"http://reddit.com/r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"http://reddit.com/r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"http://reddit.com/r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"

    def test_reddit_subreddit_r_prefix(self, sl):
        subreddit_name = "python"
        assert sl.detect_platform(f"r/{subreddit_name}") == "reddit"
        assert sl.is_valid("reddit", f"r/{subreddit_name}") is True
        assert sl.sanitize("reddit", f"r/{subreddit_name}") == f"https://reddit.com/r/{subreddit_name}"
