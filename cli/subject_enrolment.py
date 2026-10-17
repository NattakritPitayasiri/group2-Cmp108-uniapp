from database import Database
from subject import Subject

def is_subject_id_taken(subject_id, students):
    for saved_student in students:
        for saved_subject in saved_student.view_enrolment_list():
            if saved_subject.subject_id == subject_id:
                return True
    return False

def create_unique_subject():
    database = Database()
    students = database.read_from_file()
    subject = Subject()
    while is_subject_id_taken(subject.subject_id, students):
        subject = Subject()
    return subject

def enrol_in_subject(student):
    subject = create_unique_subject()
    if student.enrol_subject(subject):
        print(f"\t\tEnrolling in Subject-{subject.subject_id}")
        print(f"\t\tYou are now enrolled in "
              f"{student.count_subjects()} out of 4 subjects")
        save_student(student)
    else:
        print("\t\tStudents are allowed to enrol in 4 subjects only")

def remove_enrolled_subject(student):
    subject_id = input("\t\tRemove Subject by ID: ").strip()
    if student.remove_subject(subject_id):
        print(f"\t\tDropping Subject-{subject_id}")
        print(f"\t\tYou are now enrolled in "
              f"{student.count_subjects()} out of 4 subjects")
        save_student(student)

def save_student(student):
    database = Database()
    students = database.read_from_file()

    for index in range(len(students)):
        if students[index].student_id == student.student_id:
            students[index] = student
            database.update_file(students)
            return

def course_menu(student):
    while True:
        course_action = input(
            "\t\tStudent Course Menu (c/e/r/s/x): "
        ).strip().lower()
        if course_action == "c":
            pass
        elif course_action == "e":
            enrol_in_subject(student)
        elif course_action == "r":
            remove_enrolled_subject(student)
        elif course_action == "s":
            pass
        elif course_action == "x":
            break
