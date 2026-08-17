from unittest.mock import Mock, patch

import pytest
import requests

from app.services.web_fetcher import (
    DEFAULT_TIMEOUT,
    HEADERS,
    WebFetchError,
    fetch_page,
)


@patch("app.services.web_fetcher.requests.get")
def test_fetch_page_returns_html(mock_get):
    fake_response = Mock()
    fake_response.text = "<html><body>Example</body></html>"
    fake_response.raise_for_status.return_value = None

    mock_get.return_value = fake_response

    result = fetch_page("https://example.com")

    assert result == "<html><body>Example</body></html>"

    mock_get.assert_called_once_with(
        "https://example.com",
        headers=HEADERS,
        timeout=DEFAULT_TIMEOUT,
    )


@patch("app.services.web_fetcher.requests.get")
def test_fetch_page_converts_request_error(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout(
        "The request timed out."
    )

    with pytest.raises(WebFetchError, match="Could not download"):
        fetch_page("https://example.com")
    