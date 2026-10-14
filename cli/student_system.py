import re
import random
from student import Student

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

def generate_student_id():
        return f"{random.randint(1, 999999):06d}"

def register():
    email, password = email_login()
    student_id = generate_student_id()
    name = input("Name: ").strip()
    student = create_student(student_id, name, email, password)
    #TODO Database check email duplicates
    print(f"Enrolling Student {name}")
    return student

def login():
    email, password = email_login()

def create_student(student_id, name, email, password):
    student = Student(student_id, name, email, password)
    return student