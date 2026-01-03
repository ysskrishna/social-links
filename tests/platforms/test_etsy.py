"""Tests for Etsy platform."""
import pytest


class TestEtsy:
    """Test Etsy platform"""

    def test_etsy(self, sl):
        """Test Etsy platform"""
        shop_name = "MyShopName"
        assert sl.detect_platform(f"https://etsy.com/shop/{shop_name}") == "etsy"
        assert sl.is_valid("etsy", f"https://etsy.com/shop/{shop_name}") is True
        assert sl.sanitize("etsy", f"https://etsy.com/shop/{shop_name}") == f"https://etsy.com/shop/{shop_name}"
        # Test direct shop name
        assert sl.is_valid("etsy", shop_name) is True
        assert sl.sanitize("etsy", shop_name) == f"https://etsy.com/shop/{shop_name}"

    def test_etsy_with_www(self, sl):
        """Test Etsy with www subdomain"""
        shop_name = "MyShopName"
        assert sl.detect_platform(f"https://www.etsy.com/shop/{shop_name}") == "etsy"
        assert sl.is_valid("etsy", f"https://www.etsy.com/shop/{shop_name}") is True
        assert sl.sanitize("etsy", f"https://www.etsy.com/shop/{shop_name}") == f"https://etsy.com/shop/{shop_name}"

    def test_etsy_with_http(self, sl):
        """Test Etsy with http protocol"""
        shop_name = "MyShopName"
        assert sl.detect_platform(f"http://etsy.com/shop/{shop_name}") == "etsy"
        assert sl.is_valid("etsy", f"http://etsy.com/shop/{shop_name}") is True
        assert sl.sanitize("etsy", f"http://etsy.com/shop/{shop_name}") == f"https://etsy.com/shop/{shop_name}"

    def test_etsy_with_trailing_slash(self, sl):
        """Test Etsy with trailing slash"""
        shop_name = "MyShopName"
        assert sl.is_valid("etsy", f"https://etsy.com/shop/{shop_name}/") is True
        assert sl.sanitize("etsy", f"https://etsy.com/shop/{shop_name}/") == f"https://etsy.com/shop/{shop_name}"

