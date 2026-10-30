# How we work in this repo

New to git? Read this once from top to bottom. It's everything you need for this project.

## Rules

1. **Write your own code.** The brief says AI-generated code can get 0, and each of us has to explain
   our code at the showcase. Asking AI to explain an error or a concept is fine. Pasting its code in is not.
2. **Never commit straight to `main`.** Work on your own branch and open a pull request (PR).
3. **Pull before you start** every session, so you're working on the latest code.
4. **Don't rename shared things alone.** If you change a class, method or file in
   [docs/interfaces.md](docs/interfaces.md), tell the group first.
5. **Commit small and often**, with a message that says what you did. Your commit history is
   evidence of your contribution.

## One-time setup

1. Install git: https://git-scm.com/downloads (on Mac it may already be there: run `git --version`).
2. Accept the GitHub invite in your email.
3. Tell git who you are (use the email of your GitHub account):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
4. Download the repo:
   ```bash
   git clone https://github.com/NattakritPitayasiri/group2-Cmp108-uniapp.git
   cd group2-Cmp108-uniapp
   ```

Prefer clicking to typing? VS Code's Source Control panel (the branch icon on the left) or
GitHub Desktop (https://desktop.github.com) do all of the below with buttons.

## Every work session

```bash
# 1. Get the latest main
git checkout main
git pull

# 2. Go to your branch (first time: add -b to create it)
git checkout -b yourname/what-you-are-doing     # first time
git checkout yourname/what-you-are-doing        # after that

# 3. Bring main's latest changes into your branch
git merge main

# 4. ...write code, run it, test it...

# 5. Save your work
git status                        # see what changed
git add controller/the_file_you_changed.py
git commit -m "Add enrol option to course menu"

# 6. Upload it
git push -u origin yourname/what-you-are-doing
```

Branch names: `neo/...`, `yinuo/...`, `jeongin/...`, `royce/...`.
For example `yinuo/course-menu` or `royce/database`.

## Getting your work into main

1. Push your branch (step 6 above).
2. On GitHub, click **Compare & pull request**.
3. Fill in the checklist in the PR description.
4. Ask one teammate to look at it. When it's OK, click **Merge**.
5. Back on your laptop: `git checkout main` then `git pull`.

## When git says CONFLICT

It means you and someone else changed the same lines. Don't panic, nothing is lost.

1. Open the file. You'll see:
   ```
   <<<<<<< HEAD
   your version
   =======
   their version
   >>>>>>> main
   ```
2. Edit it so it's the version you want, and delete the `<<<<<<<`, `=======`, `>>>>>>>` lines.
   VS Code shows buttons for "Accept Current / Incoming / Both".
3. Then:
   ```bash
   git add the_file.py
   git commit
   ```
4. Not sure which version is right? Ask the person who wrote the other part before choosing.

## Don't commit

- `students.data`: everyone's test data is different. It's already in `.gitignore`.
- `__pycache__/`, `.venv/`, `.DS_Store`: also ignored.

## Useful files

- [docs/brief.pdf](docs/brief.pdf): the assessment brief
- [docs/sample-io/](docs/sample-io/): what our output must look like
- [docs/marking-checklist.md](docs/marking-checklist.md): what gets marks, by owner
- [docs/interfaces.md](docs/interfaces.md): shared class and method names
- [docs/decisions.md](docs/decisions.md): what we've agreed
