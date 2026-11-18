"""Tests for Docker Hub platform."""


class TestDockerHub:
    """Test Docker Hub platform"""

    def test_dockerhub(self, sl):
        """Test Docker Hub platform"""
        profile_id = "ysskrishna"
        # Test docker.com URL
        assert sl.is_valid("dockerhub", f"https://docker.com/u/{profile_id}") is True
        assert sl.sanitize("dockerhub", f"https://docker.com/u/{profile_id}") == f"https://hub.docker.com/u/{profile_id}"
