# services/http_client.py
import requests

from typing import Optional, Dict, Any


class HttpClient:
    def __init__(
        self, headers: Optional[Dict[str, Any]] = None, timeout: int = 10
    ):
        self.headers = headers or {}
        self.timeout = timeout

    def get_as_text(self, url: str, params: Optional[Dict[str, Any]] = None):
        response = requests.get(
            url, headers=self.headers, params=params, timeout=self.timeout
        )
        response.raise_for_status()
        return response.text

    def get_as_json(self, url: str, params: Optional[Dict[str, Any]] = None):
        response = requests.get(
            url, headers=self.headers, params=params, timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
