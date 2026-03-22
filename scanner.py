import nmap
import datetime
import time

# --- CONFIGURATION ---
TARGET_IPS = '192.168.1.2 192.168.1.3 192.168.1.4'
RESEARCHER = "CHIBUZOR NNOLI"
REPORT_FILE = "audit_results.txt"

def run_heuristic_audit():
    nm = nmap.PortScanner()
    start_time = time.time()
    
    print(f"[*] --- CARE HOME IOT SECURITY AUDIT SYSTEM ---")
    print(f"[*] Executing Heuristic Analysis on targets...")
    
    try:
        nm.scan(hosts=TARGET_IPS, arguments='-sV -Pn -T4')
    except Exception as e:
        print(f"\n[!] ERROR: {e}")
        return

    # Tracking stats for the professional summary
    total_hosts = len(nm.all_hosts())
    risky_hosts = 0
    
    audit_log = []
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # --- PROFESSIONAL HEADER & EXECUTIVE SUMMARY ---
    audit_log.append("=" * 60 + "\n")
    audit_log.append(f"  CARE HOME IOT SECURITY AUDIT REPORT\n")
    audit_log.append("=" * 60 + "\n")
    audit_log.append(f"RESEARCHER: {RESEARCHER}\n")
    audit_log.append(f"AUDIT DATE: {timestamp}\n")
    audit_log.append("-" * 60 + "\n")

    host_details = []

    for host in nm.all_hosts():
        host_status = "SECURE"
        host_report = f"\n[+] NODE: {host}\n"
        
        if 'tcp' in nm[host]:
            for port in nm[host]['tcp']:
                service = nm[host]['tcp'][port]['name']
                version = nm[host]['tcp'][port]['version']
                
                # Rule 1: Apache 2.4.58 (Target 1 & 4)
                if "2.4.58" in version:
                    host_report += f"  - ALERT: Port {port} running Outdated Apache 2.4.58\n"
                    host_report += f"    RISK: HIGH (Vulnerable to RCE/DDoS)\n"
                    host_report += f"    ADVICE: Patch Apache to version 2.4.62 or higher.\n"
                    host_status = "HIGH RISK"

                # Rule 2: FTP (Target 3)
                elif port == 21:
                    host_report += f"  - ALERT: Port 21 (FTP) is exposed\n"
                    host_report += f"    RISK: CRITICAL (Clear-text transmission)\n"
                    host_report += f"    ADVICE: Disable FTP and migrate to SFTP (Port 22).\n"
                    host_status = "CRITICAL"

            if host_status != "SECURE":
                risky_hosts += 1
            else:
                host_report += "  - STATUS: Device verified as hardened. No vulnerabilities found.\n"
        else:
            host_report += "  - STATUS: Zero listening services detected. Safe profile.\n"

        host_details.append(host_report)

    # Adding the Executive Summary to the top of the file
    audit_log.append(f"EXECUTIVE SUMMARY:\n")
    audit_log.append(f"  - Total Devices Audited: {total_hosts}\n")
    audit_log.append(f"  - Devices Requiring Attention: {risky_hosts}\n")
    audit_log.append(f"  - Security Compliance: {round(((total_hosts-risky_hosts)/total_hosts)*100)}%\n")
    audit_log.append("-" * 60 + "\n")
    
    # Merge summary with host details
    audit_log.extend(host_details)

    duration = round(time.time() - start_time, 2)
    with open(REPORT_FILE, "w") as f:
        f.writelines(audit_log)
    
    print(f"[*] Audit Complete in {duration}s. Report generated with remediation advice.")

if __name__ == "__main__":
    run_heuristic_audit()