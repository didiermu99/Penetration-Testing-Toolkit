# Example: Vulnerability Scanner

## Input
Target URL: `http://example.com`

## Output
```
Scanning ports on example.com...
Open ports on example.com: [80, 443]
Checking HTTP headers for http://example.com...
HTTP Header Issues:
 - Missing X-Content-Type-Options
 - Missing X-Frame-Options
 - Missing Content-Security-Policy
```