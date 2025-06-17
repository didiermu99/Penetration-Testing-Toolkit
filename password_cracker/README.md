# Password Cracker

## Overview
The Password Cracker tool demonstrates brute-force and dictionary attacks on hashed passwords. It is designed for educational purposes to showcase the importance of strong passwords and secure hashing algorithms.

## Features
1. **Hashing Algorithms Supported**:
   - MD5
   - SHA-1
   - SHA-256

2. **Dictionary Attack**:
   - Tests passwords from a wordlist against the given hash.

3. **Brute Force Attack** (Future Work):
   - Generate and test passwords systematically (not implemented yet).

## Installation
1. Navigate to the `password_cracker` directory:
   ```bash
   cd password_cracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the cracker:
   ```bash
   python cracker.py
   ```

2. Input the following when prompted:
   - The hash to crack.
   - The hashing algorithm (e.g., `md5`, `sha1`, `sha256`).
   - The path to the wordlist file.

## Example
### Input
Hash: `5d41402abc4b2a76b9719d911017c592`  
Algorithm: `md5`  
Wordlist: `password_cracker/wordlist.txt`

### Output
```
Attempting to crack md5 hash: 5d41402abc4b2a76b9719d911017c592
Password found: hello
```

## Disclaimer
This tool is intended for educational purposes and ethical penetration testing only. Unauthorized use is prohibited.

## License
This tool is licensed under the [MIT License](../LICENSE).