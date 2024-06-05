import re

# i. Function to check if a string is a palindrome
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    return s == s[::-1]

# ii. Function to extract email addresses from a string
def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)
