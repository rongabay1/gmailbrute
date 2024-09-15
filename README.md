Usage
To run the brute-forcing script, use the following format:

bash
Copy code
python email_bruteforce.py <pattern> --domain <domain> [options]
Example:
bash
Copy code
python email_bruteforce.py user* --domain gmail.com --smtp-port 587 --output-file valid_emails.txt
Available Options:
pattern: The email pattern to brute-force (e.g., user*1 where * is replaced by brute-forced characters).
--domain: The email domain to target (e.g., gmail.com).
--smtp-port: The SMTP server port to use (default: 25, can be set to 587 for STARTTLS).
--suffix: (Optional) Appends a domain suffix to the email (e.g., --suffix @gmail.com).
--output-file: Specifies the file to save valid emails (default: valid_emails.txt).
--delay: (Optional) Time (in seconds) to delay between SMTP checks (default: 1 second).
Example Usage with All Options:
bash
Copy code
python email_bruteforce.py john* --domain protonmail.com --smtp-port 587 --suffix @protonmail.com --output-file found_emails.txt --delay 3
Disclaimer
This tool is intended for educational and ethical research purposes only.

The use of this script is strictly for learning how email validation via SMTP works and should only be applied in environments where you have explicit permission to test. Any misuse or illegal activity resulting from the use of this script is the responsibility of the user. The author assumes no liability for any damages or legal consequences that arise from the use of this tool.

License
This project is licensed under the MIT License - see the LICENSE file for details.

vbnet
Copy code

This `README.md` covers everything from installation to usage and includes a disclaimer ensur
