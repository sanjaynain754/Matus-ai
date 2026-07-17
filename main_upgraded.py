"""
Matus AI - Upgraded Main File
सभी modules को integrate करता है
"""

import os
import sys

# Import all modules
try:
    from phone_controller import PhoneController
    from voice_input import VoiceInput
    from web_search_enhanced import WebSearch
    from command_parser import CommandParser
    from battery_optimizer import BatteryOptimizer
    MODULES_LOADED = True
except ImportError as e:
    print(f"Warning: Some modules not loaded - {e}")
    MODULES_LOADED = False


class MatusAI:
    """Main AI class जो सब कुछ control करता है"""
    
    def __init__(self):
        print("🤖 Initializing Matus AI...")
        
        # Initialize all modules
        if MODULES_LOADED:
            self.phone = PhoneController()
            self.voice = VoiceInput()
            self.search = WebSearch()
            self.parser = CommandParser()
            self.battery = BatteryOptimizer()
            print("✅ All modules loaded successfully")
        else:
            print("⚠️ Running in limited mode")
    
    def process_command(self, command):
        """
        Main command processor
        Command को parse करता है और appropriate action लेता है
        """
        if not command or not command.strip():
            return "❓ Please enter a command"
        
        print(f"\n📥 Processing: {command}")
        
        # Parse command
        parsed = self.parser.parse(command)
        action = parsed['action']
        params = parsed['parameters']
        
        print(f"🔍 Parsed action: {action}")
        print(f"📋 Parameters: {params}")
        
        # Execute action
        if action == 'open_app':
            app = params.get('app', '')
            return self._handle_open_app(app)
        
        elif action == 'web_search':
            query = params.get('query', '')
            return self._handle_web_search(query)
        
        elif action == 'set_brightness':
            level = params.get('level', 128)
            return self.phone.set_brightness(level)
        
        elif action == 'check_battery':
            return self.battery.get_battery_status()
        
        elif action == 'vibrate':
            duration = params.get('duration', 500)
            return self.phone.vibrate(duration)
        
        elif action == 'help':
            return self.parser.get_help_text()
        
        else:
            return f"❓ Command not understood: {command}\n\nType 'help' to see available commands"
    
    def _handle_open_app(self, app_name):
        """App open करने का handler"""
        app_map = {
            'whatsapp': 'com.whatsapp',
            'youtube': 'com.google.android.youtube',
            'camera': 'com.android.camera',
            'chrome': 'com.android.chrome',
            'gallery': 'com.google.android.apps.photos'
        }
        
        package = app_map.get(app_name.lower())
        if package:
            return self.phone.open_app(package)
        else:
            return f"❌ Unknown app: {app_name}"
    
    def _handle_web_search(self, query):
        """Web search का handler"""
        if not query:
            return "❓ What do you want to search?"
        
        print(f"🔍 Searching for: {query}")
        return self.search.search(query)
    
    def interactive_mode(self):
        """Interactive mode - continuously takes commands"""
        print("\n" + "="*50)
        print("🤖 Matus AI - Interactive Mode")
        print("="*50)
        print("Type 'exit' or 'quit' to stop")
        print("Type 'help' to see commands")
        print("="*50 + "\n")
        
        while True:
            try:
                command = input("🗣️ You: ").strip()
                
                if command.lower() in ['exit', 'quit', 'bye', 'बाय']:
                    print("👋 Goodbye!")
                    break
                
                if command:
                    result = self.process_command(command)
                    print(f"\n🤖 AI: {result}\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")


# Main entry point
if __name__ == "__main__":
    ai = MatusAI()
    
    # Check if running with command line argument
    if len(sys.argv) > 1:
        # Single command mode
        command = ' '.join(sys.argv[1:])
        result = ai.process_command(command)
        print(result)
    else:
        # Interactive mode
        ai.interactive_mode()
