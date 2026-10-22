# CLIUniApp and GUIUniApp

UTS 32555 Fundamentals of Software Development, Assessment 1 Part 2.
Group 2, lab Cmp1-08.

A university system with a command-line app (CLIUniApp) for students and admins, and a GUI app
(GUIUniApp) for students. Student data is stored in a local file, `students.data`.

## Requirements

- Python 3.14 (developed and tested with Python 3.14.x)
- Extra libraries: none. Everything comes from the Python standard library.
- GUIUniApp uses `tkinter`. It comes with the standard Python installers for Windows and macOS.
  If `import tkinter` fails (for example with Homebrew Python on macOS), install it with
  `brew install python-tk@3.14` or use the Python from python.org.

## How to run

Run both apps from the project folder.

```bash
# CLIUniApp
python3 cli/cli_uni_app.py

# GUIUniApp
python3 gui/gui_uni_app.py
```

- Both apps read and write the same file, `cli/students.data`. It is created automatically the
  first time you run either app. A student registered in the CLI can log in to the GUI, and the
  other way round.
- To start again with no students, delete `cli/students.data`, or use the Admin menu (`A`, then `c`, then `Y`).
- Admins do not log in. Choose `A` in the University menu to open the Admin menu.

## Project layout

| Folder | What's in it |
|---|---|
| `cli/` | CLIUniApp |
| `gui/` | GUIUniApp |
| `docs/` | Brief, sample I/O, marking checklist, decisions, shared interfaces |

| File | What it does |
|---|---|
| `cli/cli_uni_app.py` | Entry point. University menu and Student menu |
| `cli/student_system.py` | Register and login, email and password patterns |
| `cli/subject_enrolment.py` | Student Course menu: enrol, remove, show subjects, change password |
| `cli/admin_system.py` | Admin menu: list, group by grade, PASS/FAIL, remove, clear |
| `cli/student.py` | `Student` class |
| `cli/subject.py` | `Subject` class |
| `cli/database.py` | `Database` class, reads and writes `students.data` with `pickle` |
| `gui/gui_uni_app.py` | Tkinter GUI. Reuses the files in `cli/` |

## Work split

| Member | Responsible for | Marking scheme |
|---|---|---|
| Neo (Nattakrit) | University menu, Student menu (register, login, regex), integration, README, submission | a, b |
| Yinuo | Subject Enrolment menu, including change password | c |
| Jeongin | `Student` and `Subject` classes, Admin menu | d |
| Chang-Yang (Royce) Shih | `Database` class, GUIUniApp | e |

## Individual contributions

### Neo

Wrote the University menu and the Student menu in `cli_uni_app.py`, and `student_system.py` with the
email and password patterns, register and login. Register checks the format, then checks that the
email is new, then makes a unique 6 digit student id and saves the student. Login reads the saved
students and hands the logged-in `Student` to Yinuo's course menu. Added the error handling for
the student system: wrong formats, an existing email, a blank name, extra spaces and unknown menu
options. Connected the menus to the `Database`, reviewed and merged the group's pull requests,
and wrote the shared docs (sample I/O, decisions, marking checklist), this README, and the submission.

### Yinuo

Wrote `subject_enrolment.py`, the Student Course menu that opens after login. A student can enrol in
up to four subjects, and each new subject gets a random id that is not used by any other student.
A student can remove a subject by id (the id is checked first), show the enrolled subjects, and
change their password with a confirm step that repeats until both entries match. Every change is
saved back to `students.data`. Added error handling for a fifth subject, a bad or unknown subject id
and invalid menu options, and matched the menu wording to the sample output.

### Jeongin

Wrote the `Student` and `Subject` classes and the Admin system. `Student` holds up to four subjects
and can enrol, remove, count and list them, change the password, and work out the average mark, the
overall grade and PASS or FAIL. `Subject` makes a random 3 digit id and a random mark from 25 to 100
and works out the grade. `AdminSystem` lists all students, groups them by grade, splits them into
PASS and FAIL, removes a student by id, and clears the file after a Y or N check. Connected the
Admin menu to the `Database` and wrote the class details in `docs/interfaces.md`.

### Royce

I developed the `Database` class using `pickle` to save and read student data in `students.data`. The database can create the file if it does not exist and return an empty list if the file is empty. I also fixed the file path to make sure the CLI and GUI use the same database. I designed the GUI wireframes and developed `gui_uni_app.py` using Tkinter, including login, registration, enrolment, subject details, and error messages. I also integrated the GUI with the existing CLI functions so both systems can share the same student data. Finally, I tested the integration between the CLI, GUI, and database by registering accounts, logging in, and managing subject enrolments through both interfaces. The functions worked successfully during testing.
