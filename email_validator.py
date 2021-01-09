import re

def email_validator(email):

    if '@' not in email:
        return 1

    if email.startswith('@'):
        return 2

    if email.endswith('@'):
        return 3
    
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return 0
    else:
        return 4
