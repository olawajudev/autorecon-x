```python
#!/usr/bin/env python3
"""
AutoRecon-X: Modular Reconnaissance Pipeline for Authorized VAPT (Lab-Only)
Author: Ibrahim Ayoola (@olawajudev)
License: MIT
⚠️ ETHICAL USE ONLY: Isolated lab environments only (OWASP Juice Shop, Metasploitable, TryHackMe)
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Lab-only target validation
ALLOWED_RANGES = ["10.0.0.", "192.168.56.", "127.0.0."]

def validate_target(target: str) -> bool:
    """Ensure target is in authorized lab IP ranges"""
    return any(target.startswith(prefix) for prefix in ALLOWED_RANGES)

def run_command(cmd: list) -> dict:
    """Safely execute a command and capture output"""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout[:2000],  # Truncate for report size
            "stderr": result.stderr[:500],
            "cmd": " ".join(cmd)
        }
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "Command timed out"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def nmap_scan(target: str) -> dict:
    """Basic Nmap service enumeration (lab-safe flags)"""
    cmd = ["nmap", "-sV", "-sC", "-T4", "--max-retries", "2", target]
    return {"tool": "nmap", "results": run_command(cmd)}

def gobuster_scan(target: str) -> dict:
    """Directory brute-force with common wordlist"""
    cmd = ["gobuster", "dir", "-u", f"http://{target}", "-w", "/usr/share/wordlists/dirb/common.txt", "-q"]
    return {"tool": "gobuster", "results": run_command(cmd)}

def generate_report(target: str, findings: list, output_path: str):
    """Create structured JSON report"""
    report = {
        "scan_metadata": {
            "target": target,
            "timestamp": datetime.now().isoformat(),
            "scope": "lab-only",
            "tool_version": "1.0.0"
        },
        "findings": findings,
        "ethics_note": "All testing performed in authorized, isolated lab environments only."
    }
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"✓ Report saved: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="AutoRecon-X: Lab-Only Recon Pipeline")
    parser.add_argument("-t", "--target", required=True, help="Lab target IP (e.g., 192.168.56.101)")
    parser.add_argument("-o", "--output", default="reports/scan.json", help="Output JSON path")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    # Ethics enforcement
    if not validate_target(args.target):
        print(f"❌ Error: Target {args.target} not in authorized lab ranges: {ALLOWED_RANGES}")
        print("ℹ️  This tool is for isolated lab environments only (OWASP Juice Shop, Metasploitable, TryHackMe).")
        sys.exit(1)

    print(f"🔍 Starting AutoRecon-X scan against {args.target} (LAB MODE)")
    findings = []

    # Run modules
    if args.verbose: print("→ Running Nmap...")
    findings.append(nmap_scan(args.target))
    
    if args.verbose: print("→ Running Gobuster...")
    findings.append(gobuster_scan(args.target))

    # Generate report
    generate_report(args.target, findings, args.output)
    print("✅ Scan complete. Review findings in report.")

if __name__ == "__main__":
    main()
