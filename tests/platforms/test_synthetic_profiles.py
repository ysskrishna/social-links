import pytest


@pytest.mark.parametrize(
    "platform,url,profile_id,canonical",
    [
        ("huggingface", "https://huggingface.co/example-test-user/", "example-test-user", "https://huggingface.co/example-test-user"),
        ("replicate", "https://replicate.com/example-test-user/", "example-test-user", "https://replicate.com/example-test-user"),
        ("atcoder", "https://atcoder.jp/users/Example_Test_123", "Example_Test_123", "https://atcoder.jp/users/Example_Test_123"),
        ("lobsters", "https://lobste.rs/~example_test", "example_test", "https://lobste.rs/~example_test"),
        ("stack_exchange", "https://stackexchange.com/users/123456789", "123456789", "https://stackexchange.com/users/123456789"),
    ],
)
def test_synthetic_profile(sl, platform, url, profile_id, canonical):
    assert sl.detect_platform(url) == platform
    assert sl.extract_id(platform, url) == profile_id
    assert sl.sanitize(platform, url) == canonical
    assert sl.sanitize(platform, profile_id) == canonical
    assert sl.detect_platform(profile_id) is None
