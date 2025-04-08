import re
from bs4 import BeautifulSoup
from typing import Optional


def is_valid_url(url: str) -> bool:
    """Check if a URL is valid.
    And yes haha this was chatgpt :3 bc tree"""
    #* and yes haha this is chatgpt :3 bc tree
    regex = re.compile(
        r'^(https?://)?'  # http:// or https://
        r'([a-zA-Z0-9.-]+)'  # domain
        r'(\.[a-zA-Z]{2,})'  # top-level domain
        r'(:\d+)?'  # optional port
        r'(/.*)?$',  # optional path
        re.IGNORECASE
    )
    return re.match(regex, url) is not None


def prettify_html(html: str) -> str:
    """Prettify raw HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify()


def extract_emails(text: str) -> list[str]:
    """Extract all email addresses from a given text."""
    regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(regex, text)


def extract_phone_numbers(text: str) -> list[str]:
    """Extract phone numbers from a given text."""
    regex = r'\+?\d[\d\s()-]{7,}\d'
    return re.findall(regex, text)


def get_base_url(url: str) -> Optional[str]:
    """Extract the base URL from a full URL."""
    match = re.match(r'^(https?://[a-zA-Z0-9.-]+)', url)
    return match.group(1) if match else None
