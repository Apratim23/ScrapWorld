import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

class WebSearch:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def search_google(self, query, num_results=5):
        """
        Search Google for the query and return a list of result URLs.
        This is a basic implementation and might be blocked by Google.
        For production, consider using a proper search API.
        """
        try:
            search_url = f"https://www.google.com/search?q={quote_plus(query)}&num={num_results}"
            response = self.session.get(search_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all result links
            search_results = []
            for result in soup.select('div.g div.yuRUbf a'):
                url = result['href']
                if url.startswith('http') and 'google.com' not in url:
                    search_results.append(url)
            
            return search_results[:num_results]
        
        except Exception as e:
            print(f"Error searching: {str(e)}")
            return []
    
    def get_urls_for_topic(self, topic, num_results=5):
        """Get a list of relevant URLs for a given topic"""
        return self.search_google(topic, num_results)
