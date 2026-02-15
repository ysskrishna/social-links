"""Tests for Docker Hub platform."""
import pytest


class TestDockerHub:
    """Test Docker Hub platform"""

    def test_dockerhub(self, sl):
        """Test Docker Hub platform"""
        profile_id = "ysskrishna"
        assert sl.detect_platform(f"https://hub.docker.com/u/{profile_id}") == "dockerhub"
        assert sl.is_valid("dockerhub", f"https://hub.docker.com/u/{profile_id}") is True
        assert sl.sanitize("dockerhub", f"https://hub.docker.com/u/{profile_id}") == f"https://hub.docker.com/u/{profile_id}"
        # Test docker.com URL
        assert sl.is_valid("dockerhub", f"https://docker.com/u/{profile_id}") is True
        assert sl.sanitize("dockerhub", f"https://docker.com/u/{profile_id}") == f"https://hub.docker.com/u/{profile_id}"
        # Test direct username
        assert sl.is_valid("dockerhub", profile_id) is True
        assert sl.sanitize("dockerhub", profile_id) == f"https://hub.docker.com/u/{profile_id}"

