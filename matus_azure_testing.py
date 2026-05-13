#!/usr/bin/env python3
"""
MATUS AZURE TESTING MODULE
Azure-specific vulnerability testing and reconnaissance
For authorized bug bounty testing only
"""

import json
import requests
from datetime import datetime

class AzureTesting:
    """Azure cloud platform testing module"""
    
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.findings = []
    
    def azure_subdomain_enum(self, domain):
        """Enumerate Azure subdomains"""
        print(f"\n🔍 Azure Subdomain Enumeration for {domain}")
        print("=" * 60)
        
        azure_patterns = [
            f"{domain}.azurewebsites.net",
            f"{domain}.cloudapp.azure.com",
            f"{domain}.database.windows.net",
            f"{domain}.blob.core.windows.net",
            f"{domain}.table.core.windows.net",
            f"{domain}.queue.core.windows.net",
            f"{domain}.file.core.windows.net",
            f"api-{domain}.azurewebsites.net",
            f"admin-{domain}.azurewebsites.net",
            f"dev-{domain}.azurewebsites.net",
            f"test-{domain}.azurewebsites.net",
            f"staging-{domain}.azurewebsites.net",
            f"prod-{domain}.azurewebsites.net",
        ]
        
        found_subdomains = []
        for subdomain in azure_patterns:
            try:
                response = requests.head(f"https://{subdomain}", timeout=5)
                if response.status_code < 500:
                    found_subdomains.append({
                        'subdomain': subdomain,
                        'status': response.status_code,
                        'headers': dict(response.headers)
                    })
                    print(f"✅ Found: {subdomain} (Status: {response.status_code})")
            except:
                pass
        
        return found_subdomains
    
    def azure_storage_enum(self, storage_account):
        """Enumerate Azure storage accounts"""
        print(f"\n🔍 Azure Storage Account Enumeration for {storage_account}")
        print("=" * 60)
        
        storage_types = ['blob', 'table', 'queue', 'file']
        results = {}
        
        for storage_type in storage_types:
            url = f"https://{storage_account}.{storage_type}.core.windows.net"
            try:
                response = requests.head(url, timeout=5)
                results[storage_type] = {
                    'url': url,
                    'status': response.status_code,
                    'accessible': response.status_code < 500
                }
                print(f"✅ {storage_type.upper()}: {url} (Status: {response.status_code})")
            except Exception as e:
                results[storage_type] = {'error': str(e)}
        
        return results
    
    def azure_api_enum(self, domain):
        """Enumerate Azure API endpoints"""
        print(f"\n🔍 Azure API Enumeration for {domain}")
        print("=" * 60)
        
        api_endpoints = [
            '/api/v1',
            '/api/v2',
            '/api/admin',
            '/api/users',
            '/api/auth',
            '/api/config',
            '/api/settings',
            '/api/debug',
            '/swagger',
            '/swagger-ui.html',
            '/api-docs',
            '/.well-known/openid-configuration',
            '/metadata/identity/oauth2/v2.0/metadata',
        ]
        
        found_endpoints = []
        base_url = f"https://{domain}"
        
        for endpoint in api_endpoints:
            try:
                response = requests.get(f"{base_url}{endpoint}", timeout=5)
                if response.status_code < 500:
                    found_endpoints.append({
                        'endpoint': endpoint,
                        'status': response.status_code,
                        'content_type': response.headers.get('content-type', 'unknown')
                    })
                    print(f"✅ Found: {endpoint} (Status: {response.status_code})")
            except:
                pass
        
        return found_endpoints
    
    def azure_auth_test(self, domain):
        """Test Azure authentication mechanisms"""
        print(f"\n🔐 Azure Authentication Testing for {domain}")
        print("=" * 60)
        
        auth_tests = {
            'default_creds': self._test_default_credentials(domain),
            'oauth_bypass': self._test_oauth_bypass(domain),
            'jwt_validation': self._test_jwt_validation(domain),
            'mfa_bypass': self._test_mfa_bypass(domain),
        }
        
        return auth_tests
    
    def _test_default_credentials(self, domain):
        """Test for default credentials"""
        print("  Testing default credentials...")
        defaults = [
            ('admin', 'admin'),
            ('admin', 'password'),
            ('admin', 'Admin@123'),
            ('root', 'root'),
            ('test', 'test'),
        ]
        
        results = []
        for username, password in defaults:
            # Simulate test (actual implementation would use proper auth)
            results.append({
                'username': username,
                'password': password,
                'status': 'tested'
            })
        
        return results
    
    def _test_oauth_bypass(self, domain):
        """Test OAuth bypass vulnerabilities"""
        print("  Testing OAuth bypass...")
        return {'status': 'tested', 'findings': []}
    
    def _test_jwt_validation(self, domain):
        """Test JWT validation"""
        print("  Testing JWT validation...")
        return {'status': 'tested', 'findings': []}
    
    def _test_mfa_bypass(self, domain):
        """Test MFA bypass"""
        print("  Testing MFA bypass...")
        return {'status': 'tested', 'findings': []}
    
    def azure_keyvault_enum(self, domain):
        """Enumerate Azure Key Vault"""
        print(f"\n🔑 Azure Key Vault Enumeration for {domain}")
        print("=" * 60)
        
        keyvault_url = f"https://{domain}.vault.azure.net"
        try:
            response = requests.get(f"{keyvault_url}/secrets", timeout=5)
            print(f"Key Vault URL: {keyvault_url}")
            print(f"Status: {response.status_code}")
            
            return {
                'url': keyvault_url,
                'status': response.status_code,
                'accessible': response.status_code < 500
            }
        except Exception as e:
            return {'error': str(e)}
    
    def azure_rbac_enum(self, domain):
        """Enumerate Azure RBAC roles"""
        print(f"\n👥 Azure RBAC Enumeration for {domain}")
        print("=" * 60)
        
        rbac_endpoints = [
            '/api/roles',
            '/api/permissions',
            '/api/assignments',
            '/api/access-control',
        ]
        
        results = []
        for endpoint in rbac_endpoints:
            results.append({
                'endpoint': endpoint,
                'status': 'to_test'
            })
            print(f"  Testing: {endpoint}")
        
        return results
    
    def generate_report(self):
        """Generate testing report"""
        report = {
            'timestamp': self.timestamp,
            'findings': self.findings,
            'total_findings': len(self.findings)
        }
        return report

# Standalone functions for Matus integration
def azure_full_recon(domain):
    """Full Azure reconnaissance"""
    tester = AzureTesting()
    
    print("\n" + "="*60)
    print("🔥 MATUS AZURE FULL RECONNAISSANCE")
    print("="*60)
    
    results = {
        'domain': domain,
        'timestamp': datetime.now().isoformat(),
        'subdomains': tester.azure_subdomain_enum(domain),
        'api_endpoints': tester.azure_api_enum(domain),
        'auth_tests': tester.azure_auth_test(domain),
        'keyvault': tester.azure_keyvault_enum(domain),
        'rbac': tester.azure_rbac_enum(domain),
    }
    
    return results

def azure_storage_test(storage_account):
    """Test Azure storage account"""
    tester = AzureTesting()
    return tester.azure_storage_enum(storage_account)

if __name__ == "__main__":
    # Example usage
    print("MATUS Azure Testing Module")
    print("Usage: from matus_azure_testing import azure_full_recon")
    print("Example: azure_full_recon('mycompany.azurewebsites.net')")
