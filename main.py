import re

def extract_emails(text_fragment):
    # REGEX for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text_fragment)
    unique_emails = sorted(set(emails))
    
    # Join the unique email addresses with a semicolon
    result = ';'.join(unique_emails)
    
    return result

# read from user 
N = int(input())
text_fragment = ''.join([input() + '\n' for _ in range(N)])

# Extract and print the result
print(extract_emails(text_fragment))
