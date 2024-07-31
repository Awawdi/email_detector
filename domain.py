import re

def extract_domains(N, lines):
    # Combine all lines into a single string
    html_fragment = '\n'.join(lines)
    
    # Define the regular expression for matching domains in URLs
    url_pattern = r'https?://(www2?\.)?(([A-Za-z0-9-]+\.)+[A-Za-z0-9]+)'
    
    # Find all matches in the HTML fragment
    matches = re.finditer(url_pattern, html_fragment)
    
    # Extract the second capture group (the domain) from each match
    domains = [match.group(2) for match in matches]
    
    # Remove duplicates and sort lexicographically
    unique_domains = sorted(set(domains))
    
    # Join the unique domains with a semicolon
    result = ';'.join(unique_domains)
    
    return result

# Input handling
N = int(input())
lines = [input() for _ in range(N)]

# Extract and print the domains
print(extract_domains(N, lines))
