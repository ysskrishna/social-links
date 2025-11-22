from typing import Dict, List, Any

PREDEFINED_PROFILES: Dict[str, List[Dict[str, Any]]] = {
    "linkedin": [
        {
            "patterns": [
                "https?://(www\\.)?linkedin\\.com/in/(?P<id>[A-Za-z0-9_-]+)/?/?$"
            ],
            "sanitized": "https://www.linkedin.com/in/{id}/"
        },
        {
            "patterns": [
                "https?://(www\\.)?linkedin\\.com/company/(?P<id>[A-Za-z0-9_-]+)/?/?$"
            ],
            "sanitized": "https://www.linkedin.com/company/{id}/"
        }
    ],
    "twitter": [
        {
            "patterns": [
                "https?://(www\\.)?twitter\\.com/(?P<id>[A-Za-z0-9_-]+)/?/?$"
            ],
            "sanitized": "https://www.twitter.com/{id}/"
        }
    ],
    "facebook": [
        {
            "patterns": [
                "https?://(www\\.)?facebook\\.com/(?P<id>[A-Za-z0-9_-]+)/?/?$"
            ],
            "sanitized": "https://www.facebook.com/{id}/"
        }
    ]
}
