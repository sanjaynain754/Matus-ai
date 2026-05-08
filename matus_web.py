import requests
from bs4 import BeautifulSoup
import json

class MatusWeb:
    @staticmethod
    def fetch_url(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            return f"Error fetching URL: {e}"

    @staticmethod
    def scrape_text(url):
        try:
            html = MatusWeb.fetch_url(url)
            if html.startswith("Error"):
                return html
            soup = BeautifulSoup(html, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text()
            # Break into lines and remove leading/trailing whitespace
            lines = (line.strip() for line in text.splitlines())
            # Break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # Drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)
            return text
        except Exception as e:
            return f"Error scraping text: {e}"

    @staticmethod
    def get_json_api(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def search_web(query):
        # Using a simple duckduckgo-style redirect or similar public search if possible
        # For now, we'll simulate a search by providing a way to get data from a search engine result page
        search_url = f"https://www.google.com/search?q={query}"
        return MatusWeb.scrape_text(search_url)

def inject_web_tools(interpreter):
    web = MatusWeb()
    interpreter.variables['web_fetch'] = web.fetch_url
    interpreter.variables['web_scrape'] = web.scrape_text
    interpreter.variables['web_api_json'] = web.get_json_api
    interpreter.variables['web_search'] = web.search_web
