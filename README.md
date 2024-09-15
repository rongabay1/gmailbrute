# Email Brute-Forcing Script using SMTP (Gmail & ProtonMail)

This Python script is designed to brute-force email addresses using SMTP validation. It supports common email providers such as Gmail and ProtonMail and allows for flexible email patterns, SMTP server selection, and custom delays to avoid rate limiting.

## Features

- Brute-force email addresses based on a pattern (e.g., `user*1` where `*` is replaced by letters/numbers)
- Supports Gmail and ProtonMail SMTP servers (additional servers can be added)
- Validates emails using SMTP with custom ports (e.g., 587 for STARTTLS)
- Optional suffix appending to email addresses
- Ability to save valid email addresses to a specified file
- Custom delays to manage rate limiting or avoid detection
- ASCII art for a visual start

## Requirements

- Python 3.x
- `smtplib` (Standard library for SMTP)
- `argparse` (Standard library for argument parsing)
- Internet connection for SMTP queries

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/email-bruteforce-smtp.git
   cd email-bruteforce-smtp
2. Install the required Python packages (if not already installed):
```bash
pip install -r requirements.txt  # If you have additional dependencies to add
```
3. Ensure SMTP access is not blocked by your network or provider.

# Usage
To run the brute-forcing script, use the following format:

```bash
python gmailbrute.py <pattern> --domain <domain> [options]
python email_bruteforce.py user* --domain gmail.com --smtp-port 587 --output-file valid_emails.txt
```

Available Options:
pattern: The email pattern to brute-force (e.g., user*1 where * is replaced by brute-forced characters).
--domain: The email domain to target (e.g., gmail.com).
--smtp-port: The SMTP server port to use (default: 25, can be set to 587 for STARTTLS).
--suffix: (Optional) Appends a domain suffix to the email (e.g., --suffix @gmail.com).
--output-file: Specifies the file to save valid emails (default: valid_emails.txt).
--delay: (Optional) Time (in seconds) to delay between SMTP checks (default: 1 second).

```bash
python email_bruteforce.py john* --domain protonmail.com --smtp-port 587 --suffix @protonmail.com --output-file found_emails.txt --delay 3
```
## Disclaimer
This tool is intended for educational and ethical research purposes only.

The use of this script is strictly for learning how email validation via SMTP works and should only be applied in environments where you have explicit permission to test. Any misuse or illegal activity resulting from the use of this script is the responsibility of the user. The author assumes no liability for any damages or legal consequences that arise from the use of this tool.

## Contributing to a Project
@ronen1n
