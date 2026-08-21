#!/usr/bin/env python3

import socket

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((host, port))
        return result == 0
    finally:
        sock.close()


def main():
    host = input("Enter host to scan (default: 127.0.0.1): ").strip()

    if not host:
        host = "127.0.0.1"

    print(f"\nScanning {host}...\n")

    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-Alt"
    }

    found = 0

    for port, service in common_ports.items():
        if scan_port(host, port):
            print(f"[OPEN] {port:5} - {service}")
            found += 1

    print(f"\nScan complete. Open ports found: {found}")


if __name__ == "__main__":
    main()
