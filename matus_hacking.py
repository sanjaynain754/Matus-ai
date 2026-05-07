import socket
import subprocess
import os

class MatusHacking:
    @staticmethod
    def scan_ports(target, ports):
        print(f"Scanning {target}...")
        open_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open")
            sock.close()
        return open_ports

    @staticmethod
    def get_ip(domain):
        try:
            return socket.gethostbyname(domain)
        except socket.gaierror:
            return "Could not resolve domain"

    @staticmethod
    def run_command(command):
        try:
            result = subprocess.check_output(command, shell=True).decode()
            print(result)
            return result
        except Exception as e:
            print(str(e))
            return str(e)

def inject_hacking_tools(interpreter):
    interpreter.variables['scan_ports'] = MatusHacking.scan_ports
    interpreter.variables['get_ip'] = MatusHacking.get_ip
    interpreter.variables['run_cmd'] = MatusHacking.run_command
