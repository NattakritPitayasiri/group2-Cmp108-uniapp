class AdminSystem:
    def __init__(self, database):
        self.database = database

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
        students = self.database.read_from_file()

        print("\tStudent List")

        if len(students) == 0:
            print("\t\t< Nothing to Display >")
        else:
            for student in students:
                print(f"\t{student}")

    def remove_student(self, student_id):
        students = self.database.read_from_file()

        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                self.database.save_to_file(students)
                return True
        return False

    def clear_all_students(self):
        self.database.delete_from_file()

    def categorise_pass_fail(self):
        students = self.database.read_from_file()

        pass_details = []
        fail_details = []

        for student in students:
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
        students = self.database.read_from_file()

        hd_students = []
        d_students = []
        c_students = []    
        p_students = []
        z_students = []

        for student in students:
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
    from model.database import Database

    database = Database()
    admin = AdminSystem(database)
    admin.admin_subsystem()