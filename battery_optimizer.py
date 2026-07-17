"""
Matus AI Battery Optimizer
Battery level monitor करता है और optimize करता है
"""

import os

ANDROID = 'ANDROID_ARGUMENT' in os.environ

if ANDROID:
    try:
        from jnius import autoclass
        BatteryManager = autoclass('android.os.BatteryManager')
        Context = autoclass('android.content.Context')
        BATTERY_READY = True
    except Exception as e:
        print(f"Battery manager error: {e}")
        BATTERY_READY = False
else:
    BATTERY_READY = False


class BatteryOptimizer:
    """Battery को monitor और optimize करने वाला class"""
    
    def __init__(self):
        self.context = None
        if BATTERY_READY:
            try:
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                self.context = PythonActivity.mActivity.getApplicationContext()
            except Exception as e:
                print(f"Context init error: {e}")
    
    def get_battery_level(self):
        """Current battery level return करता है"""
        if not BATTERY_READY:
            return -1
        
        try:
            battery = BatteryManager()
            level = battery.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
            return level
        except Exception as e:
            print(f"Battery level error: {e}")
            return -1
    
    def is_charging(self):
        """Check करता है कि phone charging पर है या नहीं"""
        if not BATTERY_READY:
            return False
        
        try:
            battery = BatteryManager()
            status = battery.getIntProperty(BatteryManager.BATTERY_PROPERTY_STATUS)
            return status == BatteryManager.BATTERY_STATUS_CHARGING
        except Exception as e:
            return False
    
    def get_battery_status(self):
        """Complete battery status return करता है"""
        level = self.get_battery_level()
        charging = self.is_charging()
        
        if level == -1:
            return "❌ Battery information not available"
        
        status = f"🔋 Battery: {level}%"
        
        if charging:
            status += " ⚡ (Charging)"
        elif level < 20:
            status += " ⚠️ (Low - consider charging)"
        elif level < 50:
            status += " 🔶 (Medium)"
        else:
            status += " ✅ (Good)"
        
        return status
    
    def optimize_for_battery_saving(self):
        """
        Battery saving mode activate करता है
        Returns: suggestions और actions taken
        """
        level = self.get_battery_level()
        suggestions = []
        
        if level != -1 and level < 30:
            suggestions.append("⚠️ Battery low! Consider these actions:")
            suggestions.append("   • Reduce screen brightness")
            suggestions.append("   • Close background apps")
            suggestions.append("   • Disable GPS if not needed")
            suggestions.append("   • Turn off WiFi/Bluetooth if not using")
        
        return "\n".join(suggestions) if suggestions else "✅ Battery level is good"


# Test
if __name__ == "__main__":
    optimizer = BatteryOptimizer()
    
    print("=== Battery Optimizer Test ===")
    print(optimizer.get_battery_status())
    print("\nOptimization suggestions:")
    print(optimizer.optimize_for_battery_saving())
