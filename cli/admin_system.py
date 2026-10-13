class AdminSystem:
    def __init__(self, students):
        self.students = students

    def admin_subsystem(self):
        while True:
            selected = input("\tAdmin System (c/g/p/r/s/x): ").lower()

            if selected == "s":
                self.view_all_students()
            elif selected == "g":
                self.group_by_grade()
            elif selected == "p":
                self.categorise_pass_fail()
            elif selected == "r":
                student_id = input("\tRemove by ID: ")
                removed = self.remove_student(student_id)
                if removed:
                    print(f"\tRemoving Student {student_id} Account")
                else:
                    print(f"\tStudent {student_id} does not exist")
            elif selected == "c":
                print("\tClearing students database")
                confirm = input("\tAre you sure you want to clear the database (Y)ES/(N)O: ").upper()
                if confirm == "Y":
                    self.clear_all_students()
                    print("\tStudents data cleared")
            elif selected == "x":
                break
            else:
                print("Invalid choice. Please try again.")    

    def view_all_students(self):
        print("\tStudent List")

        if len(self.students) == 0:
            print("\t\t< Nothing to Display >")
        else:
            for student in self.students:
                print(f"\t{student}")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True
        return False

    def clear_all_students(self):
        self.students.clear()

    def categorise_pass_fail(self):
        pass_details = []
        fail_details = []

        for student in self.students:
            grade = student.calculate_overall_grade()

            if grade is None:
                continue

            average = student.calculate_average_mark()
            detail = f"{student.name} :: {student.student_id} --> GRADE: {grade:>2} - MARK: {average:.2f}"

            if student.calculate_pass_fail() == "PASS":
                pass_details.append(detail)
            else:
                fail_details.append(detail)

        print("\tPASS/FAIL Partition")
        print(f"\tFAIL --> [{', '.join(fail_details)}]")
        print(f"\tPASS --> [{', '.join(pass_details)}]")

    def group_by_grade(self):
        hd_students = []
        d_students = []
        c_students = []    
        p_students = []
        z_students = []

        for student in self.students:
            grade = student.calculate_overall_grade()

            if grade is None:
                continue

            average = student.calculate_average_mark()
            detail = f"{student.name} :: {student.student_id} --> GRADE: {grade:>2} - MARK: {average:.2f}"

            if grade == "HD":
                hd_students.append(detail)
            elif grade == "D":
                d_students.append(detail)
            elif grade == "C":
                c_students.append(detail)
            elif grade == "P":
                p_students.append(detail)
            elif grade == "Z":
                z_students.append(detail)

        print("\tGrade Grouping")
        if not (hd_students or d_students or c_students or p_students or z_students):
            print("\t\t< Nothing to Display >")

        if z_students:
            print(f"\tZ  --> [{', '.join(z_students)}]")
        if p_students:
            print(f"\tP  --> [{', '.join(p_students)}]")
        if c_students:
            print(f"\tC  --> [{', '.join(c_students)}]")
        if d_students:
            print(f"\tD  --> [{', '.join(d_students)}]")
        if hd_students:
            print(f"\tHD --> [{', '.join(hd_students)}]")


if __name__ == "__main__":
    from student import Student
    from subject import Subject

    student1 = Student("673358", "John Smith", "john.smith@university.com", "Helloworld123")
    student2 = Student("762740", "Alen Jones", "alen.jones@university.com", "Goodmorning123")

    subject1 = Subject()
    student1.enrol_subject(subject1)

    subject2 = Subject()
    student2.enrol_subject(subject2)
    
    admin = AdminSystem([student1, student2])
    admin.admin_subsystem()