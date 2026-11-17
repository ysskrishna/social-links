"""Tests for Weights & Biases platform."""
import pytest


class TestWandb:
    """Test Weights & Biases platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://wandb.ai/ysskrishna", "https://forge.coreweave.com/profile/ysskrishna"),
        ],
    )
    def test_wandb_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "wandb"
        assert sl.is_valid("wandb", url) is True
        assert sl.sanitize("wandb", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://wandb.ai/wandb/projects",
            "https://wandb.ai/site",
            "https://wandb.ai/ysskrishna/my-project",
        ],
    )
    def test_wandb_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("wandb", url) is False
        assert sl.detect_platform(url) != "wandb"
