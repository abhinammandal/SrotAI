import requests


DEFAULT_TIMEOUT = 10

HEADERS = {
    "User-Agent": "SrotAI/0.1 Educational Project"
}


class WebFetchError(Exception):
    """Raised when SrotAI cannot download a webpage."""


def fetch_page(url: str) -> str:
    """Download a webpage and return its HTML content."""

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=DEFAULT_TIMEOUT
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as error:
        raise WebFetchError(
            f"Could not download the webpage: {error}"
        ) from error

    return response.text