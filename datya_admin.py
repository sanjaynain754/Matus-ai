"""
AdminAgent - System Administration Tools
Controlled by Datya | Admin: Sanjay
"""

import os
import sys
import platform
import subprocess
import shutil


class AdminAgent:
    """System admin tools for device management"""

    def admin_sys_info(self):
        """Get complete system information"""
        info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Release": platform.release(),
            "Architecture": platform.machine(),
            "Processor": platform.processor(),
            "Python": sys.version.split()[0],
            "Home": os.path.expanduser("~"),
            "CWD": os.getcwd(),
            "User": os.environ.get("USER", "unknown"),
            "Hostname": platform.node(),
        }
        result = "╔═══════════════════════════════════════╗\n"
        result += "║  SYSTEM INFORMATION                   ║\n"
        result += "╠═══════════════════════════════════════╣\n"
        for key, val in info.items():
            result += f"║  {key:15s} {str(val)[:22]:22s}║\n"
        result += "╚═══════════════════════════════════════╝"
        return result

    def admin_list_procs(self):
        """List running processes"""
        try:
            if platform.system() == "Windows":
                output = subprocess.check_output(["tasklist"], timeout=5).decode('utf-8', errors='replace')
            else:
                output = subprocess.check_output(["ps", "aux"], timeout=5).decode('utf-8', errors='replace')
            return output[:2000]
        except Exception as e:
            return f"Error listing processes: {str(e)}"

    def admin_kill_proc(self, pid):
        """Kill a process by PID"""
        try:
            pid = str(pid)
            if platform.system() == "Windows":
                subprocess.check_call(["taskkill", "/F", "/PID", pid], timeout=5)
            else:
                subprocess.check_call(["kill", "-9", pid], timeout=5)
            return f"Process {pid} killed successfully."
        except Exception as e:
            return f"Error killing process {pid}: {str(e)}"

    def admin_is_root(self):
        """Check if running with root/admin privileges"""
        try:
            if platform.system() == "Windows":
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.getuid() == 0
        except:
            return False

    def admin_disk_usage(self, path="/"):
        """Check disk usage"""
        try:
            usage = shutil.disk_usage(str(path))
            total_gb = usage.total / (1024**3)
            used_gb = usage.used / (1024**3)
            free_gb = usage.free / (1024**3)
            pct = (usage.used / usage.total) * 100

            return (f"Disk Usage ({path}):\n"
                    f"  Total: {total_gb:.2f} GB\n"
                    f"  Used:  {used_gb:.2f} GB\n"
                    f"  Free:  {free_gb:.2f} GB\n"
                    f"  Usage: {pct:.1f}%")
        except Exception as e:
            return f"Disk error: {str(e)}"

    def admin_battery(self):
        """Check battery status (Android)"""
        try:
            # Try Android battery manager
            if os.environ.get('ANDROID_ARGUMENT'):
                from jnius import autoclass
                BatteryManager = autoclass('android.os.BatteryManager')
                activity = autoclass('org.kivy.android.PythonActivity').mActivity
                bm = activity.getSystemService(activity.BATTERY_SERVICE)
                level = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
                charging = bm.isCharging()
                return f"Battery: {level}% {'(Charging)' if charging else '(Not charging)'}"
            else:
                return "Battery info not available on this platform."
        except Exception as e:
            return f"Battery check error: {str(e)}"

    def admin_set_brightness(self, level):
        """Set screen brightness (Android)"""
        try:
            if os.environ.get('ANDROID_ARGUMENT'):
                from jnius import autoclass
                Settings = autoclass('android.provider.Settings$System')
                activity = autoclass('org.kivy.android.PythonActivity').mActivity
                level = int(float(level))
                level = max(0, min(255, level))
                Settings.System.putInt(activity.getContentResolver(),
                                      Settings.System.SCREEN_BRIGHTNESS, level)
                return f"Brightness set to {level}/255"
            else:
                return "Brightness control only available on Android."
        except Exception as e:
            return f"Brightness error: {str(e)}"

    def admin_vibrate(self, duration="500"):
        """Vibrate device (Android)"""
        try:
            if os.environ.get('ANDROID_ARGUMENT'):
                from jnius import autoclass
                activity = autoclass('org.kivy.android.PythonActivity').mActivity
                vibrator = activity.getSystemService(activity.VIBRATOR_SERVICE)
                duration = int(duration)
                vibrator.vibrate(duration)
                return f"Vibrating for {duration}ms"
            else:
                return "Vibrate only available on Android."
        except Exception as e:
            return f"Vibrate error: {str(e)}"

    def get_tools(self):
        """Return all tools as a dict"""
        return {
            'admin_sys_info': self.admin_sys_info,
            'admin_list_procs': self.admin_list_procs,
            'admin_kill_proc': self.admin_kill_proc,
            'admin_is_root': self.admin_is_root,
            'admin_disk_usage': self.admin_disk_usage,
            'admin_battery': self.admin_battery,
            'admin_set_brightness': self.admin_set_brightness,
            'admin_vibrate': self.admin_vibrate,
        }
