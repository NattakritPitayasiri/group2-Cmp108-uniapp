import re
import random
from student import Student
from database import Database
from subject_enrolment import course_menu

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

def is_id_taken(student_id, student_db):
    for s in student_db:
        if s.student_id == student_id:
            return True
    return False

def register():
    email, password = email_login()
    db = Database()
    student_db = db.read_from_file()
    for s in student_db: #check existing email in db
        if s.email == email:
            print(f"Student {s.name} already exists")
            return
    student_id = generate_student_id()
    while is_id_taken(student_id, student_db): #check duplicated id
        student_id = generate_student_id()

    while True:
        name = input("Name: ").strip()
        if name:
            break
        print("Please fill your name")
    student = create_student(student_id, name, email, password)
    student_db.append(student)
    db.save_to_file(student_db)
    print(f"Enrolling Student {name}")
    return student

def login():
    email, password = email_login()
    student_db = Database().read_from_file()#list of student in database
    for s in student_db:
        if s.email == email and s.password == password:
            course_menu(s)
            return
    print("Student does not exist")


def create_student(student_id, name, email, password):
    student = Student(student_id, name, email, password)
    return student