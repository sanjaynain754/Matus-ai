#!/usr/bin/env python3
"""
MATUS HINDI EXPLAINER MODULE
Provides detailed Hindi explanations for all operations
"""

import json
from datetime import datetime

class HindiExplainer:
    def __init__(self):
        self.explanations = self._load_explanations()

    def _load_explanations(self):
        """Load Hindi explanations database"""
        return {
            "ssh_brute_force": {
                "title": "SSH ब्रूट फोर्स अटैक",
                "description": "यह एक SSH सर्वर पर कई बार लॉगिन करने की कोशिश करता है",
                "steps": [
                    "1. पहले target server से connection बनाया जाता है",
                    "2. फिर हर username और password combination को try किया जाता है",
                    "3. अगर कोई combination काम करता है, तो credentials मिल जाते हैं",
                    "4. सभी attempts को log किया जाता है"
                ],
                "what_happened": "यह tool SSH सर्वर पर brute force attack करता है और सही username-password combination खोजता है",
                "security_note": "यह केवल authorized systems पर ही use करें"
            },
            "ftp_brute_force": {
                "title": "FTP ब्रूट फोर्स अटैक",
                "description": "FTP सर्वर पर कई बार लॉगिन करने की कोशिश",
                "steps": [
                    "1. FTP server से connection establish किया जाता है",
                    "2. हर username-password को try किया जाता है",
                    "3. सफल login के बाद credentials record होते हैं",
                    "4. Multi-threading से तेजी से attack होता है"
                ],
                "what_happened": "FTP सर्वर पर brute force attack चलाया गया और valid credentials खोजे गए",
                "security_note": "केवल अपने authorized systems पर use करें"
            },
            "http_brute_force": {
                "title": "HTTP ब्रूट फोर्स अटैक",
                "description": "Web application पर HTTP authentication को break करना",
                "steps": [
                    "1. Target URL को identify किया जाता है",
                    "2. हर username-password combination को HTTP request के साथ भेजा जाता है",
                    "3. Response status को check किया जाता है (200 = success)",
                    "4. Valid credentials को record किया जाता है"
                ],
                "what_happened": "Web application पर HTTP basic auth को brute force किया गया",
                "security_note": "केवल अपने servers पर testing करें"
            },
            "port_scan": {
                "title": "पोर्ट स्कैनिंग",
                "description": "किसी server के खुले ports को खोजना",
                "steps": [
                    "1. Target IP address को identify किया जाता है",
                    "2. हर port पर connection attempt किया जाता है",
                    "3. अगर port open है तो response मिलता है",
                    "4. Open ports और services को list किया जाता है"
                ],
                "what_happened": "Target server पर port scanning की गई और सभी open ports मिल गए",
                "security_note": "Authorized networks पर ही scan करें"
            },
            "vulnerability_scan": {
                "title": "वल्नरेबिलिटी स्कैनिंग",
                "description": "System में security issues खोजना",
                "steps": [
                    "1. Target system को analyze किया जाता है",
                    "2. Known vulnerabilities से comparison किया जाता है",
                    "3. Weak configurations को identify किया जाता है",
                    "4. Detailed report generate होती है"
                ],
                "what_happened": "System में vulnerabilities scan किए गए और risk assessment की गई",
                "security_note": "केवल अपने systems के लिए"
            },
            "payload_generation": {
                "title": "पेलोड जेनरेशन",
                "description": "Exploitation के लिए custom payload बनाना",
                "steps": [
                    "1. Payload type को select किया जाता है",
                    "2. Attacker की IP और port को configure किया जाता है",
                    "3. Payload को encode किया जाता है (base64, URL, आदि)",
                    "4. Ready-to-use payload generate होता है"
                ],
                "what_happened": "Custom exploitation payload generate किया गया जो target को compromise कर सकता है",
                "security_note": "केवल authorized testing में use करें"
            },
            "sql_injection": {
                "title": "SQL इंजेक्शन टेस्टिंग",
                "description": "Database queries को manipulate करने की कोशिश",
                "steps": [
                    "1. Vulnerable input field को identify किया जाता है",
                    "2. SQL injection payloads को try किया जाता है",
                    "3. Database से unauthorized data निकाला जा सकता है",
                    "4. Vulnerability की severity determine की जाती है"
                ],
                "what_happened": "Application में SQL injection vulnerability test किया गया",
                "security_note": "केवल authorized applications पर test करें"
            },
            "xss_detection": {
                "title": "XSS डिटेक्शन",
                "description": "Cross-Site Scripting vulnerabilities खोजना",
                "steps": [
                    "1. Input fields को identify किया जाता है",
                    "2. JavaScript payloads को inject किया जाता है",
                    "3. अगर script execute होता है तो XSS vulnerable है",
                    "4. Vulnerability को report किया जाता है"
                ],
                "what_happened": "Application में XSS vulnerabilities के लिए test किया गया",
                "security_note": "केवल अपने applications पर test करें"
            },
            "system_enumeration": {
                "title": "सिस्टम एन्यूमरेशन",
                "description": "Target system की detailed information निकालना",
                "steps": [
                    "1. OS type और version को identify किया जाता है",
                    "2. Running services को list किया जाता है",
                    "3. User accounts को enumerate किया जाता है",
                    "4. Network configuration को analyze किया जाता है"
                ],
                "what_happened": "Target system की comprehensive information gather की गई",
                "security_note": "केवल authorized systems के लिए"
            },
            "privilege_escalation": {
                "title": "प्राइविलेज एस्केलेशन",
                "description": "Limited user से admin/root बनने की कोशिश",
                "steps": [
                    "1. Current user permissions को check किया जाता है",
                    "2. Known privilege escalation vectors को test किया जाता है",
                    "3. Misconfigured SUID binaries को identify किया जाता है",
                    "4. Possible escalation paths को suggest किया जाता है"
                ],
                "what_happened": "System में privilege escalation opportunities identify किए गए",
                "security_note": "केवल authorized testing में"
            },
            "reverse_shell": {
                "title": "रिवर्स शेल जेनरेशन",
                "description": "Target system से attacker को command execution shell देना",
                "steps": [
                    "1. Attacker की IP और port को configure किया जाता है",
                    "2. Different shell types के लिए payload generate होते हैं",
                    "3. Payload को target पर execute किया जाता है",
                    "4. Attacker को interactive shell मिल जाता है"
                ],
                "what_happened": "Reverse shell payload generate किया गया जो target system को compromise कर सकता है",
                "security_note": "केवल authorized targets पर use करें"
            },
            "web_scraping": {
                "title": "वेब स्क्रेपिंग",
                "description": "Website से data को extract करना",
                "steps": [
                    "1. Target URL को fetch किया जाता है",
                    "2. HTML content को parse किया जाता है",
                    "3. Useful information को extract किया जाता है",
                    "4. Data को structured format में organize किया जाता है"
                ],
                "what_happened": "Website से data successfully extract किया गया",
                "security_note": "Website के ToS को respect करें"
            },
            "dns_enumeration": {
                "title": "DNS एन्यूमरेशन",
                "description": "Domain के सभी subdomains को खोजना",
                "steps": [
                    "1. Target domain को identify किया जाता है",
                    "2. DNS queries को perform किया जाता है",
                    "3. सभी known subdomains को list किया जाता है",
                    "4. IP addresses को resolve किया जाता है"
                ],
                "what_happened": "Domain के सभी subdomains और DNS records enumerate किए गए",
                "security_note": "केवल authorized domains के लिए"
            }
        }

    def explain_operation(self, operation_type, result, additional_info=None):
        """Generate Hindi explanation for an operation"""
        if operation_type not in self.explanations:
            return self._generic_explanation(operation_type, result)

        exp = self.explanations[operation_type]
        
        explanation = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation_type,
            "title": exp["title"],
            "description": exp["description"],
            "detailed_explanation": self._generate_detailed_explanation(exp, result, additional_info),
            "steps_performed": exp["steps"],
            "what_happened": exp["what_happened"],
            "results_summary": self._summarize_results(result),
            "security_note": exp["security_note"],
            "recommendations": self._generate_recommendations(operation_type, result)
        }
        
        return explanation

    def _generate_detailed_explanation(self, exp, result, additional_info):
        """Generate detailed Hindi explanation"""
        explanation = f"""
🔍 **विस्तृत व्याख्या:**

**क्या किया गया:**
{exp['description']}

**कैसे काम किया:**
यह operation निम्नलिखित तरीके से काम करता है:

"""
        for step in exp['steps']:
            explanation += f"• {step}\n"
        
        if additional_info:
            explanation += f"\n**अतिरिक्त जानकारी:**\n{additional_info}\n"
        
        explanation += f"\n**परिणाम:**\n{exp['what_happened']}\n"
        
        return explanation

    def _summarize_results(self, result):
        """Summarize results in Hindi"""
        if isinstance(result, dict):
            summary = "**परिणाम सारांश:**\n"
            for key, value in result.items():
                if isinstance(value, list):
                    summary += f"• {key}: {len(value)} items मिले\n"
                elif isinstance(value, (int, float)):
                    summary += f"• {key}: {value}\n"
                else:
                    summary += f"• {key}: {str(value)[:100]}\n"
            return summary
        else:
            return f"**परिणाम:** {str(result)}"

    def _generate_recommendations(self, operation_type, result):
        """Generate security recommendations in Hindi"""
        recommendations = {
            "ssh_brute_force": [
                "✅ Strong passwords use करें (कम से कम 16 characters)",
                "✅ SSH key-based authentication enable करें",
                "✅ Default ports को change करें",
                "✅ Firewall से SSH access को restrict करें",
                "✅ Failed login attempts को monitor करें"
            ],
            "ftp_brute_force": [
                "✅ FTP को disable करें, SFTP use करें",
                "✅ Strong credentials set करें",
                "✅ IP-based access control implement करें",
                "✅ FTP access को log करें"
            ],
            "http_brute_force": [
                "✅ Rate limiting implement करें",
                "✅ Account lockout policy set करें",
                "✅ Multi-factor authentication enable करें",
                "✅ HTTPS use करें",
                "✅ Failed attempts को log करें"
            ],
            "port_scan": [
                "✅ Unnecessary ports को close करें",
                "✅ Firewall rules को configure करें",
                "✅ IDS/IPS system install करें",
                "✅ Regular port audits करें"
            ],
            "vulnerability_scan": [
                "✅ सभी software को updated रखें",
                "✅ Security patches को regularly apply करें",
                "✅ Weak configurations को fix करें",
                "✅ Regular security audits करें"
            ]
        }
        
        return recommendations.get(operation_type, [
            "✅ Security best practices follow करें",
            "✅ Regular security audits करें",
            "✅ Updates को timely apply करें"
        ])

    def _generic_explanation(self, operation_type, result):
        """Generate generic explanation for unknown operations"""
        return {
            "timestamp": datetime.now().isoformat(),
            "operation": operation_type,
            "title": f"{operation_type} Operation",
            "detailed_explanation": f"यह operation '{operation_type}' को execute किया गया",
            "results_summary": self._summarize_results(result),
            "security_note": "हमेशा authorized systems पर ही testing करें"
        }

    def get_hindi_summary(self, operation_type, result):
        """Get a quick Hindi summary"""
        explanation = self.explain_operation(operation_type, result)
        
        summary = f"""
╔════════════════════════════════════════════════════════╗
║                    {explanation['title']}
╚════════════════════════════════════════════════════════╝

📋 **ऑपरेशन विवरण:**
{explanation['description']}

🔧 **क्या किया गया:**
{explanation['what_happened']}

📊 **परिणाम:**
{explanation['results_summary']}

💡 **सिफारिशें:**
"""
        for rec in explanation['recommendations']:
            summary += f"{rec}\n"
        
        summary += f"\n⚠️ **सुरक्षा नोट:**\n{explanation['security_note']}\n"
        
        return summary

# Export functions
def explain_ssh_brute(result):
    explainer = HindiExplainer()
    return explainer.get_hindi_summary("ssh_brute_force", result)

def explain_ftp_brute(result):
    explainer = HindiExplainer()
    return explainer.get_hindi_summary("ftp_brute_force", result)

def explain_http_brute(result):
    explainer = HindiExplainer()
    return explainer.get_hindi_summary("http_brute_force", result)

def explain_port_scan(result):
    explainer = HindiExplainer()
    return explainer.get_hindi_summary("port_scan", result)

def explain_vuln_scan(result):
    explainer = HindiExplainer()
    return explainer.get_hindi_summary("vulnerability_scan", result)

def explain_payload(result):
    explainer = HindiExplainer()
    return explainer.get_hindi_summary("payload_generation", result)

def explain_any(operation_type, result):
    explainer = HindiExplainer()
    return explainer.get_hindi_summary(operation_type, result)
