# from student import Student
# from subject import Subject
# from admin_system import AdminSystem

# student1 = Student("002340", "John Smith", "john.smith@university.com", "Helloworld123")
# student2 = Student("002341", "Mary Brown", "mary.brown@university.com", "Goodmorning456")
# student3 = Student("002342", "David Lee", "david.lee@university.com", "Welcome789")
# student4 = Student("002343", "Emma Wilson", "emma.wilson@university.com", "Goodnight123")

# subject1 = Subject()
# subject5 = Subject()
# student1.enrol_subject(subject1)
# student1.enrol_subject(subject5)

# grade = student1.calculate_overall_grade()
# average = student1.calculate_average_mark()

# print(f"{student1.name}'s first mark:", subject1.mark)
# print(f"{student1.name}'s second mark:", subject5.mark)
# print(f"{student1.name}'s average mark:", student1.calculate_average_mark())

# print(f"{student1.name} :: {student1.student_id} --> GRADE: {grade:>2} - MARK: {average:.2f}")

# subject2 = Subject()
# student2.enrol_subject(subject2)
# # # print("Mary's mark:", subject2.mark)

# subject3 = Subject()
# student3.enrol_subject(subject3)
# # # print("David's mark:", subject3.mark)

# subject4 = Subject()
# student4.enrol_subject(subject4)
# # # print("Emma's mark:", subject4.mark)

# student_list = [student1, student2, student3, student4]
# admin = AdminSystem(student_list)
# admin.admin_subsystem()
# # # print("Student count:", len(admin.students))
# # # admin.view_all_students()




# # print(admin.remove_student("002340"))
# # print(len(student_list))
# # print(admin.remove_student("002340"))

# # subject1 = Subject()
# # subject2 = Subject()
# # subject3 = Subject()
# # subject4 = Subject()
# # subject5 = Subject()

# # student1.enrol_subject(subject1)
# # student1.enrol_subject(subject2)
# # student1.enrol_subject(subject3)
# # student1.enrol_subject(subject4)
# # student1.enrol_subject(subject5)

# # student1.count_subjects()
# # print(student1.count_subjects())
# # print(subject1.mark)
# # print(subject2.mark)
# # print(student1.calculate_average_mark())
# # print(student1.calculate_overall_grade())
# # print(student1.calculate_pass_fail())
# # print(student1)
# # print(subject1)


from student import Student
from admin_system import AdminSystem
from subject import Subject

student1 = Student("673358", "John Smith", "john.smith@university.com", "Helloworld123")
student2 = Student("762740", "Alen Jones", "alen.jones@university.com", "Newworld123")

subject1 = Subject()
student2.enrol_subject(subject1)

print("Alen's mark:", subject1.mark)

admin = AdminSystem([student1, student2])

admin.view_all_students()
admin.group_by_grade()
admin.categorise_pass_fail()