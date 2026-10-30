import random


class Subject:
    def __init__(self):
        self.subject_id = self.generate_subject_id()
        self.mark = self.generate_mark()
        self.grade = self.calculate_grade()

    def generate_subject_id(self):
        return f"{random.randint(1, 999):03d}"
    
    def generate_mark(self):
        return random.randint(25, 100)

    def calculate_grade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "Z"

    def __str__(self):
        return f"[ Subject::{self.subject_id} -- mark = {self.mark} -- grade = {self.grade:>3} ]" #[ Subject::455 -- mark = 57 -- grade =   P ]


if __name__ == "__main__":
    subject1 = Subject() 
    print(subject1)                     

