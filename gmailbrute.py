import argparse
import itertools
import string
import smtplib
import time

# Function to display ASCII art
def display_ascii_art():
    ascii_art = '''
                            .-....:.-..           
                            .:.::::.:..           
                         ...=:::-:::.-..          
                        ..=++-==::==-=--..        
                        :+==+++=--=---:--.        
                    .....+=+===--:::-=:-=.        
                ...:=+=-...=*+=--::=++-....       
             ..:=+++++**+:...++=-=+-..:==+=...    
            .:=+==+++++***=..:===--..-+=++++=:.   
          ..-====++++++*****+-+-::-=++++======-.  
          .:=====++++++*++=+*+-::.:=++=-=======.  
          .-.....=++--+++=. -=-:..:::++=+======:  
    :::.    ..-+*=*=-===-:..:-:....:....-:..::.:  
    .:-.:---::.-===+**++=*#+-......:......  ....  
             .+=++:.-=--=+++**-::..::.            
            .++*=.======-=--+##--:..-..           
            -++=.+===.-#*=-=-=%+--::-+.           
            ++*:-+++..:*#==+==#*=-:-=-=.          
          ..*++:+++- .:#*==+=*#+===+=--- ......   
          ..+*+-*++-  .**+++*#*+=.:++-==-+-=+=.   
            -*=#+*++==#*++*##*+=....++*#*#*+:..   
            .++-%#*+--+**++++*+=..  :**=          
             .=*-+##*==**####*---.   ..           
             ..:+*=--=++====+*=:..                
                 .:=++++++=-..  
                 @RG&RN                   
    '''
    print(ascii_art)

# Function to get SMTP server based on the domain
def get_smtp_server(domain):
    servers = {
        'gmail.com': [
            'alt1.gmail-smtp-in.l.google.com',
            'alt3.gmail-smtp-in.l.google.com',
            'gmail-smtp-in.l.google.com',
            'alt4.gmail-smtp-in.l.google.com',
            'alt2.gmail-smtp-in.l.google.com'
        ],
        'protonmail.com': ['mail.protonmail.ch'],       
    }
    return servers.get(domain, ['alt1.gmail-smtp-in.l.google.com'])  # Default to Gmail if domain not found

# Function to check if the email is valid using SMTP server
def is_valid_email_smtp(email, smtp_servers, smtp_port, retries=3):
    for attempt in range(retries):
        for smtp_server in smtp_servers:
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.set_debuglevel(0)
                server.helo()
                server.mail('')
                code, message = server.rcpt(email)
                server.quit()
                
                if code == 250:
                    return True
            except Exception as e:
                print(f"Attempt {attempt + 1} - Error checking email: {email} on server {smtp_server} - {e}")
                time.sleep(2)  # Wait before retrying

    return False

# Function to brute-force email based on a pattern and domain
def brute_force_email_pattern(pattern, domain, smtp_port, suffix=None, max_length=4, delay=1, output_file='valid_emails.txt'):
    # Only letters and digits for brute-forcing
    characters = string.ascii_letters + string.digits
    smtp_servers = get_smtp_server(domain)

    print(f"\nBrute-forcing domain: {domain} with SMTP servers: {smtp_servers} on port {smtp_port}")
    
    if '@' in pattern:
        local_part, pattern_domain = pattern.split('@', 1)
    else:
        local_part = pattern
        pattern_domain = domain

    if suffix:
        pattern_domain = suffix.lstrip('@')  # Remove leading @ if present
    
    # Generate positions of * in the pattern
    positions = [i for i, char in enumerate(local_part) if char == '*']
    
    # Open file to append valid emails
    with open(output_file, 'a') as file:
        while True:
            for length in range(1, max_length + 1):
                # Generate all possible combinations of characters for the length
                for combination in itertools.product(characters, repeat=len(positions)):
                    # Create the email candidate by filling in the pattern
                    email_candidate = list(local_part)
                    
                    for index, pos in enumerate(positions):
                        email_candidate[pos] = combination[index]
                    
                    email_candidate = ''.join(email_candidate)
                    email = f"{email_candidate}@{pattern_domain}"
                    
                    print(f"Testing email: {email}")
                    if is_valid_email_smtp(email, smtp_servers, smtp_port):
                        print(f"Email is valid: {email}")
                        print(f"Valid email found: {email}")
                        file.write(f"{email}\n")
                        file.flush()  # Ensure the email is written to the file immediately
                    
                    # Add a delay to avoid rate limiting
                    time.sleep(delay)

def main():
    # Display ASCII art
    display_ascii_art()
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Brute-force email addresses based on a pattern.")
    parser.add_argument("pattern", type=str, help="Email pattern to brute-force (e.g., user*1)")
    parser.add_argument("--domain", type=str, required=True, help="Domain to test (e.g., gmail.com)")
    parser.add_argument("--smtp-port", type=int, default=25, help="SMTP server port (default: 25, e.g., 587)")
    parser.add_argument("--suffix", type=str, help="Suffix to append to the local part of the email (e.g., @gmail.com)")
    parser.add_argument("--output-file", type=str, default='valid_emails.txt', help="File to save valid emails")

    args = parser.parse_args()
    
    # Brute-force emails
    try:
        brute_force_email_pattern(args.pattern, args.domain, args.smtp_port, suffix=args.suffix, output_file=args.output_file)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        print("Exiting...")

if __name__ == "__main__":
    main()
