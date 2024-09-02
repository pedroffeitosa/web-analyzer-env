import sys
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

def extract_text_from_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text

def identify_sections(text_content):
    summarizer = pipeline("summarization")
    summary = summarizer(text_content, max_length=100, min_length=50, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.example.com"
    text_content = extract_text_from_html(url)
    sections = identify_sections(text_content)
    print("Identified Sections:")
    print(sections)
