from subject import Subject


class Student:

    def __init__(self, student_id, name, email, password):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def enrol_subject(self, subject):
        if self.count_subjects() < 4:
            self.add_subject(subject)
            return True
        else:
            return False

    def add_subject(self, subject):
        self.subjects.append(subject)

    def count_subjects(self):
        return len(self.subjects)
        
    def remove_subject(self, subject_id):
        for subject in self.subjects:
            if subject.subject_id == subject_id:
                self.subjects.remove(subject)
                return True
        return False

    def view_enrolment_list(self):
        return self.subjects

    def change_password(self, new_password):
        self.password = new_password

    def calculate_average_mark(self):
        if self.count_subjects() == 0:
            return 0.0
        total = 0
        for subject in self.subjects:
            total += subject.mark
        return total / self.count_subjects()

    def calculate_overall_grade(self):
        if self.count_subjects() == 0:
            return None
        
        average = self.calculate_average_mark()
        if average >= 85:
            return "HD"
        elif average >= 75:
            return "D"
        elif average >= 65:
            return "C"
        elif average >= 50:
            return "P"
        else:
            return "Z"

    def calculate_pass_fail(self):
        if self.count_subjects() == 0:
            return None
        
        average = self.calculate_average_mark()
        if average >= 50:
            return "PASS"
        else:
            return "FAIL"

    def __str__(self):
        return f"{self.name} :: {self.student_id} --> Email: {self.email}" # John Smith :: 673358 --> Email: john.smith@university.com


if __name__ == "__main__":

    student1 = Student("002340", "John Smith", "john.smith@university.com", "Helloworld123")
    student2 = Student("673358", "Grace Choi", "grace.choi@university.com", "Goodmorning123")

    for i in range(5):
        subject = Subject()
        result = student1.enrol_subject(subject)
        print(result)

    for subject in student1.view_enrolment_list():
        print(subject)

    first_subject = student1.view_enrolment_list()[0]
    result = student1.remove_subject(first_subject.subject_id)
    print("Remove result: ", result)
    print("Subject count: ", student1.count_subjects())

    result = student1.remove_subject("000")
    print("Remove result: ", result)
    print("Subject count: ", student1.count_subjects())

    print("Average mark: ", student1.calculate_average_mark())
    print("Grade: ", student1.calculate_overall_grade())
    print("Pass/Fail: ", student1.calculate_pass_fail())

    print(student1)
    print(student2)
    print(student2.calculate_average_mark())
    print(student2.calculate_overall_grade())
    print(student2.calculate_pass_fail())

   