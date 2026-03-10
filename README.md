Lightweight IoT Risk Assessment Framework (LRAF)
MSc Cybersecurity Dissertation Artefact Lead Researcher: Chibuzor Nnoli
Institution: Teesside University
Focus: Proactive Defense for UK Adult Social Care Infrastructure

This project presents an Integrated Security Prototype designed to address the "Cybersecurity Gap" in underfunded UK care facilities. Utilizing a Heuristic Signature-Based Engine, the framework identifies high-risk IoT vulnerabilities (e.g., legacy Apache services) with a minimal computational footprint, ensuring suitability for low-resource hardware like the Raspberry Pi.
________________________________________
Technical Specifications & Methodology
The development follows the DSRM framework, transitioning from problem identification to a validated technical artefact.
•	Backend Engine: Python 3.12 utilizing python-nmap for service fingerprinting.
•	Intelligent Heuristics: Deterministic logic used to flag Apache 2.4.58 as a high-priority risk.
•	Performance Metrics: Benchmarked at 6.564s total execution time, representing a significant latency reduction over traditional IDS.
•	Frontend: Flask-based web dashboard for non-technical stakeholders.

Network Arrangement (Reproducibility)
The system was evaluated in a Virtualised Sandbox using a private Host-Only Adapter network to ensure ethical isolation.
  Manual Configuration of enp0s3 Interface
To replicate the environment, the following Modern Linux IP Toolset commands were utilized to establish the Layer-3 handshake:
1. Interface Activation
Bash
# Execute on both nodes to administratively enable the virtual NIC
sudo ip link set enp0s3 up
2. Static IP Provisioning
Bash
# Attacker Node (The Scanner)
sudo ip addr add 192.168.1.1/24 dev enp0s3
# Target Node (The IoT Device)
sudo ip addr add 192.168.1.2/24 dev enp0s3

Execution Workflow
1.	Validate Connectivity: Ensure a successful handshake via ICMP: ping 192.168.1.2.
2.	Run Backend Audit: Execute python3 scanner.py to perform the heuristic scan.
3.	Inspect Persistent Logs: Review findings via cat audit_results.txt.
4.	Launch Visualization: Execute python3 app.py and navigate to http://127.0.0.1:5000.

Empirical Evidence
The following results were captured during the Demonstration & Evaluation phase:
MetricResultEvidenceNetwork Stability0% Packet Lossthe_ping_test.pngDetection Accuracy100% (Apache 2.4.58)Detection_accuracy.pngComputational Cost6.564 SecondsComputational_cost.pngSystem VisibilityIntegrated UISystem_visibility.png________________________________________


  To confirm the setup is correct
Users should perform these two checks:
1. Connectivity Proof: Run `ping 192.168.1.2` from the scanner.
 Expected Outcome: 0% packet loss as seen in `the_ping_test.png`.

2. Web Access: Open a browser and navigate to `http://127.0.0.1:5000`.
 Expected Outcome: The Care Home IoT Security Audit dashboard displaying the Apache 2.4.58 alert. See in the ‘system_visibility.png’


