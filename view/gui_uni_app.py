import tkinter as tk
from tkinter import messagebox, simpledialog

from model.database import Database
from controller.student_system import (verify_patterns, generate_student_id, is_id_taken, create_student)
from controller.subject_enrolment import enrol_in_subject, save_student

window = tk.Tk()

def login():
    Email = Email_entry.get().strip()
    Password = Password_entry.get().strip()

    if Email == "" or Password == "":
        messagebox.showwarning("Login Failed", "Enter Email and Password")
        return
    if not verify_patterns(Email, Password):
        messagebox.showwarning("Login Failed", "Invalid Email or Password format")
        return

    students = Database().read_from_file()
    for student in students:
        if student.email == Email and student.password == Password:
            print("Login Successful")
            enrolment(student)
            return
    messagebox.showerror("Login Failed", "Incorrect Email or Password")
def register():
    register_window = tk.Toplevel(window)
    register_window.title("Student Registration")
    register_window.geometry("400x350")

    tk.Label(register_window, text="Student Registration").pack()

    tk.Label(register_window, text="Name").pack()
    Name_entry = tk.Entry(register_window)
    Name_entry.pack()

    tk.Label(register_window, text="Email").pack()
    Email_entry = tk.Entry(register_window)
    Email_entry.pack()

    tk.Label(register_window, text="Password").pack()
    Password_entry = tk.Entry(register_window, show="*")
    Password_entry.pack()

    def submit_register():
       Name = Name_entry.get().strip()
       Email = Email_entry.get().strip()
       Password = Password_entry.get().strip()

       if Name == "" or Email == "" or Password == "":
           messagebox.showwarning("Registration Failed", "Please fill in the fields")
           return
       if not verify_patterns(Email, Password):
            messagebox.showwarning("Registration Failed", "Invalid Email or Password format")
            return
        
       db = Database () #avoid duplicate registration
       student_db = db.read_from_file()

       for student in student_db:
           if student.email == Email:
               messagebox.showwarning("Registration Failed", "Email already exist")
               return

       student_id = generate_student_id()
       while is_id_taken(student_id, student_db):
           student_id = generate_student_id()

       student = create_student(student_id, Name, Email, Password)
       student_db.append(student) #Add to the list
       db.save_to_file(student_db)
       messagebox.showinfo("Registration Successful", f"Welcome, {Name}!")
       register_window.destroy()

    tk.Button(register_window, text="Register", command = submit_register).pack()

def subject_detail(subject):
    detail_window = tk.Toplevel(window)
    detail_window.title("Subject Detail")
    detail_window.geometry("400x300")

    tk.Label(detail_window, text = "Subject Detail").pack()
    tk.Label(detail_window, text = f"Subject ID: {subject.subject_id}").pack()
    tk.Label(detail_window, text = f"Mark: {subject.mark}").pack()
    tk.Label(detail_window, text = f"Grade: {subject.grade}").pack()

    tk.Button(detail_window, text = "Back to Enrolment", command = detail_window.destroy).pack()


def enrolment(student):
    enrolment_window = tk.Toplevel(window)
    enrolment_window.title("Student Enrolment")
    enrolment_window.geometry("400x350")

    tk.Label(enrolment_window, text = "Student Enrolment").pack()
    tk.Label(enrolment_window, text = f"Student: {student.name}").pack()
    Subject_label = tk.Label(enrolment_window, text = f"Enrolled Subjects: {student.count_subjects()} /4")
    Subject_label.pack()
    subjects_frame = tk.Frame(enrolment_window)
    subjects_frame.pack()

    def show_subjects():
        for item in subjects_frame.winfo_children():
            item.destroy()
        for subject in student.view_enrolment_list():
            tk.Button(subjects_frame, text = f"Subject {subject.subject_id} >", command = lambda selected_subject = subject: subject_detail(selected_subject)).pack()
    show_subjects()

    def enrol_subject():
        if student.count_subjects() >= 4:
            messagebox.showwarning("Enrolment Failed", "You cannot enrol in more than 4 subjects")
            return

        enrol_in_subject(student)
        Subject_label.config(text = f"Enrolled Subjects: {student.count_subjects()} /4")
        messagebox.showinfo("Enrolment Successful", "Successful")
        show_subjects()
        
    tk.Button(enrolment_window, text = "Enrol Subject", command = enrol_subject).pack()

    
    def view_subjects():
        subjects = student.view_enrolment_list()

        if not subjects:
           messagebox.showinfo("Enrolment List", "No subjects enrolled.")
           return

        subject_ids = "\n".join(str(subject.subject_id) for subject in subjects)
        messagebox.showinfo("Enrolment List", subject_ids)

    tk.Button(enrolment_window, text="View Enrolment List", command = view_subjects).pack()

    def remove_subject():
        subject_id = simpledialog.askstring("Remove Subject", "Enter Subject ID:") #small window

        if subject_id is None:
            return
        subject_id = subject_id.strip()
        if student.remove_subject(subject_id):
            save_student(student)
            Subject_label.config(text = f"Enrolled Subjects: {student.count_subjects()} /4")
            show_subjects()
            messagebox.showinfo("Remove Successful", "Subject Remove")
        else:
            messagebox.showwarning("Remove Failed", "Subject ID not found")

    tk.Button(enrolment_window, text="Remove Subject", command=remove_subject).pack()
    
window.title("University Application")
window.geometry("400x300") #width x height
title_label = tk.Label(window, text="Student Login")
title_label.pack() #display

Email_label = tk.Label(window, text="Email")
Email_label.pack()  
Email_entry = tk.Entry(window) #enter text
Email_entry.pack()

Password_label = tk.Label(window, text="Password")
Password_label.pack() 
Password_entry = tk.Entry(window, show='*') 
Password_entry.pack() 

Login_button = tk.Button(window, text="Login", command = login)
Login_button.pack() 

Register_button = tk.Button(window, text="Register", command = register)
Register_button.pack()

window.mainloop() 