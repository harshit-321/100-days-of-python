# email_slicer_simple.py
import re

def slice_email(email: str):
    """Return (local_part, domain) or raise ValueError if invalid."""
    email = email.strip()
    m = re.match(r'^([^@]+)@(.+)$', email)
    if not m:
        raise ValueError(f"Invalid email: {email}")
    return m.group(1), m.group(2)

if __name__ == "__main__":
    test = input("Enter an email: ").strip()
    try:
        local, domain = slice_email(test)
        print(f"Local part: {local}")
        print(f"Domain:     {domain}")
    except ValueError as e:
        print(e)