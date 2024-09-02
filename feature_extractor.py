from bs4 import BeautifulSoup
import requests
from config import URL  # Import the centralized URL

def extract_features(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example features: number of sections, presence of viewport meta tag, content length
    num_sections = len(soup.find_all('section'))
    has_viewport = bool(soup.find('meta', {'name': 'viewport'}))
    content_length = len(soup.get_text())

    # Additional features (example):
    num_images = len(soup.find_all('img'))
    num_links = len(soup.find_all('a'))
    num_headings = len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))
    text_to_html_ratio = len(soup.get_text()) / len(str(soup))  # Ratio of text length to HTML length
    has_meta_description = bool(soup.find('meta', attrs={"name": "description"}))
    title_length = len(soup.title.string) if soup.title else 0

    # Ensure that 9 elements are returned
    return [
        num_sections, has_viewport, content_length, num_images,
        num_links, num_headings, text_to_html_ratio, has_meta_description, title_length
    ]
