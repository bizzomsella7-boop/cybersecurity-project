import urllib.request
from datetime import datetime

print("================================")
print("      HTTPS SECURITY CHECKER")
print("================================")

url = input("Weka URL ya website yako: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = []

report.append("================================")
report.append("      SECURITY ASSESSMENT")
report.append("================================")
report.append(f"Website: {url}")
report.append(f"Time: {time_now}")

try:
    response = urllib.request.urlopen(url, timeout=10)

    report.append(f"Status: {response.status}")

    if url.startswith("https://"):
        report.append("HTTPS: PASS")
    else:
        report.append("HTTPS: REVIEW")

    report.append("")
    report.append("Security Headers:")

    security_headers = {
        "Strict-Transport-Security": "HSTS",
        "Content-Security-Policy": "CSP",
        "X-Content-Type-Options": "X-Content-Type-Options",
        "X-Frame-Options": "X-Frame-Options"
    }

    for header, name in security_headers.items():
        if header in response.headers:
            report.append(f"[PASS] {name}")
        else:
            report.append(f"[REVIEW] {name}")

except Exception as e:
    report.append("[ERROR] Connection failed")
    report.append(f"Reason: {e}")

print("\n".join(report))

with open("security_report.txt", "w") as file:
    file.write("\n".join(report))

print("\nReport saved as: security_report.txt")
