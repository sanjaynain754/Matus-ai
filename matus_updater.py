import subprocess
import os

class MatusUpdater:
    @staticmethod
    def self_update():
        print("Checking for Matus updates...")
        try:
            # Check if it's a git repository
            if not os.path.exists('.git'):
                return "Error: Not a git repository. Cannot self-update."
            
            # Pull latest changes from GitHub
            result = subprocess.check_output(['git', 'pull', 'origin', 'main']).decode()
            if "Already up to date" in result:
                return "Matus is already up to date."
            else:
                return f"Matus has been updated successfully!\n{result}"
        except Exception as e:
            return f"Error during self-update: {e}"

    @staticmethod
    def self_upgrade():
        print("Upgrading Matus dependencies and environment...")
        try:
            # Upgrade pip and required packages
            subprocess.check_call([os.sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([os.sys.executable, "-m", "pip", "install", "--upgrade", "openai", "kivy"])
            return "Matus environment upgraded successfully."
        except Exception as e:
            return f"Error during self-upgrade: {e}"

def inject_updater_tools(interpreter):
    updater = MatusUpdater()
    interpreter.variables['self_update'] = updater.self_update
    interpreter.variables['self_upgrade'] = updater.self_upgrade
