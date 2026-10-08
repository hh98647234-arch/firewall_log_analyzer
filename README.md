# Firewall log analyzer 
A python-based cybersecurity project that analyzes firewall logs and identifies repeated blocked connection attempts.
## Features 
- Read firewall log files
- Identifies ALLOW and BLOCK actions
- Counts allowed and blocked connections
- Extracts IP addresses
- Detects IPs with3 or more blocked attempts
- Generates a basic security reports
  ## Technologies Used
- Python
- Collections counter
- Firewall log analysis
- Basic SOC monitoring
  ## Project files
-`firewall_analyzer.py` - main python script
`firewall_logs.txt` - sample firewall log data
## Example output
```text
=== FIREWALL SECURITY REPORT ===
Allowed connections: 3
Blocked connections: 5
ALERT: 192.168.1.25 - 3 blocked attempts
IP 10.0.0.8 - 2 blocked attempts
```
## Cybersecurity concepts
- Firewall monitoring
- Network traffic analysis
- IP address identification
- Suspicious activity detection
- Security event analysis
  ## Disclaimer
  This project is for educational and cybersecurity learning purpose only. Alerts indicate repeated blocked attempts, not confirmed attacks.
