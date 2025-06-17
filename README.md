# Penetration Testing Toolkit

## Overview
The Penetration Testing Toolkit is a collection of tools designed for ethical hacking and cybersecurity education. This toolkit includes tools for vulnerability scanning and password cracking, helping users identify weaknesses and strengthen their systems.

## Tools Included
1. **Vulnerability Scanner**: Scans for open ports and common web vulnerabilities, such as missing security headers.
2. **Password Cracker**: Demonstrates brute-force and dictionary attacks on hashed passwords.

## Features
- Ethical hacking practices with responsible usage guidelines.
- Secure coding to ensure safe handling of sensitive data.
- Detailed reports for vulnerability scanning and password cracking.

## Tech Stack
- **Programming Language**: Python
- **Libraries**:
  - Networking: `socket`, `scapy`, `paramiko`
  - Web Scanning: `requests`, `beautifulsoup4`
  - Cryptography: `hashlib`, `cryptography`
- **UI/UX**: Command-line interface (CLI) or web-based dashboard.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/didiermu99/Penetration-Testing-Toolkit.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Penetration-Testing-Toolkit
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Vulnerability Scanner
Run the vulnerability scanner:
```bash
python vulnerability_scanner/scanner.py
```

### Password Cracker
Run the password cracker:
```bash
python password_cracker/cracker.py
```

## Disclaimer
This toolkit is intended for educational purposes and ethical penetration testing only. Unauthorized use is prohibited.

## License
See [LICENSE](LICENSE).