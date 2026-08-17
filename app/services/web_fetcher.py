import requests


DEFAULT_TIMEOUT = 10

HEADERS = {
    "User-Agent": "SrotAI/0.1 Educational Project"
}


def fetch_page(url: str) -> str:
    """Download a webpage and return its HTML content."""

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=DEFAULT_TIMEOUT
    )

    response.raise_for_status()

    return response.text