# Shared interfaces

Fill this in together at the meeting (ALL.2). It is the contract between our parts: if a name here
changes, tell everyone, because someone else's menu is calling it.

Required by the brief (Section 3): classes `Student`, `Subject`, `Database`.
Optional: controller classes (`StudentController`, `SubjectController`, ...) that hold the menus.

## Files

| File | Contains | Owner |
|---|---|---|
| `cli/student.py` | Student class | Jeongin |
| `cli/subject.py` | Subject class | Jeongin |
| `cli/admin_system.py` | AdminSystem class | Jeongin |

## Proposed names from the Part 1 class diagram

The class and method names below come from our Part 1 design (story to method trace table). They are a
**proposal** for the meeting: keep, rename or drop each one. Arguments, return values and "Used by" are
still blank on purpose, we fill those in together.

## Student (owner: Jeongin)

Brief: `id` is a unique random 6-digit number (000001 to 999999). Fields: name, email, password, list of subjects.
Max 4 subjects. Pass if the average mark is 50 or more.

| Method / field | Arguments | Returns | Used by |
|---|---|---|---|
| `__init__` | `student_id`, `name`, `email`, `password` | `None` | Student registration |
| `student_id` | — | String, e.g. `"000123"` | Student menu, AdminSystem, Database |
| `name`, `email`, `password` | — | Strings | Student menu, AdminSystem, GUI |
| `subjects` | — | List of Subject objects | Enrolment menu, AdminSystem, GUI |
| `enrol_subject` | `subject`: Subject object | `True` if added; `False` if the four-subject limit is reached | Enrolment menu, GUI |
| `add_subject` | `subject`: Subject object | `None` | Student.enrol_subject |
| `count_subjects` | None | Integer | Student methods, enrolment menu |
| `remove_subject` | `subject_id`: String | `True` if removed; `False` if not found | Enrolment menu, GUI |
| `view_enrolment_list` | None | List of Subject objects | Enrolment menu, GUI |
| `change_password` | `new_password`: String | `None` | Enrolment menu |
| `calculate_average_mark` | None | Average mark; `0.0` if no subjects | Student grade methods, AdminSystem |
| `calculate_overall_grade` | None | `"HD"`, `"D"`, `"C"`, `"P"`, or `"Z"`; `None` if no subjects | AdminSystem.group_by_grade, AdminSystem.categorise_pass_fail |
| `calculate_pass_fail` | None | `"PASS"` or `"FAIL"`; `None` if no subjects | AdminSystem.categorise_pass_fail |
| `__str__` | None | Student details as a string | AdminSystem.view_all_students |

`enrol_subject()` and `remove_subject()` return True on success and False on failure. Feedback messages are handled by the calling menu or GUI.

## Subject (owner: Jeongin)

Brief: `id` is a unique random 3-digit number (001 to 999). `mark` is random, 25 to 100. `grade` comes from the mark.

| Method / field | Arguments | Returns | Used by |
|---|---|---|---|
| `__init__` | None | `None`; creates the subject ID, mark, and grade | Enrolment menu, GUI |
| `subject_id` | — | Three-digit string, e.g. `"097"` | Student.remove_subject, enrolment menu, GUI |
| `mark` | — | Integer from 25 to 100 | Subject.calculate_grade, Student.calculate_average_mark |
| `grade` | — | `"HD"`, `"D"`, `"C"`, `"P"`, or `"Z"` | Subject output |
| `generate_subject_id` | None | Random ID string from `"001"` to `"999"` | Subject.__init__ |
| `generate_mark` | None | Random integer from 25 to 100 | Subject.__init__ |
| `calculate_grade` | None | Grade string calculated from the mark | Subject.__init__ |
| `__str__` | None | Subject details as a string | Enrolment menu, GUI |

Subject generates a random ID but does not check for duplicates.
The enrolment code must check that the ID is unique within the student's subject list before enrolling.

## Database (owner: Royce)

Brief: check `students.data` exists and create it if not; read and write objects; clear all objects.

| Method | Arguments | Returns | Used by |
|---|---|---|---|
| `save_to_file` | | | |Save the student list to student data
| `read_from_file` | | | | Read and return the student list
| `update_file` | | | |update student list
| `delete_from_file` | | | | delete all student records by empty list

## StudentSystem (owner: Neo)

Student menu: register and login.

| Method | Arguments | Returns | Used by |
|---|---|---|---|
| `student_subsystem` | | | |
| `match_credentials` | | | |
| `verify_patterns` | | | |
| `show_error` | | | |
| `register` | | | |
| `verify_email` | | | |
| `verify_password` | | | |
| `generate_student_id` | | | |
| `pad_student_id` | | | |

## AdminSystem (owner: Jeongin)

| Method | Arguments | Returns | Used by |
|---|---|---|---|
| `__init__` | `database`: Database object | `None` | University menu |
| `admin_subsystem` | None | `None`; returns when x is selected | University menu |
| `view_all_students` | None | `None`; prints the student list | Admin menu |
| `group_by_grade` | None | `None`; prints students grouped by overall grade | Admin menu |
| `categorise_pass_fail` | None | `None`; prints FAIL and PASS groups | Admin menu |
| `remove_student` | `student_id`: String | `True` if removed and saved; `False` if not found | Admin menu |
| `clear_all_students` | None | `None`; clears saved student records | Admin menu |

## CLIUniApp (owner: Neo)

| Method | Arguments | Returns | Used by |
|---|---|---|---|
| `main` | | | |
| `university_menu` | | | |

## GUIUniApp (owner: Royce)

| Class | Method | Arguments | Returns |
|---|---|---|---|
| `LoginWindow` | `show_login_window` | | |
| `LoginWindow` | `gui_login` | | |
| `LoginWindow` | `handle_empty_fields` | | |
| `EnrolmentWindow` | `show_enrolment_window` | | |
| `EnrolmentWindow` | `add_to_enrolment_list` | | |
| `EnrolmentWindow` | `handle_limit_exception` | | |

## Menus / controllers

The Part 1 design has no separate class for the Subject Enrolment menu (Yinuo's part). Decide at the meeting:
a new class, or methods on `Student`.

| Menu | Entry point (how another part starts it) | Owner |
|---|---|---|
| University (A/S/X) | | Neo |
| Student (l/r/x) | | Neo |
| Subject Enrolment (c/e/r/s/x) | | Yinuo |
| Admin (c/g/p/r/s/x) | `AdminSystem(database).admin_subsystem()` | Jeongin |
| GUIUniApp | | Royce |

## Shared constants

Regex patterns, colours, file name, etc. Where do they live, and what are they called?

| Name | Value / meaning | Defined in |
|---|---|---|
| | | |
