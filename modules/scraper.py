import requests
from bs4 import BeautifulSoup
from llama_index.readers.web import TrafilaturaWebReader
import re
from urllib.parse import urlparse

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def scrape_with_bs4(self, url):
        """Scrape web content using BeautifulSoup"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.extract()
            
            # Get text content
            text = soup.get_text(separator='\n')
            
            # Clean up text: remove extra newlines and whitespace
            clean_text = re.sub(r'\n+', '\n', text).strip()
            clean_text = re.sub(r'\s+', ' ', clean_text)
            
            # Extract title
            title = soup.title.string if soup.title else "No title found"
            
            # Extract domain
            domain = urlparse(url).netloc
            
            return {
                "url": url,
                "title": title,
                "domain": domain,
                "content": clean_text
            }
        except Exception as e:
            return {
                "url": url,
                "error": str(e),
                "content": None
            }

    def scrape_with_llamaindex(self, url):
        """Scrape web content using LlamaIndex's SimpleWebPageReader"""
        try:
            SimpleWebPageReader = download_loader("SimpleWebPageReader")
            loader = SimpleWebPageReader()
            documents = loader.load_data(urls=[url])

            if documents and len(documents) > 0:
                return {
                    "url": url,
                    "title": documents[0].metadata.get("title", "No title found"),
                    "domain": urlparse(url).netloc,
                    "content": documents[0].text
                }
            else:
                return {
                    "url": url,
                    "error": "No content found",
                    "content": None
                }
        except Exception as e:
            return {
                "url": url,
                "error": str(e),
                "content": None
            }
