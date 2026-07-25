"""
HackingAgent - Security & Network Tools
Controlled by Datya
"""

import socket
import subprocess
import os
import platform


class HackingAgent:
    """Network scanning and system command agent"""

    def scan_ports(self, target, ports="80,443,8080,22,21,3306,5432"):
        """Scan ports on a target host"""
        try:
            target = str(target)
            if isinstance(ports, str):
                port_list = [int(p.strip()) for p in ports.split(',') if p.strip().isdigit()]
            elif isinstance(ports, (list, tuple)):
                port_list = [int(p) for p in ports]
            else:
                port_list = [int(ports)]

            open_ports = []
            for port in port_list:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()

            result = f"Scan Results for {target}:\n"
            if open_ports:
                result += f"Open ports: {', '.join(str(p) for p in open_ports)}"
            else:
                result += "No open ports found."
            return result
        except Exception as e:
            return f"Scan error: {str(e)}"

    def get_ip(self, domain):
        """Get IP address for a domain"""
        try:
            return socket.gethostbyname(str(domain))
        except socket.gaierror:
            return f"Could not resolve domain: {domain}"
        except Exception as e:
            return f"Error: {str(e)}"

    def run_cmd(self, command):
        """Run a system command (safe - limited)"""
        try:
            result = subprocess.check_output(
                str(command), shell=True, timeout=10, stderr=subprocess.STDOUT
            ).decode('utf-8', errors='replace')
            return result[:2000]  # Limit output
        except subprocess.TimeoutExpired:
            return "Command timed out (10s limit)"
        except Exception as e:
            return f"Command error: {str(e)}"

    def read_file(self, path):
        """Read a file"""
        try:
            with open(str(path), 'r', errors='replace') as f:
                content = f.read()
            return content[:2000]
        except Exception as e:
            return f"Read error: {str(e)}"

    def write_file(self, path, content):
        """Write content to a file"""
        try:
            with open(str(path), 'w') as f:
                f.write(str(content))
            return f"Written to {path} successfully."
        except Exception as e:
            return f"Write error: {str(e)}"

    def ping_host(self, target, count="4"):
        """Ping a host"""
        try:
            count = int(count)
            cmd = f"ping -c {count} {target}" if platform.system() != "Windows" else f"ping -n {count} {target}"
            result = subprocess.check_output(
                cmd, shell=True, timeout=30, stderr=subprocess.STDOUT
            ).decode('utf-8', errors='replace')
            return result[:1000]
        except Exception as e:
            return f"Ping error: {str(e)}"

    def dns_lookup(self, domain, record_type="A"):
        """Basic DNS lookup using nslookup"""
        try:
            cmd = f"nslookup -type={record_type} {domain}"
            result = subprocess.check_output(
                cmd, shell=True, timeout=10, stderr=subprocess.STDOUT
            ).decode('utf-8', errors='replace')
            return result[:1000]
        except Exception as e:
            return f"DNS error: {str(e)}"

    def get_tools(self):
        """Return all tools as a dict"""
        return {
            'scan_ports': self.scan_ports,
            'get_ip': self.get_ip,
            'run_cmd': self.run_cmd,
            'read_file': self.read_file,
            'write_file': self.write_file,
            'ping_host': self.ping_host,
            'dns_lookup': self.dns_lookup,
        }
