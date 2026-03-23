

IoT Guardian: Heuristic-Based Security Audit Framework
Lead Researcher: CHIBUZOR NNOLI  
Academic Focus: MSc Cyber Security | Care Home Infrastructure Protection
1. Project Overview
This research artefact is a scalable security auditing system designed for the unique constraints of residential care home IoT environments. By moving beyond traditional signature-based scanning, this tool utilizes a Heuristic Engine to identify vulnerabilities with a minimal resource footprint, ensuring no disruption to sensitive medical equipment.

The project simulates a realistic healthcare facility network using a Multi-Node Star Topology built in a virtualized environment.
2. Network Architecture & Topology
The environment is hosted within a VirtualBox Internal Network, ensuring a secure, sandboxed testing ground isolated from the public internet.

Node	IP Address	Security Personality	Role in Research
Scanner	192.168.1.1	Auditor Node	Master Controller (Flask + Python)
iot-alpha	192.168.1.2	High Risk	Modeling Software Obsolescence
iot-beta	192.168.1.3	Zero Risk	Modeling Hardened/Secure Endpoints
iot-gamma	192.168.1.4	Critical	Modeling Legacy Protocol Insecurity

3. Detailed Target Provisioning (Setup Guide)
To validate the Heuristic Engine, each target VM was manually configured to represent a specific risk profile common in IoT deployments.

 A. iot-alpha: The Vulnerable Web-Server (`192.168.1.2`)
This node simulates an IoT gateway running an outdated web interface.
1.  Install Base OS: Ubuntu 22.04 LTS.
2.  Install Specific Legacy Version:
    ```bash
    sudo apt update
    sudo apt install apache2=2.4.58-1ubuntu8
    ```
3.  Verify Version: Run `apache2 -v` to ensure it displays 2.4.58.
4.  Start Service: `sudo systemctl start apache2`.

 B. iot-beta: The Hardened Endpoint (`192.168.1.3`)
This node represents a modern, secure IoT device with a "Zero-Trust" configuration.
1.  Stop Unnecessary Services: ```bash
    sudo systemctl stop apache2
    sudo systemctl disable apache2
    ```
2.  Enable Firewall (UFW):
    ```bash
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw enable
    ```
3.  Result: The scanner will find the host is online but reports Zero Risk because no ports are listening.

 C. iot-gamma: The Legacy Medical Device (`192.168.1.4`)
This node models an old medical device that uses unencrypted protocols for data transfer.
1.  Install Insecure Services:
    ```bash
    sudo apt install vsftpd apache2=2.4.58-1ubuntu8
    ```
2.  Open Critical Ports:
    ```bash
    sudo ufw allow 21/tcp
    sudo ufw allow 80/tcp
    ```
3.  Configure FTP: Ensure `vsftpd` is running with `sudo systemctl start vsftpd`.
4.  Result: The scanner flags this as CRITICAL due to the presence of Port 21 (FTP).

 4. Heuristic Methodology (Scientific Justification)
The framework employs a Heuristic Logic Engine rather than a standard signature database.

 Pattern Recognition: The engine performs Service Fingerprinting. It analyzes banner strings and applies logical rules: "If service is Apache AND version is < 2.4.62, then Status = High Risk."
 Protocol-Level Analysis: The system identifies Insecure Protocols (like FTP) based on the inherent risk of unencrypted transmission, fulfilling the "Privacy by Design" requirement of healthcare data.
 Operational Efficiency: Because the rules are lightweight, a deep audit of the entire subnet completes in ~8.59 seconds.

---

 5. Technology Stack
 Backend: Python 3.10+
 Scanner Core: `python-nmap` (Nmap 7.80+)
 Web Framework: Flask
 Frontend UI: Bootstrap 5 (Custom Dark Security Theme)
 Editor: Mousepad (Minimal resource overhead)

---

 6. Setup & Execution

 Installation
```bash
 Install system dependencies
sudo apt update && sudo apt install nmap python3-pip

 Install Python requirements
pip install python-nmap flask
```

 Running the System
1.  Initialize the Auditor: Run `python3 app.py`.
2.  Access the Dashboard: Open `http://127.0.0.1:5000` in the browser.
3.  Live Audit: Click "🚀 Start New Audit" to trigger the heuristic engine and generate the latest report.

 7. Performance Metrics
 Audit Duration: ~8.59 seconds.
 Detection Accuracy: 100% success across all 3 Target Personas.
 Resource Footprint: Negligible CPU/RAM impact on the scanner node.

 Lead Researcher
Chibuzor Nnoli MSc Cyber Security Research Project | 2026


