Website Security Audit Report

1. Overview

This report documents a basic passive security configuration assessment of:

Target: "github.com"

Assessment type: SSL/TLS, HTTP Security Headers, and Basic Security Configuration
Method: Passive HTTP header and certificate inspection
Tools: "curl", "OpenSSL"
Authorization: Publicly accessible target; no intrusive testing was performed.

---

2. SSL/TLS Assessment

Certificate

- Subject: "CN=github.com"
- Issuer: Sectigo Public Server Authentication CA DV E36
- Valid From: July 3, 2026
- Valid Until: September 30, 2026

Result

PASS — The certificate presented for "github.com" matched the expected domain and was valid at the time of assessment.

---

3. HTTP Security Headers

Security Control| Result
Strict-Transport-Security| PASS
Content-Security-Policy| PASS
X-Frame-Options| PASS
X-Content-Type-Options| PASS
Referrer-Policy| PASS

Observations

HSTS

The server returned:

"max-age=31536000; includeSubDomains; preload"

This indicates that browsers are instructed to use HTTPS for an extended period.

Content Security Policy

A Content-Security-Policy header was present and configured with restrictive directives.

Clickjacking Protection

"X-Frame-Options: deny"

This prevents the page from being embedded in frames.

MIME Sniffing Protection

"X-Content-Type-Options: nosniff"

This helps prevent browsers from MIME-sniffing responses.

Referrer Policy

A restrictive Referrer-Policy was present.

---

4. Cookie Security Observations

The response included cookies using security attributes such as:

- "Secure"
- "HttpOnly"
- "SameSite=Lax"

These attributes provide additional protection against common client-side and cross-site attacks.

Note: Cookie values were intentionally excluded from this report.

---

5. Basic Server Configuration

Observed headers included:

- "Cache-Control: max-age=0, private, must-revalidate"
- "Server: github.com"

No "Access-Control-Allow-Origin" header was observed in the tested response.

No redirect or "Allow" header was observed in the tested response.

The absence of these headers in this particular response is not, by itself, evidence of a vulnerability.

---

6. Overall Assessment

Rating: Strong — 9/10

The tested configuration demonstrated several good security practices:

- Valid TLS certificate
- HTTPS enforced with HSTS
- Content Security Policy
- Clickjacking protection
- MIME sniffing protection
- Referrer policy
- Secure cookie attributes

No obvious security misconfiguration was identified through this limited passive assessment.

---

7. Limitations

This assessment was intentionally limited to passive inspection.

It did not include:

- Authentication testing
- Vulnerability exploitation
- Password testing
- Brute-force testing
- Port scanning
- SQL injection testing
- Cross-site scripting exploitation
- Access-control testing
- Internal infrastructure testing

Therefore, this report should not be interpreted as proof that the target is completely secure.

---

8. Commands Used

curl -I "https://github.com"

openssl s_client -connect "github.com:443" \
  -servername "github.com" </dev/null 2>/dev/null |
  openssl x509 -noout -subject -issuer -dates

curl -sI "https://github.com" |
  grep -Ei 'strict-transport-security|content-security-policy|x-frame-options|x-content-type-options|referrer-policy|permissions-policy'

---

9. Conclusion

The basic passive security assessment of "github.com" identified a strong HTTPS and HTTP security-header configuration.

The assessment provides a useful demonstration of basic website security auditing using standard Linux security tools such as "curl" and "OpenSSL".

Assessment status: COMPLETE
