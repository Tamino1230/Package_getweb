# GetWeb

`GetWeb` is a Python package designed to simplify web scraping and HTTP requests. It provides utilities for fetching web pages, extracting content, and downloading files.

`I actually made it because im to dumb for bs4 and requests`  
*Note: This package was created to provide a simpler alternative to using libraries like BeautifulSoup and Requests directly.*
My Discord: [Tamino1230](https://discord.com/users/702893526303637604)

## Features

- Perform GET and POST requests with error handling.
- Download files from URLs.
- Extract text, links, and images from web pages.
- Search for elements by tag, ID, or class using BeautifulSoup.
- Fetch metadata, titles, and headings from web pages.
- Retrieve HTTP headers from URLs.

## Installation

### Option 1: Manual Installation

1. Download or clone this repository.
2. Place the `GetWeb` folder in your project directory.
3. Ensure the `GetWeb` folder contains the `getweb` module.

### Option 1.5: Insert Local Python Folder

To add the `GetWeb` package to your local Python environment, follow these steps:

1. Find the folder where Python is installed on your computer:
    - **Windows**: Look for one of these paths:
        - `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<version>\Lib\site-packages`
        - `C:\Python<version>\Lib\site-packages` / `C:\Python<version>\Lib` (if Python is installed directly in `C:\Python`)
    - **macOS/Linux**: Check one of these paths:
        - `/usr/local/lib/python<version>/site-packages`
        - `~/.local/lib/python<version>/site-packages`

2. Copy the `GetWeb` folder into the `site-packages` or `Lib (only Windows)` directory.

3. Verify the installation by running the following command in your Python environment:

    ```python
    import getweb
    print("getweb package installed successfully!")
    ```

### Option 2: Using `pip`

(Not yet available on PyPI. Use manual installation for now.)

## Usage

### Importing the Package

```python
from getweb import getweb
```

### Example: Fetching a Web Page

```python
# Initialize the getweb object with a URL
web = getweb("https://example.com")

# Fetch the page content
web.fetch()

# Get the text content of the page
print(web.get_text())

# Get all links on the page
print(web.get_links())

# Get all image sources on the page
print(web.get_images())
```

### Example: Searching for Elements

```python
# Find all elements with a specific tag
print(web.find_by_tag("p"))

# Find an element by its ID
print(web.find_by_id("main-content"))

# Find all elements with a specific class
print(web.find_by_class("highlight"))

# Find elements by a specific attribute
print(web.find_by_attribute("data-role", "button"))
```

### Example: Extracting Metadata and Headings

```python
# Get all meta tags
print(web.get_meta_tags())

# Get the title of the page
print(web.get_title())

# Get all headings (h1 to h6)
print(web.get_headings())

# Get headings of a specific level (e.g., h2)
print(web.get_headings(level=2))
```

### Example: Downloading a File

```python
from GetWeb.getweb.response import download_file

# Download a file from a URL
success = download_file("https://example.com/file.zip", "file.zip")
if success:
    print("File downloaded successfully!")
else:
    print("Failed to download the file.")
```

### Example: Fetching Headers

```python
from GetWeb.getweb.response import get_headers

# Get headers from a URL
headers = get_headers("https://example.com")
if headers:
    print(headers)
else:
    print("Failed to fetch headers.")
```

### Additional Utilities

The `GetWeb` package also includes utility functions for common web-related tasks:

#### Example: Validating a URL

```python
from GetWeb.getweb.utils import is_valid_url

# Check if a URL is valid
url = "https://example.com"
if is_valid_url(url):
    print(f"{url} is valid!")
else:
    print(f"{url} is not valid.")
```

#### Example: Prettifying HTML

```python
from GetWeb.getweb.utils import prettify_html

# Prettify raw HTML content
raw_html = "<html><body><h1>Title</h1></body></html>"
pretty_html = prettify_html(raw_html)
print(pretty_html)
```

#### Example: Extracting Emails

```python
from GetWeb.getweb.utils import extract_emails

# Extract email addresses from text
text = "Contact us at support@example.com or sales@example.org." # text could be the HTML
emails = extract_emails(text)
print(emails)
```

#### Example: Extracting Phone Numbers

```python
from GetWeb.getweb.utils import extract_phone_numbers

# Extract phone numbers from text
text = "Call us at +1-800-555-1234 or (123) 456-7890." # text could be the HTML
phone_numbers = extract_phone_numbers(text)
print(phone_numbers)
```

#### Example: Getting the Base URL

```python
from GetWeb.getweb.utils import get_base_url

# Extract the base URL from a full URL
full_url = "https://example.com/path/to/resource"
base_url = get_base_url(full_url)
print(base_url)
```
