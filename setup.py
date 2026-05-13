#!/usr/bin/env python3
"""
MATUS AI - Setup script for PyPI package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="matus-ai",
    version="1.0.0",
    author="sanjaynain754",
    author_email="sanjaynain754@example.com",
    description="MATUS ULTIMATE - The most powerful penetration testing and bug bounty framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sanjaynain754/Matus-ai",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "beautifulsoup4>=4.11.0",
        "paramiko>=3.0.0",
        "pycryptodome>=3.15.0",
        "scapy>=2.4.5",
        "netaddr>=0.8.0",
        "dnspython>=2.2.0",
    ],
    entry_points={
        "console_scripts": [
            "matus=matus_ultimate:main",
        ],
    },
    keywords=[
        "penetration-testing",
        "bug-bounty",
        "hacking",
        "security",
        "azure",
        "hackerone",
        "metasploit",
        "hydra",
        "network-scanning",
        "vulnerability-assessment",
        "exploitation",
        "reconnaissance",
        "cybersecurity",
        "ethical-hacking",
    ],
    project_urls={
        "Bug Reports": "https://github.com/sanjaynain754/Matus-ai/issues",
        "Source": "https://github.com/sanjaynain754/Matus-ai",
        "Documentation": "https://github.com/sanjaynain754/Matus-ai/blob/main/README.md",
    },
)
