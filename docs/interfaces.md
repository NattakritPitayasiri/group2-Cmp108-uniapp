# Shared interfaces

Fill this in together at the meeting (ALL.2). It is the contract between our parts: if a name here
changes, tell everyone, because someone else's menu is calling it.

Required by the brief (Section 3): classes `Student`, `Subject`, `Database`.
Optional: controller classes (`StudentController`, `SubjectController`, ...) that hold the menus.

## Files

| File | Contains | Owner |
|---|---|---|
| | | |

## Proposed names from the Part 1 class diagram

The class and method names below come from our Part 1 design (story to method trace table). They are a
**proposal** for the meeting: keep, rename or drop each one. Arguments, return values and "Used by" are
still blank on purpose, we fill those in together.

## Student (owner: Jeongin)

Brief: `id` is a unique random 6-digit number (000001 to 999999). Fields: name, email, password, list of subjects.
Max 4 subjects. Pass if the average mark is 50 or more.

| Method / field | Arguments | Returns | Used by |
|---|---|---|---|
| `enrol_subject` | | | |
| `count_subjects` | | | |
| `remove_subject` | | | |
| `view_enrolment_list` | | | |
| `change_password` | | | |
| `calculate_average_mark` | | | |
| `calculate_overall_grade` | None | String: HD, D, C, P, or Z | AdminSystem.group_by_grade |
| `calculate_pass_fail` | None | String: PASS or FAIL | AdminSystem.categorise_pass_fail |

`enrol_subject()` and `remove_subject()` return True on success and False on failure. Feedback messages are handled by the calling menu or GUI.

## Subject (owner: Jeongin)

Brief: `id` is a unique random 3-digit number (001 to 999). `mark` is random, 25 to 100. `grade` comes from the mark.

| Method / field | Arguments | Returns | Used by |
|---|---|---|---|
| `generate_subject_id` | | | |
| `generate_mark` | | | |
| `calculate_grade` | | | |

## Database (owner: Royce)

Brief: check `students.data` exists and create it if not; read and write objects; clear all objects.

| Method | Arguments | Returns | Used by |
|---|---|---|---|
| `save_to_file` | | | |
| `read_from_file` | | | |
| `update_file` | | | |
| `delete_from_file` | | | |

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
| `admin_subsystem` | | | |
| `view_all_students` | | | |
| `group_by_grade` | | | |
| `categorise_pass_fail` | | | |
| `remove_student` | | | |
| `clear_all_students` | | | |

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
| Admin (c/g/p/r/s/x) | | Jeongin |
| GUIUniApp | | Royce |

## Shared constants

Regex patterns, colours, file name, etc. Where do they live, and what are they called?

| Name | Value / meaning | Defined in |
|---|---|---|
| | | |
