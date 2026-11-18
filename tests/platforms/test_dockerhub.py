class TestDockerHub:
    def test_dockerhub(self, sl):
        profile_id = "ysskrishna"
        assert sl.is_valid("dockerhub", f"https://docker.com/u/{profile_id}") is True
        assert sl.sanitize("dockerhub", f"https://docker.com/u/{profile_id}") == f"https://hub.docker.com/u/{profile_id}"
