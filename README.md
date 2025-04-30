# SSH Username Enumerator 🔐

This script uses Paramiko to perform username enumeration against an SSH service. It's useful during a pentest or CTF to identify valid users on a target system.

## 🚀 Features

- Attempts to authenticate with usernames from a wordlist
- Detects and logs valid usernames based on server responses
- Handles various SSH exceptions gracefully
- Simple and easy to extend (e.g. for brute-force modules or threading)

## 🛠️ Usage

1. **Install the required module**:

```bash
pip install paramiko
```

2.	Edit the script to specify:
•	Target IP address
•	Path to your username wordlist

3.	Run it:
```
python ssh_enum.py
```

### Script Parameters
ip = 'x.x.x.x'                   # Target IP
user_path = r'wlist/path'       # Path to your username wordlist
port = 22                       # Optional, default is 22

### Example output:
```
[+] Valid username: admin
[-] Invalid username: root - Authentication failed.
[-] Invalid username: test - Authentication failed.
```
Inside the script, customize:
