"""
WebAgent - Web Access & Scraping Tools
Controlled by Datya
"""

import json

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


class WebAgent:
    """Web fetching, scraping, and API tools"""

    def web_fetch(self, url):
        """Fetch raw HTML/content from a URL"""
        if not HAS_REQUESTS:
            return "Error: requests library not available."
        try:
            response = requests.get(str(url), timeout=15)
            response.raise_for_status()
            return response.text[:3000]
        except Exception as e:
            return f"Fetch error: {str(e)}"

    def web_scrape(self, url):
        """Scrape clean text from a webpage"""
        if not HAS_REQUESTS:
            return "Error: requests library not available."
        if not HAS_BS4:
            return "Error: beautifulsoup4 not available."
        try:
            response = requests.get(str(url), timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # Remove script and style
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()
            text = soup.get_text(separator='\n', strip=True)
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            return '\n'.join(lines)[:3000]
        except Exception as e:
            return f"Scrape error: {str(e)}"

    def web_api_json(self, url):
        """Fetch JSON from an API endpoint"""
        if not HAS_REQUESTS:
            return "Error: requests library not available."
        try:
            response = requests.get(str(url), timeout=15)
            response.raise_for_status()
            return json.dumps(response.json(), indent=2)[:3000]
        except Exception as e:
            return f"API error: {str(e)}"

    def web_search(self, query):
        """Search the web for information"""
        if not HAS_REQUESTS:
            return "Error: requests library not available."
        try:
            search_url = f"https://www.google.com/search?q={query}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36'
            }
            response = requests.get(search_url, headers=headers, timeout=15)
            if HAS_BS4:
                soup = BeautifulSoup(response.text, 'html.parser')
                results = []
                for tag in soup.select('h3'):
                    if tag.string:
                        results.append(tag.string.strip())
                if results:
                    return f"Search results for '{query}':\n" + '\n'.join(f"  - {r}" for r in results[:10])
            return response.text[:1500]
        except Exception as e:
            return f"Search error: {str(e)}"

    def web_get_status(self, url):
        """Check HTTP status code of a URL"""
        if not HAS_REQUESTS:
            return "Error: requests library not available."
        try:
            response = requests.head(str(url), timeout=10, allow_redirects=True)
            return f"URL: {url}\nStatus: {response.status_code} {response.reason}"
        except Exception as e:
            return f"Status check error: {str(e)}"

    def get_tools(self):
        """Return all tools as a dict"""
        return {
            'web_fetch': self.web_fetch,
            'web_scrape': self.web_scrape,
            'web_api_json': self.web_api_json,
            'web_search': self.web_search,
            'web_get_status': self.web_get_status,
        }
