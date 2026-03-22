This **README.md** is designed for an MSc-level cybersecurity dissertation project. It explains the transition from a single-node test to a **Multi-Target Heuristic Framework**, which is exactly what your supervisor wanted to see.

---

# IoT Guardian: Heuristic-Based Security Audit Framework
**Lead Researcher:** CHIBUZOR NNOLI  
**Academic Focus:** MSc Cyber Security | Care Home IoT Protection



## 1. Project Overview
This project is a scalable security auditing tool designed to identify vulnerabilities in IoT environments (specifically care homes). It utilizes a **Heuristic Engine** to fingerprint services and detect outdated software or insecure protocols across multiple network nodes.

The system has been upgraded from a Peer-to-Peer setup to a **Multi-Node Architecture** to simulate a real-world facility with multiple residents and devices.

---

## 2. Network Architecture
The environment is built using an **Internal/Host-Only** virtual network to ensure a "sandboxed" and safe auditing process.

| Device | Role | IP Address | Security Profile |
| :--- | :--- | :--- | :--- |
| **Scanner** | Auditor (Flask/Python) | `192.168.1.1` | Master Controller |
| **IoT-Alpha** | Vulnerable Target | `192.168.1.2` | Outdated Apache 2.4.58 |
| **IoT-Beta** | Secure Node | `192.168.1.3` | Hardened (No services) |
| **IoT-Gamma** | Legacy Device | `192.168.1.4` | Insecure FTP (Port 21) |

---

## 3. Core Features
* **Subnet-Wide Discovery:** Scans targeted IPs (`.2` through `.4`) to map the facility's attack surface.
* **Heuristic Engine:** Analyzes service banners to detect specific risks (e.g., CVEs associated with Apache 2.4.58).
* **Web Dashboard:** A professional Flask-based UI providing an **Executive Summary** and **Remediation Advice**.
* **One-Touch Audit:** Trigger a full network re-scan directly from the browser.



---

## 4. Installation & Setup

### **Prerequisites**
* **Linux Environment:** Ubuntu 22.04+ recommended.
* **Nmap:** `sudo apt install nmap`
* **Python Libraries:** ```bash
    pip install python-nmap flask
    ```

### **Execution**
1.  **Start the Target VMs:** Ensure all IoT clones are running with their assigned IPs.
2.  **Initialize the Backend:**
    ```bash
    python3 scanner.py
    ```
3.  **Launch the Web Dashboard:**
    ```bash
    python3 app.py
    ```
4.  **Access:** Open `http://localhost:5000` in your browser.

---

## 5. Evaluation & Performance
During the testing phase, the system demonstrated high efficiency:
* **Scan Duration:** ~8.59 seconds for a 3-node deep audit.
* **Accuracy:** 100% detection rate of targeted vulnerabilities (Apache 2.4.58 & FTP).
* **Scalability:** The framework handles multi-node clusters without exponential increases in latency.

---

## 6. Research Significance
This artefact demonstrates that low-power hardware in care home environments can be protected using **lightweight heuristic scanning** rather than heavy, expensive enterprise solutions. It bridges the gap between high-level security needs and budget-constrained healthcare settings.

---

### **Lead Researcher Contact**
**Chibuzor Nnoli** *MSc Cyber Security Research Project*

---

**Would you like me to add a "License" section (like MIT or GPL) to this README to make it look even more like a professional open-source project?**
