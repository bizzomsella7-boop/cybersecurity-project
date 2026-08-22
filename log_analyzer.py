#!/usr/bin/env python3

import re
from collections import Counter

LOG_FILE = "sample_auth.log"


def analyze_log(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"[ERROR] Log file not found: {filename}")
        return

    failed_logins = []
    successful_logins = []
    ip_addresses = []

    for line in lines:
        if "Failed password" in line:
            failed_logins.append(line.strip())

        if "Accepted password" in line:
            successful_logins.append(line.strip())

        ips = re.findall(r"(?:\d{1,3}\.){3}\d{1,3}", line)
        ip_addresses.extend(ips)

    ip_counter = Counter(ip_addresses)

    print("\n===== CYBERSECURITY LOG ANALYZER =====")
    print(f"Log file: {filename}")
    print(f"Total log entries: {len(lines)}")
    print(f"Failed login attempts: {len(failed_logins)}")
    print(f"Successful login attempts: {len(successful_logins)}")

    print("\n--- IP ADDRESS ACTIVITY ---")

    if ip_counter:
        for ip, count in ip_counter.most_common():
            print(f"{ip}: {count} event(s)")
    else:
        print("No IP addresses found.")

    print("\n--- FAILED LOGIN ATTEMPTS ---")

    if failed_logins:
        for attempt in failed_logins:
            print(attempt)
    else:
        print("No failed login attempts found.")

    print("\n===== ANALYSIS COMPLETE =====")


if __name__ == "__main__":
    analyze_log(LOG_FILE)
