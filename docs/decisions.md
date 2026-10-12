# Decisions

Things the group has to agree on. Fill in the **Decided** line at the meeting, with the date.
Once something is decided, everyone follows it, so ask here before doing it differently.

## Already decided

| Topic | Decision | Date |
|---|---|---|
| Language | Python | 2026-10-02 |
| Code lives in | This GitHub repo | 2026-10-02 |
| Split | a + b + integration: Neo. c (incl. change password): Yinuo. Student/Subject classes + d: Jeongin. Database + e (GUI): Royce | 2026-10-02 |
| Submit | Thu 22 Oct, before the showcase on Fri 23 Oct | 2026-10-02 |

## Open (meeting Sun 4 Oct)

### 1. Python version
Everyone runs `python3 --version` and reports here. pickle files can break between very different versions.
- Neo: 3.14.7
- Yinuo:
- Jeongin:
- Royce:3.14.7

**Decided:** 

### 2. How students.data is stored
The brief says "read and write objects", which points to `pickle`.

**Decided:** Pickle

### 3. Submitted or corrected Part 1 design?
Two errors in our submitted Part 1 design: "Add a subject" should be an `<<include>>` of Enrol, and
Database to Student should be a `<<use>>` dependency, not an association. The code follows one or the other.

**Decided:**

### 4. Copy the brief's typos?
Matching I/O is marked on wording.
- `Droping Subject-541` (one p). Copy it, or spell it `Dropping`? Ask the tutor if unsure.
- Enrol line shows `Subject-97`, show line shows `Subject::097`. Suggestion: pad to 3 digits everywhere,
  since the brief defines the ID as 3 digits.

**Decided:**

### 5. Coloured output?
The screenshots use colours (cyan menus, red errors, yellow info). Use ANSI escape codes, or plain text?
If yes, agree one shared set of colour constants so all menus look the same.

**Decided:**

### 6. Grade bands
Not stated in the brief. The sample is consistent with the UTS bands:
Z < 50, P 50 to 64, C 65 to 74, D 75 to 84, HD 85+.

**Decided:**

### 7. How menus call each other
Who creates the Database object, and how does a logged-in Student get passed from the Student menu
to the Course menu? Write the answer into [interfaces.md](interfaces.md).

**Decided:**
