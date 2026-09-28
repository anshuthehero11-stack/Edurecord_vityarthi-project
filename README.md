# Student Course & Grade Management System

## Overview
This is a small console-based Python project made for the VITyarthi *Build Your Own Project* evaluation. It helps to manage students, the courses they are enrolled in and their grades. The user works through a simple numbered menu. The project uses Python classes, inheritance, sets and dictionaries.

The data is kept in memory only, so it is cleared when the program is closed.

## Features
- Add a new student (ID + name)
- Enrol a student in a course (duplicate enrolment is not allowed)
- Add a grade for a course (only if the student is enrolled in it)
- Show all failed students (grade below 50)
- Search a student by ID and see their courses and grades
- Menu keeps running until the user selects Exit
- Messages for common mistakes (student not found, already enrolled, not enrolled in course, wrong menu option)

## Technologies / Tools Used
- Python 3
- Concepts used: classes and inheritance, `set`, `dict`, `while` loop, `if/elif`, `input()` and `print()`
- Git and GitHub for version control
- VS Code / IDLE (any editor works)

## Project Structure
```
.
├── VITYARTHI_Project.py   # main program (classes + menu)
├── README.md
└── statement.md
```

## Steps to Install & Run
1. Install Python 3 from https://www.python.org/downloads/ (no extra libraries are needed).
2. Clone or download this repository:
   ```
   git clone <your-repo-link>
   cd <your-repo-folder>
   ```
3. Run the program:
   ```
   python VITYARTHI_Project.py
   ```
   (On some systems use `python3 VITYARTHI_Project.py`)
4. Type the number of the option you want and press Enter.

## How to Use
| Option | What it does |
|--------|--------------|
| 1 | Add student. Asks for student id and name |
| 2 | Enroll course. Asks for student id and course name |
| 3 | Add grade. Asks for student id, course name and grade |
| 4 | Show failed students (grade below 50) |
| 5 | Search student by id. Shows name, courses and grades |
| 6 | Exit |

## Instructions for Testing
Testing is done manually by running the program and checking the output. Some cases to try:

| # | What to do | Expected output |
|---|-----------|-----------------|
| 1 | Option 1 with id `101`, name `Rahul` | `student added` |
| 2 | Option 2 for `101`, course `Maths` | `course enrolled` |
| 3 | Option 2 for `101`, course `Maths` again | `already enrolled` |
| 4 | Option 2 with an id that was never added | `no student found` |
| 5 | Option 3 for `101` with a course he is not enrolled in | `not enrolled in course` |
| 6 | Option 3 for `101`, `Maths`, grade `72` | `grade saved` |
| 7 | Grade `38` for a course, then option 4 | student is listed as failed |
| 8 | Grade exactly `50`, then option 4 | student is NOT listed (50 is a pass) |
| 9 | Option 4 when nobody failed | `no failed students` |
| 10 | Option 5 with a valid id | name, courses and grades are shown |
| 11 | Option 5 with a wrong id | `no student found` |
| 12 | Type `9` in the menu | `wrong input try again` |

## Sample Run
```
type 1 2 3 4 5 or 6 1
student id 101
student name Rahul
student added
type 1 2 3 4 5 or 6 2
student id 101
course name Maths
course enrolled
type 1 2 3 4 5 or 6 3
student id 101
course name Maths
grade 72
grade saved
type 1 2 3 4 5 or 6 5
student id to search 101
name Rahul
course Maths grade 72.0
```
*(The menu is printed every time before "type 1 2 3 4 5 or 6". It is left out here to save space.)*

## Screenshots
_Code and Output Screenshot:_
```
![image alt](https://github.com/anshuthehero11-stack/Edurecord_vityarthi-project/blob/dcf36a04c6387546622bb36d64e2a1c6b187b5dd/CODE1.png)

```


## Author
Name: `Shivansh Pandey`  
Reg. No.: `26BCE11235`
