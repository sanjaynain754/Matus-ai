"""
Matus AI Phone Controller
यह module phone को control करने के लिए है
Android पर pyjnius और android module का use करता है
"""

import os
import sys

# Check if we're running on Android
ANDROID = 'ANDROID_ARGUMENT' in os.environ

if ANDROID:
    try:
        from android.permissions import request_permissions, Permission
        from jnius import autoclass
        # Android Java classes
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        Context = autoclass('android.content.Context')
        Settings = autoclass('android.provider.Settings')
        ANDROID_READY = True
    except Exception as e:
        print(f"Android import error: {e}")
        ANDROID_READY = False
else:
    ANDROID_READY = False
    print("Running on desktop - phone control disabled")


class PhoneController:
    """Phone को control करने वाला main class"""
    
    def __init__(self):
        self.activity = None
        self.context = None
        if ANDROID_READY:
            try:
                self.activity = PythonActivity.mActivity
                self.context = self.activity.getApplicationContext()
            except Exception as e:
                print(f"Activity init error: {e}")
    
    def open_app(self, package_name):
        """
        कोई भी app खोलता है
        Example: open_app("com.whatsapp")
        """
        if not ANDROID_READY:
            return "Error: Android पर नहीं चल रहा"
        
        try:
            intent = self.context.getPackageManager().getLaunchIntentForPackage(package_name)
            if intent:
                self.activity.startActivity(intent)
                return f"✅ {package_name} खुल गया"
            else:
                return f"❌ App नहीं मिला: {package_name}"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def open_whatsapp(self):
        """WhatsApp खोलता है"""
        return self.open_app("com.whatsapp")
    
    def open_youtube(self):
        """YouTube खोलता है"""
        return self.open_app("com.google.android.youtube")
    
    def open_camera(self):
        """Camera खोलता है"""
        return self.open_app("com.android.camera")
    
    def open_browser(self, url="https://www.google.com"):
        """Browser में URL खोलता है"""
        if not ANDROID_READY:
            return "Error: Android पर नहीं चल रहा"
        
        try:
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
            self.activity.startActivity(intent)
            return f"✅ Browser खुला: {url}"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def set_brightness(self, level):
        """
        Screen brightness बदलता है (0-255)
        """
        if not ANDROID_READY:
            return "Error: Android पर नहीं चल रहा"
        
        try:
            # Check if auto brightness is on
            auto = Settings.System.getInt(
                self.context.getContentResolver(),
                Settings.System.SCREEN_BRIGHTNESS_MODE
            )
            
            if auto == 1:
                # Auto brightness off करो
                Settings.System.putInt(
                    self.context.getContentResolver(),
                    Settings.System.SCREEN_BRIGHTNESS_MODE,
                    Settings.System.SCREEN_BRIGHTNESS_MODE_MANUAL
                )
            
            # Brightness set करो
            Settings.System.putInt(
                self.context.getContentResolver(),
                Settings.System.SCREEN_BRIGHTNESS,
                int(level)
            )
            return f"✅ Brightness set to {level}"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def vibrate(self, duration_ms=500):
        """Phone को vibrate करता है"""
        if not ANDROID_READY:
            return "Error: Android पर नहीं चल रहा"
        
        try:
            vibrator = self.context.getSystemService(Context.VIBRATOR_SERVICE)
            vibrator.vibrate(duration_ms)
            return f"✅ Vibrate for {duration_ms}ms"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def get_battery_level(self):
        """Battery level बताता है"""
        if not ANDROID_READY:
            return "Error: Android पर नहीं चल रहा"
        
        try:
            battery = autoclass('android.os.BatteryManager')
            level = battery.getIntProperty(battery.BATTERY_PROPERTY_CAPACITY)
            return f"🔋 Battery: {level}%"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def process_command(self, command):
        """
        Natural language command को समझता है और execute करता है
        """
        cmd = command.lower()
        
        # App opening commands
        if "whatsapp" in cmd and ("open" in cmd or "खोल" in cmd):
            return self.open_whatsapp()
        
        elif "youtube" in cmd and ("open" in cmd or "खोल" in cmd):
            return self.open_youtube()
        
        elif "camera" in cmd and ("open" in cmd or "खोल" in cmd):
            return self.open_camera()
        
        # Brightness commands
        elif "brightness" in cmd or "brightness" in cmd:
            if "high" in cmd or "तेज़" in cmd or "बढ़ा" in cmd:
                return self.set_brightness(255)
            elif "low" in cmd or "कम" in cmd or "घटा" in cmd:
                return self.set_brightness(50)
            elif "medium" in cmd or "बीच" in cmd:
                return self.set_brightness(128)
        
        # Battery check
        elif "battery" in cmd or "बैटरी" in cmd:
            return self.get_battery_level()
        
        # Vibrate
        elif "vibrate" in cmd or "वाइब्रेट" in cmd:
            return self.vibrate()
        
        # Web search (next file में add करेंगे)
        elif "search" in cmd or "खोज" in cmd or "ढूंढ" in cmd:
            return "🔍 Web search feature जल्द आ रहा है..."
        
        else:
            return f"❓ Command समझ नहीं आई: {command}"


# Test करने के लिए
if __name__ == "__main__":
    controller = PhoneController()
    
    print("=== Matus AI Phone Controller Test ===")
    print("Testing commands...")
    
    # Test battery
    print(controller.get_battery_level())
    
    # Test command processing
    print(controller.process_command("whatsapp खोलो"))
    print(controller.process_command("battery check करो"))
