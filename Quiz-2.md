Here is a complete, structured assignment handout ready to share with your students.

# Quiz-2
## Due Date: 09/10, During class time
## Points: 20


# If there is missing information or confusion, please make assumptions yourself. My goal is to see whether you know how to create a branch, do a PR, and resolve conflicts.


## Roles

* **Student A:** Repository Owner & Initial Committer
* **Student B:** Collaborator

---

## Starter Code: `calculator.py`

This initial script will be placed on the `main` branch.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate():
    print("Welcome to the Pair Calculator!")
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))

if __name__ == "__main__":
    calculate()

```

---

1. **Setup & Invitation:** Student A creates; Student B joins.
1. **Student A:**
* Create a new GitHub repository named `git-calculator-cs325` (set to Public IMPORTANT).
* Do git init and set up remote.

```bash
git add calculator.py
git commit -m "feat: initial calculator setup"
git push origin main

```

* In Github Go to **Settings > Collaborators > Add people** and invite **Student B**.

2. **Student B:**
* Accept the invitation via email or GitHub notifications.
* Clone the repository to your local machine:

```bash
git clone <repo-url>

```


2. **Round 1: PR Review Workflow:** Student A writes code, Student B reviews (Request Changes then Approve).
1. **Student A creates a feature branch:**

```bash
git checkout -b feature/multiply # -b means branch

```

```bash
# Alternative way to do this
git branch feature/login   # Step 1: Create the branch
git checkout feature/login # Step 2: Switch to it
```


* Add a `multiply(a, b)` function to `calculator.py`, currently you only have `add()` and `subtract()`:

```python
def multiply(a, b):
    return a * b

```

* Commit and push:

```bash
git add calculator.py
git commit -m "feat: add multiply function"
git push -u origin feature/multiply

```

* Open a **Pull Request (PR)** on GitHub targeting `main`. Assign **Student B** as the reviewer.

2. **Student B reviews (Reject/Request Changes):**
* **Student B** must run `git fetch` to see the new branch locally.
* Select **Request changes** with a comment: *"Please add a print statement for multiplication in calculate() as well."* Please look into the code only `welcome`, `addition` and `subtract` is there no `multiply` so ask the student to add it. So basically you are not accepting the PR but asking for more things to get done.


3. **Student A fixes and updates:**
* Update `calculate()` to call `multiply(5, 3)`.
* Commit and push on the same branch (`git push origin feature/multiply`).


4. **Student B approves and merges:**
* Review the new commit, click **Approve**, and then click **Merge pull request**.




3. **Round 2: Reverse PR Review Workflow:** Student B writes code, Student A reviews (now the roles will be reversed).
1. **Both Students synchronize `main`:**

```bash
git checkout main
git pull origin main # you need a updated main

```

2. **Student B creates a feature branch:**

```bash
git checkout -b feature/divide # Creating a new branch

```

* Add a `divide(a, b)` function:

```python
def divide(a, b):
    return a / b

```

* Commit and push:

```bash
git add calculator.py
git commit -m "feat: add divide function"
git push -u origin feature/divide

```

* Open a PR on GitHub targeting `main`. Assign **Student A** as the reviewer.

3. **Student A reviews (Request Changes):**
* Select **Request changes** with a comment: *"Please handle division by zero safely before we merge."*


4. **Student B fixes and updates:**
* Update `divide(a, b)` to check `if b == 0: return "Error: Division by zero"`.
* Commit and push to `feature/divide`.


5. **Student A approves and merges:**
* Submit an **Approve** review and merge the PR into `main`.




4. **Round 3: Intentional Merge Conflict & Resolution:** Both edit the exact same lines simultaneously.
1. **Both Students pull the latest `main`:**

```bash
git checkout main
git pull origin main

```

2. **Create individual branches:**
* **Student A:**



```bash
git checkout -b fix/student-a

```

Change the following line in (I think line-8) `calculator.py` to:

```python
print("=== Team Calculator: Version A ===")

```

Commit and push:

```bash
git commit -m "chore: update welcome banner A"
git push -u origin fix/student-a

```

then push into the `main` branch too

```bash
# 1. Switch back to main
git checkout main

# 2. Merge the feature branch into local main
git merge fix/student-a

# 3. Push the updated main to GitHub
git push origin main
```

You just pushed into the main branch. It is always advisable to create a PR whenever there is a change of code and many people are working on it. There is nothing like "this is my branch" remember. 

* **Student B:**

```bash
git checkout -b fix/student-b

```

Change line 8??? in `calculator.py` to:

```python
print(">>> Super Calculator: Version B <<<")

```

Commit and push:

```bash
git commit -m "chore: update welcome banner B"
git push -u origin fix/student-b

```

```
 *Open PR #4 targeting `main`.* So you compare `main` branch with the branch `student-b` while creating a PR.

```

3. **Notice the Conflict:**
* GitHub will block PR #4, showing: **"Can't automatically merge. Don't worry, you can still create the pull request."**


4. **Resolve the Conflict locally (Student B):**

```bash
git checkout fix/banner-b
git pull origin main

```

* Git will inject conflict markers inside `calculator.py`:

```python
<<<<<<< HEAD
print(">>> Super Calculator: Version B <<<")
=======
print("=== Team Calculator: Version A ===")
>>>>>>> main

```

* Open the file, discuss with Student A, and decide on a unified line (e.g., `print("=== Team Calculator 1.0 ===")`)
* Stage, commit, and push the resolution:

```bash
git add calculator.py
git commit -m "fix: resolve banner merge conflict"
git push origin fix/banner-b

```

5. **Final Review & Merge:**
* Student A verifies the resolved PR #4 on GitHub, approves it, and merges it.

