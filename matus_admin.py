import os
import sys
import platform
import subprocess
import shutil

class MatusAdmin:
    @staticmethod
    def get_system_info():
        info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Architecture": platform.machine(),
            "Processor": platform.processor(),
            "Python Version": sys.version.split()[0],
            "Home Directory": os.path.expanduser("~"),
            "Current Directory": os.getcwd()
        }
        return info

    @staticmethod
    def list_processes():
        try:
            if platform.system() == "Windows":
                output = subprocess.check_output(["tasklist"]).decode()
            else:
                output = subprocess.check_output(["ps", "aux"]).decode()
            return output
        except Exception as e:
            return f"Error listing processes: {e}"

    @staticmethod
    def kill_process(pid):
        try:
            if platform.system() == "Windows":
                subprocess.check_call(["taskkill", "/F", "/PID", str(pid)])
            else:
                subprocess.check_call(["kill", "-9", str(pid)])
            return f"Process {pid} killed successfully."
        except Exception as e:
            return f"Error killing process {pid}: {e}"

    @staticmethod
    def check_privileges():
        try:
            if platform.system() == "Windows":
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.getuid() == 0
        except:
            return False

    @staticmethod
    def disk_usage(path="/"):
        try:
            usage = shutil.disk_usage(path)
            return {
                "Total": f"{usage.total / (1024**3):.2f} GB",
                "Used": f"{usage.used / (1024**3):.2f} GB",
                "Free": f"{usage.free / (1024**3):.2f} GB"
            }
        except Exception as e:
            return f"Error checking disk usage: {e}"

def inject_admin_tools(interpreter):
    admin = MatusAdmin()
    interpreter.variables['admin_sys_info'] = admin.get_system_info
    interpreter.variables['admin_list_procs'] = admin.list_processes
    interpreter.variables['admin_kill_proc'] = admin.kill_process
    interpreter.variables['admin_is_root'] = admin.check_privileges
    interpreter.variables['admin_disk_usage'] = admin.disk_usage
