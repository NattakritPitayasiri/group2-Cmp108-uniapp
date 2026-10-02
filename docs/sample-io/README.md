# Sample I/O

Expected program output, typed out from the screenshots in Section 4 of [the brief](../brief.pdf).
"Matching I/O" is worth 1 mark in each of a, b, c and d, so our output should match these files
word for word.

> **Not verified yet.** These were transcribed from the PDF images. Spacing may be off, especially
> inside `grade =   P` and `GRADE:  C`. Check against the PDF before relying on exact spaces.
> Once checked, delete this note.

| File | Scenario | Brief page | Owner |
|---|---|---|---|
| [01-university-system.txt](01-university-system.txt) | University menu, A / S / X | 3 | Neo |
| [02-student-register.txt](02-student-register.txt) | Register, format errors, already exists | 4 | Neo |
| [03-student-login.txt](03-student-login.txt) | Login, wrong password, success | 4 | Neo |
| [04-enrol-and-show.txt](04-enrol-and-show.txt) | Enrol up to 4, show subjects | 5 | Yinuo |
| [05-remove-subject.txt](05-remove-subject.txt) | Remove a subject by ID | 5 | Yinuo |
| [06-change-password.txt](06-change-password.txt) | Change password, mismatch | 6 | Yinuo |
| [07-admin-list-group-partition.txt](07-admin-list-group-partition.txt) | Show, group by grade, PASS/FAIL | 6 | Jeongin |
| [08-admin-remove-and-clear.txt](08-admin-remove-and-clear.txt) | Remove student, clear all | 7 | Jeongin |

## Reading the files

- **Indentation:** each level is one tab, which looks like 8 spaces in the screenshots.
  University menu = no indent, Student and Admin menus = 1 level, Student Course Menu = 2 levels.
- **User input** is the text after the prompt on the same line (for example `: S`).
- **Random values** (student IDs, subject IDs, marks) will differ from ours. Match the format, not the numbers.
- **Colours in the screenshots:** cyan = menu prompts, green = `Student Sign Up` / `Student Sign In`,
  yellow = info and success lines, red = errors. Colour is optional (see [decisions.md](../decisions.md)).

## Things the brief does that are easy to miss

- Register asks for `Name:` **after** the format check and the "already exists" check.
- On a format error, Register and Login loop back to `Email:` without leaving the screen.
- A wrong password at login prints `Student does not exist`, not a separate message.
- Change password: on a mismatch, only `Confirm Password:` is asked again.
- Grades are right-aligned to 3 characters: `grade =   P`, `grade =  HD`.
- Admin group/partition use each student's **average** mark, shown to 2 decimal places.
- `< Nothing to Display >` is indented one extra level.
- Typos in the brief: `Droping` (one p) and `Subject-97` vs `Subject::097`. See [decisions.md](../decisions.md).
