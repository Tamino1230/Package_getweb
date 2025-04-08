# response.py
import requests
from typing import Optional, Dict, Any


def get(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, str]] = None,
    timeout: int = 10,
    allow_redirects: bool = True
) -> Optional[requests.Response]:
    """GET request with basic error handling."""
    try:
        resp = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=timeout,
            allow_redirects=allow_redirects
        )
        resp.raise_for_status()
        return resp
    except requests.RequestException as e:
        print(f"[ERROR][GET] {url} → {e}")
        return None


def post(
    url: str,
    data: Optional[Dict[str, Any]] = None,
    json: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 10
) -> Optional[requests.Response]:
    """POST request with form or JSON data."""
    try:
        resp = requests.post(
            url,
            data=data,
            json=json,
            headers=headers,
            timeout=timeout
        )
        resp.raise_for_status()
        return resp
    except requests.RequestException as e:
        print(f"[ERROR][POST] {url} → {e}")
        return None


def download_file(url: str, filepath: str, chunk_size: int = 1024) -> bool:
    """Downloads a file from a URL and saves it locally."""
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
        return True
    except requests.RequestException as e:
        print(f"[ERROR][DOWNLOAD] {url} → {e}")
        return False


def get_headers(url: str) -> Optional[Dict[str, str]]:
    """Gets the headers from a URL without downloading the body."""
    try:
        resp = requests.head(url)
        resp.raise_for_status()
        return dict(resp.headers)
    except requests.RequestException as e:
        print(f"[ERROR][HEAD] {url} → {e}")
        return None
