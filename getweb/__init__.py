# getweb.py
import getweb.response as resp
import getweb.utils as utils
from bs4 import BeautifulSoup

__author__ = "https://github.com/Tamino1230"
__repo__ = ""
__all__ = ["getweb", resp, utils, "BeautifulSoup", "requests"]
__version__ = "v0.0.1"

class getweb:
    def __init__(self, url: str):
        self.url = url
        self.page = None
        self.soup = None

    def fetch(self):
        self.page = resp.get(self.url)
        if self.page:
            self.soup = BeautifulSoup(self.page.text, 'html.parser')
        else:
            self.soup = None

    def get_text(self):
        if self.soup:
            return self.soup.get_text(strip=True)
        return "No content"

    def get_links(self):
        if not self.soup:
            return []
        return [a['href'] for a in self.soup.find_all('a', href=True)]

    def get_images(self):
        if not self.soup:
            return []
        return [img['src'] for img in self.soup.find_all('img', src=True)]

    def find_by_tag(self, tag: str):
        if self.soup:
            return self.soup.find_all(tag)
        return []

    def find_by_id(self, element_id: str):
        if self.soup:
            return self.soup.find(id=element_id)
        return None

    def find_by_class(self, class_name: str):
        if self.soup:
            return self.soup.find_all(class_=class_name)
        return []

    def find_by_attribute(self, attr_name: str, attr_value: str):
        if self.soup:
            return self.soup.find_all(attrs={attr_name: attr_value})
        return []

    def get_meta_tags(self):
        if self.soup:
            return self.soup.find_all('meta')
        return []

    def get_title(self):
        if self.soup:
            title_tag = self.soup.find('title')
            return title_tag.string if title_tag else None
        return None

    def get_headings(self, level: int = None):
        if not self.soup:
            return []
        if level:
            return self.soup.find_all(f'h{level}')
        return [self.soup.find_all(f'h{i}') for i in range(1, 7)]