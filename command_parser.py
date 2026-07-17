"""
Matus AI Command Parser
Natural language commands को समझता है और action decide करता है
Supports Hindi, English, and Hinglish
"""

import re


class CommandParser:
    """Commands को parse और understand करने वाला class"""
    
    def __init__(self):
        self.command_patterns = {
            'open_app': [
                r'(open|launch|start|चालू|खोल)\s+(whatsapp|youtube|camera|chrome|gallery)',
                r'(whatsapp|youtube|camera|chrome|gallery)\s+(open|चालू|खोल)'
            ],
            'web_search': [
                r'(search|google|find|look up|खोज|ढूंढ|search for)\s+(.+)',
                r'(.+)\s+(search|google|खोज|ढूंढ)'
            ],
            'set_brightness': [
                r'(brightness|ब्राइटनेस)\s+(high|low|medium|तेज़|कम|बीच)',
                r'(increase|decrease|बढ़ा|घटा)\s+brightness',
                r'brightness\s+(to|set)\s+(\d+)'
            ],
            'check_battery': [
                r'(battery|बैटरी)\s+(level|status|check|कितनी|बता)',
                r'(how much|कितनी)\s+battery'
            ],
            'vibrate': [
                r'(vibrate|vibration|वाइब्रेट|वाइब्रेशन)',
            ],
            'help': [
                r'(help|मदद|क्या कर सकते हो|what can you do)'
            ]
        }
    
    def parse(self, command):
        """
        Command को parse करता है और action + parameters return करता है
        """
        cmd_lower = command.lower().strip()
        
        # Check each pattern
        for action, patterns in self.command_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, cmd_lower, re.IGNORECASE)
                if match:
                    return self._extract_action(action, match, command)
        
        # No pattern matched
        return {
            'action': 'unknown',
            'parameters': {},
            'original': command
        }
    
    def _extract_action(self, action, match, original_command):
        """Action और parameters extract करता है"""
        result = {
            'action': action,
            'parameters': {},
            'original': original_command
        }
        
        if action == 'open_app':
            # Extract app name
            apps = ['whatsapp', 'youtube', 'camera', 'chrome', 'gallery']
            for app in apps:
                if app in original_command.lower():
                    result['parameters']['app'] = app
                    break
        
        elif action == 'web_search':
            # Extract search query
            groups = match.groups()
            if len(groups) > 1:
                result['parameters']['query'] = groups[-1].strip()
            else:
                # Remove command words
                query = re.sub(r'(search|google|find|look up|खोज|ढूंढ)', '', 
                             original_command, flags=re.IGNORECASE).strip()
                result['parameters']['query'] = query
        
        elif action == 'set_brightness':
            # Extract brightness level
            if 'high' in original_command.lower() or 'तेज़' in original_command:
                result['parameters']['level'] = 255
            elif 'low' in original_command.lower() or 'कम' in original_command:
                result['parameters']['level'] = 50
            elif 'medium' in original_command.lower() or 'बीच' in original_command:
                result['parameters']['level'] = 128
            else:
                # Try to extract number
                numbers = re.findall(r'\d+', original_command)
                if numbers:
                    result['parameters']['level'] = int(numbers[0])
        
        elif action == 'vibrate':
            # Extract duration if mentioned
            numbers = re.findall(r'\d+', original_command)
            if numbers:
                result['parameters']['duration'] = int(numbers[0]) * 1000
            else:
                result['parameters']['duration'] = 500
        
        return result
    
    def get_help_text(self):
        """Help text return करता है"""
        return """
🤖 **Matus AI Commands:**

📱 **Apps खोलना:**
   • "WhatsApp खोलो"
   • "Open YouTube"
   • "Camera चालू करो"

🔍 **Web Search:**
   • "Search cricket score"
   • "खोजो Python क्या है"
   • "Google weather today"

💡 **Brightness:**
   • "Brightness बढ़ाओ"
   • "Set brightness to 100"
   • "ब्राइटनेस कम करो"

🔋 **Battery:**
   • "Battery check करो"
   • "How much battery"
   • "बैटरी कितनी है"

📳 **Vibrate:**
   • "Vibrate"
   • "Vibrate for 2 seconds"

❓ **Help:**
   • "Help"
   • "क्या कर सकते हो"
"""


# Test
if __name__ == "__main__":
    parser = CommandParser()
    
    test_commands = [
        "WhatsApp खोलो",
        "Search cricket score",
        "Brightness बढ़ाओ",
        "Battery check करो",
        "Vibrate for 3 seconds",
        "Help"
    ]
    
    print("=== Command Parser Test ===\n")
    for cmd in test_commands:
        result = parser.parse(cmd)
        print(f"Command: {cmd}")
        print(f"Parsed: {result}\n")
