"""
Matus AI Web Search Module
DuckDuckGo API का use करके web search करता है
No API key required - completely free
"""

import requests
import json
from urllib.parse import quote_plus


class WebSearch:
    """Web search करने वाला class"""
    
    def __init__(self):
        self.base_url = "https://api.duckduckgo.com/"
    
    def search(self, query, max_results=3):
        """
        Web search करता है और results return करता है
        """
        try:
            # Prepare URL
            encoded_query = quote_plus(query)
            url = f"{self.base_url}?q={encoded_query}&format=json&no_html=1"
            
            # Make request
            headers = {
                'User-Agent': 'MatusAI/1.0 (Android App)'
            }
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return self._format_results(data, max_results)
            else:
                return f"❌ Search failed with status: {response.status_code}"
        
        except requests.exceptions.Timeout:
            return "❌ Search timeout - please check internet"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def _format_results(self, data, max_results):
        """Search results को format करता है"""
        results = []
        
        # Abstract (main answer)
        if data.get('AbstractText'):
            results.append(f"📝 {data['AbstractText']}")
            if data.get('AbstractSource'):
                results.append(f"   Source: {data['AbstractSource']}")
        
        # Related topics
        if data.get('RelatedTopics'):
            for i, topic in enumerate(data['RelatedTopics'][:max_results]):
                if isinstance(topic, dict) and topic.get('Text'):
                    results.append(f"\n{i+1}. {topic['Text']}")
                    if topic.get('FirstURL'):
                        results.append(f"   Link: {topic['FirstURL']}")
        
        if not results:
            return "❓ No results found. Try different keywords."
        
        return "\n".join(results)
    
    def quick_answer(self, query):
        """
        Quick answer देता है (definitions, calculations, etc.)
        """
        try:
            encoded_query = quote_plus(query)
            url = f"{self.base_url}?q={encoded_query}&format=json"
            
            response = requests.get(url, timeout=5)
            data = response.json()
            
            # Answer type
            if data.get('AnswerType'):
                return f"✅ {data.get('Answer', 'No answer')}"
            
            # Definition
            if data.get('Definition'):
                return f"📖 {data['Definition']}"
            
            return "❓ No quick answer available"
        
        except Exception as e:
            return f"❌ Error: {str(e)}"


# Test
if __name__ == "__main__":
    search = WebSearch()
    
    print("=== Web Search Test ===")
    print("\n1. Searching 'cricket score':")
    print(search.search("cricket score"))
    
    print("\n2. Quick answer 'what is python':")
    print(search.quick_answer("what is python"))
