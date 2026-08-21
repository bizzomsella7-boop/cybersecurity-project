#!/usr/bin/env python3

import socket
import ipaddress

print("=" * 50)
print("        NETWORK SECURITY SCANNER")
print("=" * 50)

target = input("Enter IP address (your own network/device): ").strip()

try:
    ipaddress.ip_address(target)
except ValueError:
    print("Invalid IP address.")
    exit()

print(f"\nScanning: {target}")
print("-" * 50)

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    8080: "HTTP-Proxy"
}

for port, service in common_ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN]   Port {port:<5} {service}")
    else:
        print(f"[CLOSED] Port {port:<5} {service}")

    sock.close()

print("-" * 50)
print("Scan complete.")
