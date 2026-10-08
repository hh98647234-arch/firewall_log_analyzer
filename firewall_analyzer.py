from collections import Counter
log_file = "firewall_logs.txt"
allowed_ips = []
blocked_ips = []
with open(log_file, "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 5:
            action = parts[2]
            ip = parts[3]
        if action == "ALLOW":
            allowed_ips.append(ip)
        elif action == "BLOCK":
            blocked_ips.append(ip)

blocked_counts = Counter(blocked_ips)
print("=== FIREWALL SECURITY REPORT ===")
print("Allowed connections:", len(allowed_ips))
print("Blocked connections:", len(blocked_ips))
for ip, count in blocked_counts.items():
    if count >= 3:
        print(f"ALERT: {ip} - {count} blocked attemps")
    else:
        print(f"IP {ip} - {count} blocked attempts")