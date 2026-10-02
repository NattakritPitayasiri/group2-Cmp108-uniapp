# Marking checklist

From Section 6 and 9 of [the brief](brief.pdf). Tick a box only when it works **in the merged app on `main`**,
not just on your own branch. The software must run to get any marks.

## a. University System, 4 marks (Neo)
- [ ] Student: can go to the student menu (1)
- [ ] Admin: can go to the admin menu (1)
- [ ] Browsing: student/admin can move between menus (1)
- [ ] Matching I/O: wording and indentation match [01](sample-io/01-university-system.txt) (1)

## b. Student System, 9 marks (Neo)
- [ ] Register: student can register, data saved to file (2)
- [ ] Login: student can log in, data read from file (2)
- [ ] RegEx: used for both login and register (2)
- [ ] Error handling: exceptions, errors, logical scenarios handled (2)
- [ ] Matching I/O: [02](sample-io/02-student-register.txt), [03](sample-io/03-student-login.txt) (1)

## c. Subject Enrolment System, 15 marks (Yinuo)
- [ ] Enrol: student can enrol in a maximum of 4 subjects (2)
- [ ] Tracking: subject enrolment is tracked (2)
- [ ] Remove a subject: by its ID (2)
- [ ] Show subjects: list all enrolled subjects (1)
- [ ] Change password (2)
- [ ] Read/write to file: student and subject data read from / written to file (3)
- [ ] Error handling (2)
- [ ] Matching I/O: [04](sample-io/04-enrol-and-show.txt), [05](sample-io/05-remove-subject.txt), [06](sample-io/06-change-password.txt) (1)

## d. Admin System, 15 marks (Jeongin)
- [ ] Show students: list all (1)
- [ ] Group students by grade (2)
- [ ] Partition students into PASS/FAIL (2)
- [ ] Remove a student by ID (2)
- [ ] Clear file: remove all students (2)
- [ ] Read/write to file (3)
- [ ] Error handling (2)
- [ ] Matching I/O: [07](sample-io/07-admin-list-group-partition.txt), [08](sample-io/08-admin-remove-and-clear.txt) (1)

## e. GUIUniApp, 7 marks (Royce)
- [ ] Login window: main window, goes to the enrolment window, students read from `students.data` (2)
- [ ] Enrolment window: enrol in a maximum of 4 subjects (2)
- [ ] Subject window: enrolled subjects listed with marks and grades (2)
- [ ] Exception window: format errors, and trying to enrol in more than 4 subjects (1)

## Model classes (Jeongin + Royce, used by everyone)
- [ ] `Student`: random unique 6-digit ID, name, email, password, subjects list, max 4
- [ ] `Subject`: random unique 3-digit ID, random mark 25 to 100, grade from mark
- [ ] `Database`: creates `students.data` if missing, read/write objects, clear all

## Group rules (from Section 7)
- [ ] Everything integrated into one program. If any part can't be integrated, **everyone loses 10%**
- [ ] No AI-generated code (can be marked 0)
- [ ] README lists how we split the work and each person's contribution
- [ ] Zip named `group2-Cmp108.zip`, submitted on Canvas

## f. Showcase, 5 marks (everyone, in person, Fri 23 Oct)
Missing the showcase = **0 for Part 2 and Part 3**.
- [ ] Demo of the working software with all group components (2)
- [ ] Clear speech (1)
- [ ] Walkthrough of the source code showing individual contributions (1)
- [ ] Correct answers to questions (1)
