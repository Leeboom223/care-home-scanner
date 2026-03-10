import nmap

# Initialize the Port Scanner engine
nm = nmap.PortScanner()
target_ip = '192.168.1.2'
report_file = 'audit_results.txt'

print("==================================================")
print("   CARE HOME IOT SECURITY AUDIT: " + target_ip)
print("   LEAD RESEARCHER: CHIBUZOR NNOLI")
print("==================================================")

# Performs the Service Version Detection
print("[*] Performing Deep Service Version Scan...")
nm.scan(target_ip, '1-1024', '-sV')

results = "--- DETAILED SECURITY VULNERABILITY REPORT ---\n"
results += "Target Device: " + target_ip + "\n"
results += "Audit Conducted by: Chibuzor Nnoli\n\n"

# FIRST "IF": Checks if the machine is online
if target_ip in nm.all_hosts():
    for proto in nm[target_ip].all_protocols():
        ports = nm[target_ip][proto].keys()
        for port in sorted(ports):
            # Extracting details from the scan engine
            state = nm[target_ip][proto][port]['state']
            service = nm[target_ip][proto][port]['name']
            version = nm[target_ip][proto][port].get('version', 'Unknown')

            # --- THE MISSING LOGIC THAT MAKES IT WORK ---
            finding = "Port: " + str(port) + "/" + proto + " | State: " + state + " | Service: " + service + " | Version: " + version
            
            # HEURISTIC INTELLIGENCE (The ALERT logic)
            if "2.4.58" in version:
                finding += " [!] ALERT: Outdated Service - High Risk for Care Home"
            
            # PRINTING THE RESULT TO THE TERMINAL
            print("[+] " + finding)
            results += finding + "\n"
            # --- END OF THE MISSING LOGIC ---
else:
    print("[-] Error: Target " + target_ip + " is unreachable.")
    results += "Error: Target unreachable during audit.\n"

# Saving the final report for dissertation evidence
with open(report_file, 'w') as f:
    f.write(results)

print("==================================================")
print("[+] PROFESSIONAL AUDIT SAVED AS: " + report_file)
print("==================================================")