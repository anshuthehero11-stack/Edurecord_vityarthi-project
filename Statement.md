# Problem Statement

## Problem Statement
In many small classes and coaching groups, student details, the courses they take and their marks are still written in notebooks or scattered Excel sheets. Because of this it becomes slow to find one student's record, and it is easy to enrol a student in the same course twice or to miss which students have failed. Teachers need a very simple tool that keeps all of this in one place.

This project is a **Student Course & Grade Management System** made in Python. It runs in the console (command line) and lets the user add students, enrol them in courses, record grades, and quickly see who has failed.

## Scope of the Project
**What the project does:**
- Add a student with an ID and a name
- Enrol a student in a course (a student cannot be enrolled in the same course twice)
- Add a grade for a course the student is enrolled in
- Show all students who have failed (grade below 50) along with the course and marks
- Search a student by ID and show the name, courses and grades

**What the project does NOT do (out of scope):**
- No graphical interface, it is only a console menu
- No database or file saving. The data is stored in memory, so it is lost when the program is closed
- No login or user accounts
- No GPA / percentage calculation or report card printing

## Target Users
- Teachers or class coordinators who want to keep a small record of students and marks
- Students who want a simple example of how OOP (classes and inheritance), sets and dictionaries are used in Python

## High-Level Features
1. **Student management:** add a student and search a student by ID
2. **Course enrolment:** enrol a student in a course, duplicates are blocked
3. **Grade management:** add a grade only if the student is enrolled in that course
4. **Failed students report:** lists every course where the grade is below 50
5. **Menu-driven interface:** simple numbered menu that keeps running until the user chooses Exit
6. **Basic messages for wrong input:** shows messages like "no student found", "already enrolled" and "wrong input try again"
