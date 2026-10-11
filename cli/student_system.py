import re

EMAIL_PATTERN = r"[a-z0-9_]+(\.?[a-z0-9]+)?@university\.com"
PASSWORD_PATTERN = r"[A-Z][a-zA-Z]{5,}\d{3,}"

def verify_patterns(email, password):
    if re.fullmatch(EMAIL_PATTERN, email):
        if re.fullmatch(PASSWORD_PATTERN, password):
            return True
        else:
            return False
    else:
        return False

def email_login():
    while True:
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        if verify_patterns(email, password):
            print("email and password formats acceptable")
            return email, password
        else:
            print("Incorrect email or password format")

def register():
    email, password = email_login()

def login():
    email, password = email_login()