# 🔍 AutoRecon-X
> Modular reconnaissance pipeline for authorized VAPT engagements (Lab-Only)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Lab%20Tool-orange)

A structured, scope-bound reconnaissance tool that orchestrates Nmap, Gobuster, Nuclei, and WhatWeb into a single pipeline with JSON report output. Designed for portfolio demonstration in isolated lab environments only.

> ⚠️ **ETHICAL USE ONLY**: This tool is intended for authorized security testing in isolated lab environments (e.g., OWASP Juice Shop, Metasploitable, TryHackMe). Never use against systems you do not own or have explicit written permission to test.

---

## 🚀 Quick Start (Lab Environment)

### Prerequisites
- Python 3.8+
- Tools installed in PATH: `nmap`, `gobuster`, `nuclei`, `whatweb`
- Target: Local lab VM (e.g., `192.168.56.101`)

### Installation
```bash
# Clone the repo
git clone https://github.com/wajudev/autorecon-x.git
cd autorecon-x

# Install dependencies (if any)
pip install -r requirements.txt  # Optional: create this file if adding Python libs


## Usage:

# Basic scan against lab target
python src/autorecon_x.py -t 192.168.56.101 -o reports/lab-scan.json

# With specific modules
python src/autorecon_x.py -t 192.168.56.101 --modules nmap,gobuster -v


## Example Output Structure:

{
  "scan_metadata": {
    "target": "192.168.56.101",
    "timestamp": "2026-04-29T20:00:00Z",
    "scope": "lab-only"
  },
  "findings": [
    {
      "tool": "nmap",
      "service": "http",
      "port": 80,
      "version": "Apache 2.4.49",
      "cve": ["CVE-2021-41773"],
      "risk": "HIGH"
    }
  ]
}


🧱 ## Prerequisites:

src/
├── autorecon_x.py      # Main orchestrator
├── modules/
│   ├── nmap_scan.py    # Nmap wrapper
│   ├── gobuster_scan.py # Directory brute-force
│   └── nuclei_scan.py  # Vulnerability templates
reports/                # JSON/Markdown outputs (gitignored by default)
docs/                   # Lab setup guides, methodology notes


## 📄 Sample Lab Report
See companion repo: vapt-webapp-report for a full engagement deliverable example.

## 🔐 Ethics & Compliance
All testing performed in isolated VirtualBox/VMware labs
Targets: OWASP Juice Shop, Metasploitable2, TryHackMe public rooms
No credentials, IPs, or real domains stored in code
Reports sanitized: 10.0.0.x, example.com, REDACTED

## 🤝 Contributing
Educational contributions welcome! Please:
Fork the repo
Create a feature branch
Add tests for new modules
Submit a PR with lab validation notes

## 📜 License
MIT License – See LICENSE for details.
