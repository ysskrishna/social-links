from typing import Dict, List, Any

PREDEFINED_PLATFORMS: Dict[str, List[Dict[str, Any]]] = {
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
    "facebook": [
        {
            "patterns": [
                "https?://(www\\.)?facebook\\.com/(?P<id>[A-Za-z0-9_-]+)/?/?$"
            ],
            "sanitized": "https://www.facebook.com/{id}/"
        }
    ]
}

