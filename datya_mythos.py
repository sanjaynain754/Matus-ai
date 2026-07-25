"""
MythosAgent - Security Analysis & Vulnerability Assessment
Controlled by Datya | Optional OpenAI integration
"""

import os

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


class MythosAgent:
    """Security analysis agent for vulnerability assessment"""

    def __init__(self):
        self.client = None
        if HAS_OPENAI:
            api_key = os.environ.get("OPENAI_API_KEY")
            if api_key:
                try:
                    self.client = OpenAI(api_key=api_key)
                except Exception:
                    pass

    def mythos_scan_code(self, code_snippet):
        """Analyze code for security vulnerabilities"""
        if self.client is None:
            return self._basic_security_check(code_snippet)

        prompt = f"Analyze this code for security vulnerabilities:\n\n```{code_snippet}``\n\nIdentify all potential issues and provide fixes."

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a security expert analyzing code for vulnerabilities."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Analysis error: {str(e)}"

    def mythos_basic_check(self, url):
        """Basic security checks on a URL"""
        checks = []

        # Check protocol
        if str(url).startswith("https://"):
            checks.append("✓ HTTPS enabled")
        elif str(url).startswith("http://"):
            checks.append("✗ HTTP only (not secure)")
        else:
            checks.append("? Protocol unknown")

        # Check for common issues
        url_str = str(url).lower()
        if "password" in url_str or "token" in url_str:
            checks.append("⚠ URL may contain sensitive data")
        if "admin" in url_str:
            checks.append("⚠ Admin endpoint detected")

        return f"Security Check for {url}:\n" + '\n'.join(f"  {c}" for c in checks)

    def mythos_report(self, findings):
        """Generate a security report from findings"""
        if self.client is None:
            return f"Security Report:\n{findings}"

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Generate a professional security report with severity ratings and recommendations."},
                    {"role": "user", "content": f"Findings: {findings}"}
                ],
                max_tokens=1500,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Report error: {str(e)}"

    def _basic_security_check(self, code):
        """Basic rule-based security check without AI"""
        issues = []
        code_lower = str(code).lower()

        if "eval(" in code:
            issues.append("HIGH: eval() usage detected - code injection risk")
        if "exec(" in code:
            issues.append("HIGH: exec() usage detected - code execution risk")
        if "os.system(" in code:
            issues.append("MEDIUM: os.system() - command injection risk")
        if "subprocess" in code and "shell=True" in code:
            issues.append("MEDIUM: subprocess with shell=True - injection risk")
        if "sql" in code_lower and ("+" in code or "format(" in code or "f\"" in code):
            issues.append("HIGH: Possible SQL injection - use parameterized queries")
        if "<script>" in code_lower:
            issues.append("MEDIUM: Script tags detected - XSS risk")
        if "password" in code_lower and ("=" in code and "''" in code):
            issues.append("MEDIUM: Empty password detected")
        if "http://" in code:
            issues.append("LOW: HTTP used instead of HTTPS")

        if issues:
            return "Security Issues Found:\n" + '\n'.join(f"  {i}" for i in issues)
        return "No obvious security issues found."

    def get_tools(self):
        """Return all tools as a dict"""
        tools = {
            'mythos_scan_code': self.mythos_scan_code,
            'mythos_basic_check': self.mythos_basic_check,
            'mythos_report': self.mythos_report,
        }
        return tools
