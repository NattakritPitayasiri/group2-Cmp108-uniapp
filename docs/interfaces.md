# Shared interfaces

Fill this in together at the meeting (ALL.2). It is the contract between our parts: if a name here
changes, tell everyone, because someone else's menu is calling it.

Required by the brief (Section 3): classes `Student`, `Subject`, `Database`.
Optional: controller classes (`StudentController`, `SubjectController`, ...) that hold the menus.

## Files

| File | Contains | Owner |
|---|---|---|
| | | |

## Student (owner: Jeongin)

Brief: `id` is a unique random 6-digit number (000001 to 999999). Fields: name, email, password, list of subjects.
Max 4 subjects. Pass if the average mark is 50 or more.

| Method / field | Arguments | Returns | Used by |
|---|---|---|---|
| | | | |

## Subject (owner: Jeongin)

Brief: `id` is a unique random 3-digit number (001 to 999). `mark` is random, 25 to 100. `grade` comes from the mark.

| Method / field | Arguments | Returns | Used by |
|---|---|---|---|
| | | | |

## Database (owner: Royce)

Brief: check `students.data` exists and create it if not; read and write objects; clear all objects.

| Method | Arguments | Returns | Used by |
|---|---|---|---|
| | | | |

## Menus / controllers

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
