________________________________________
IoT Guardian: Heuristic-Based Security Audit Framework
Lead Researcher: CHIBUZOR NNOLI
Academic Focus: MSc Cyber Security | Care Home IoT Protection
1. Project Overview
This research artefact is a scalable security auditing tool designed to identify vulnerabilities in IoT environments (specifically residential care homes). It utilizes a custom Heuristic Engine to fingerprint services and detect outdated software or insecure protocols across multiple network nodes simultaneously.
The system has been upgraded from a single-node test to a Multi-Node Architecture to simulate a real-world facility with multiple residents and diverse medical/IoT devices.
________________________________________
2. Network Architecture & Topology
The environment is built using an Internal/Host-Only virtual network (VirtualBox) to ensure a "sandboxed" and safe auditing process, preventing any external interference.
Device	Role	IP Address	Security Profile
Scanner	Auditor (Flask/Python)	192.168.1.1	Master Controller
IoT-Alpha	Vulnerable Target	192.168.1.2	Outdated Apache 2.4.58
IoT-Beta	Secure Node	192.168.1.3	Hardened (No services)
IoT-Gamma	Legacy Device	192.168.1.4	Insecure FTP (Port 21)
________________________________________
3. Target Provisioning (Vulnerability Modeling)
To evaluate the Heuristic Engine, the three IoT Target VMs were manually provisioned with specific "Security Personas." This was done to model the most common risks found in healthcare IT settings.
Target 1: Outdated Web-Server (192.168.1.2)
•	Risk Modeled: Software Obsolescence (RCE/DDoS Vulnerability).
•	Setup: Provisioned with Apache 2.4.58.
•	Command: sudo apt install apache2=2.4.58-1ubuntu8
Target 2: Hardened Device (192.168.1.3)
•	Risk Modeled: Zero-Trust / Secure Profile.
•	Setup: All non-essential services disabled; internal firewall active.
•	Command: sudo systemctl stop apache2 && sudo ufw enable
Target 3: Legacy Protocol Device (192.168.1.4)
•	Risk Modeled: Clear-text Data Interception.
•	Setup: Provisioned with an unencrypted FTP server (Port 21).
•	Command: sudo apt install vsftpd && sudo systemctl start vsftpd
________________________________________
4. Core Features
•	Subnet-Wide Discovery: Targets specific IPs (.2 through .4) to map the facility's attack surface instantly.
•	Heuristic Logic Engine: Analyzes service banners and port states to detect specific risks (e.g., CVEs associated with Apache 2.4.58).
•	Professional Dashboard: A Flask-based UI providing an Executive Summary, Risk Levels, and Remediation Advice.
•	One-Touch Audit: Users can trigger a full network re-scan directly from the browser with the "Start New Audit" feature.
________________________________________
5. Installation & Execution
Prerequisites
•	OS: Ubuntu 22.04 LTS (Scanner & Targets).
•	Dependencies: sudo apt install nmap python3-pip.
•	Libraries: pip install python-nmap flask.
How to Run
1.	Configure Networking: Ensure all VMs are on the same VirtualBox "Host-Only" adapter.
2.	Initialize Backend: Run python3 scanner.py to ensure the first report is generated.
3.	Launch Web Server: Run python3 app.py.
4.	View Dashboard: Access http://127.0.0.1:5000 in the browser.
________________________________________
6. Evaluation Results
•	Scan Efficiency: Full 3-node deep audit completed in ~8.59 seconds.
•	Detection Accuracy: 100% success rate in identifying the "Vulnerable," "Secure," and "Critical" profiles.
•	Operational Value: Provides clear remediation steps for care home managers, bridging the gap between technical data and executive decision-making.
________________________________________
Lead Researcher
Chibuzor Nnoli MSc Cyber Security Research Project
________________________________________
Would you like me to help you format a "References" section for the README that includes the official Apache security advisories for version 2.4.58?

