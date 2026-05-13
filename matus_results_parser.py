#!/usr/bin/env python3
"""
MATUS RESULTS PARSER
Parse, organize, and analyze security testing results
"""

import json
from datetime import datetime
from collections import defaultdict

class ResultsParser:
    """Parse and organize security testing results"""
    
    def __init__(self):
        self.findings = []
        self.statistics = defaultdict(int)
        self.severity_distribution = defaultdict(int)
    
    def add_finding(self, title, vulnerability_type, severity, description, proof=None):
        """Add a finding"""
        finding = {
            'id': len(self.findings) + 1,
            'title': title,
            'type': vulnerability_type,
            'severity': severity,
            'description': description,
            'proof': proof,
            'timestamp': datetime.now().isoformat()
        }
        
        self.findings.append(finding)
        self.statistics['total_findings'] += 1
        self.severity_distribution[severity] += 1
        
        return finding
    
    def get_findings_by_severity(self, severity):
        """Get findings by severity level"""
        return [f for f in self.findings if f['severity'] == severity]
    
    def get_findings_by_type(self, vuln_type):
        """Get findings by vulnerability type"""
        return [f for f in self.findings if f['type'] == vuln_type]
    
    def generate_summary(self):
        """Generate findings summary"""
        summary = {
            'total_findings': len(self.findings),
            'severity_distribution': dict(self.severity_distribution),
            'critical': len(self.get_findings_by_severity('Critical')),
            'high': len(self.get_findings_by_severity('High')),
            'medium': len(self.get_findings_by_severity('Medium')),
            'low': len(self.get_findings_by_severity('Low')),
            'info': len(self.get_findings_by_severity('Info')),
        }
        return summary
    
    def generate_markdown_report(self):
        """Generate markdown report"""
        report = "# Security Testing Report\n\n"
        report += f"**Generated:** {datetime.now().isoformat()}\n\n"
        
        # Summary
        summary = self.generate_summary()
        report += "## Summary\n\n"
        report += f"- **Total Findings:** {summary['total_findings']}\n"
        report += f"- **Critical:** {summary['critical']}\n"
        report += f"- **High:** {summary['high']}\n"
        report += f"- **Medium:** {summary['medium']}\n"
        report += f"- **Low:** {summary['low']}\n"
        report += f"- **Info:** {summary['info']}\n\n"
        
        # Findings by severity
        for severity in ['Critical', 'High', 'Medium', 'Low', 'Info']:
            findings = self.get_findings_by_severity(severity)
            if findings:
                report += f"## {severity} Severity Findings\n\n"
                for finding in findings:
                    report += f"### {finding['title']}\n\n"
                    report += f"**Type:** {finding['type']}\n\n"
                    report += f"**Description:** {finding['description']}\n\n"
                    if finding['proof']:
                        report += f"**Proof:** {finding['proof']}\n\n"
                    report += "---\n\n"
        
        return report
    
    def generate_json_report(self):
        """Generate JSON report"""
        return {
            'timestamp': datetime.now().isoformat(),
            'summary': self.generate_summary(),
            'findings': self.findings
        }
    
    def generate_csv_report(self):
        """Generate CSV report"""
        csv = "ID,Title,Type,Severity,Description,Timestamp\n"
        for finding in self.findings:
            csv += f"{finding['id']},\"{finding['title']}\",{finding['type']},{finding['severity']},\"{finding['description']}\",{finding['timestamp']}\n"
        return csv
    
    def export_to_file(self, filename, format='json'):
        """Export report to file"""
        if format == 'json':
            content = json.dumps(self.generate_json_report(), indent=2)
            ext = '.json'
        elif format == 'markdown':
            content = self.generate_markdown_report()
            ext = '.md'
        elif format == 'csv':
            content = self.generate_csv_report()
            ext = '.csv'
        else:
            raise ValueError(f"Unknown format: {format}")
        
        filepath = f"{filename}{ext}"
        with open(filepath, 'w') as f:
            f.write(content)
        
        return filepath

class FindingOrganizer:
    """Organize findings for HackerOne submission"""
    
    def __init__(self):
        self.parser = ResultsParser()
    
    def organize_for_submission(self):
        """Organize findings for HackerOne"""
        findings = self.parser.findings
        
        # Group by severity and type
        organized = {
            'critical': [],
            'high': [],
            'medium': [],
            'low': [],
            'info': []
        }
        
        for finding in findings:
            severity = finding['severity'].lower()
            organized[severity].append(finding)
        
        # Sort by severity
        submission_order = []
        for severity in ['critical', 'high', 'medium', 'low', 'info']:
            submission_order.extend(organized[severity])
        
        return submission_order
    
    def generate_submission_checklist(self):
        """Generate submission checklist"""
        checklist = """
# HackerOne Submission Checklist

## Before Submission
- [ ] All findings verified
- [ ] Proof of concept tested
- [ ] Screenshots captured
- [ ] Remediation suggestions provided
- [ ] References included
- [ ] Report reviewed for clarity

## For Each Finding
- [ ] Clear title
- [ ] Detailed description
- [ ] Impact assessment
- [ ] Step-by-step reproduction
- [ ] Proof of concept
- [ ] Screenshots/videos
- [ ] Remediation advice

## Submission
- [ ] Select correct program
- [ ] Choose appropriate team
- [ ] Set correct severity
- [ ] Add all attachments
- [ ] Review before submitting
- [ ] Submit report

## After Submission
- [ ] Monitor for responses
- [ ] Provide additional info if requested
- [ ] Collaborate with security team
- [ ] Wait for resolution
- [ ] Receive reward
"""
        return checklist

def parse_results(findings_list):
    """Parse results from list"""
    parser = ResultsParser()
    for finding in findings_list:
        parser.add_finding(
            finding['title'],
            finding['type'],
            finding['severity'],
            finding['description'],
            finding.get('proof')
        )
    return parser

if __name__ == "__main__":
    # Example usage
    parser = ResultsParser()
    
    # Add sample findings
    parser.add_finding(
        "SQL Injection in Search",
        "SQL Injection",
        "Critical",
        "User input not sanitized in search parameter"
    )
    
    parser.add_finding(
        "Stored XSS in Comments",
        "Cross-Site Scripting",
        "High",
        "Comments field allows script injection"
    )
    
    # Generate reports
    print(parser.generate_markdown_report())
    print("\n\n--- Summary ---\n")
    print(json.dumps(parser.generate_summary(), indent=2))
