# Student Learning and Results Management System

## PROG211 – Object-Oriented Programming 1

**Institution:** Limkokwing University of Creative Technology – Sierra Leone
**Department:** Information and Communication Technology
**Semester:** 03
**Assignment:** Real-World Solutions under DPG Standards
**Domain:** Education

---

## 1. Project Overview

The Student Learning and Results Management System is a simple Python program developed using Object-Oriented Programming (OOP) concepts.

The purpose of the system is to demonstrate how OOP can be used to manage basic student and course information in an educational environment.

The program allows users to:

* Create student records.
* Create course records.
* Associate students with courses.
* Update student information.
* Store multiple student objects in a list.
* Display student records.
* Validate student IDs.

---

## 2. Problem Statement

Educational institutions need effective ways to manage student and course information.

When records are handled manually, updating and displaying information can become difficult.

This project provides a simple programming-based solution for managing basic student and course information.

The system is designed as an educational demonstration rather than a complete production management system.

---

## 3. Objectives

The main objectives are to:

1. Demonstrate the use of Python classes and objects.
2. Demonstrate attributes and methods.
3. Use a Python list to store multiple objects.
4. Demonstrate instance methods.
5. Demonstrate class methods.
6. Demonstrate static methods.
7. Demonstrate interaction between objects.
8. Apply Digital Public Goods principles.

---

## 4. OOP Concepts Used

### Classes

The project contains two main classes:

* `Student`
* `Course`

### Objects

Objects are created from these classes.

Example:

```python
student1 = Student(
    "ST001",
    "Mohamed Dumbuya",
    "Diploma in Information Technology",
    course1
)
```

### Attributes

The Student class contains:

* `student_id`
* `name`
* `program`
* `course`

The Course class contains:

* `course_code`
* `course_name`
* `lecturer`

### Instance Methods

Examples include:

```python
display_info()
update_program()
display_course()
```

### Class Method

The project includes:

```python
create_student()
```

It creates a Student object using the class.

### Static Method

The project includes:

```python
validate_student_id()
```

It validates the format of a student ID.

---

## 5. Data Structure

The project uses one main Python data structure: a **list**.

```python
students = []
```

Student objects are added to the list using:

```python
students.append(student1)
```

The records are displayed using a loop.

---

## 6. Digital Public Goods Alignment

### Open Source

The source code is publicly available on GitHub so that others can inspect, learn from, and reuse the project.

### Inclusive and Accessible

The program uses a simple command-line interface and does not require expensive equipment or advanced computer resources.

### Privacy Respecting

The system avoids storing sensitive personal information.

Only basic sample information such as student ID, name, program, and course is used.

### Modular and Reusable

The project is divided into classes and methods.

The Student and Course classes can be reused and extended for other educational applications.

---

## 7. Technologies Used

* Python 3
* Object-Oriented Programming
* Python List
* GitHub

No external libraries are required.

---

## 8. How to Run the Program

### Step 1

Install Python 3 on your computer.

### Step 2

Clone or download this repository.

### Step 3

Open the project folder in a terminal.

### Step 4

Run:

```bash
python student_portal.py
```

The program will display course information, student information, ID validation, student records, and the total number of students.

---

## 9. Sample Output

```text
===== COURSE INFORMATION =====
Course Code: DIT1102
Course Name: Web Design and Development
Lecturer: Mr. Amkam

===== STUDENT INFORMATION =====
Student ID: ST001
Name: Mohamed Dumbuya
Program: Diploma in Information Technology
Course: Web Design and Development
Course Code: DIT1102

===== STUDENT ID VALIDATION =====
ST001 valid: True
ABC12 valid: False

===== STUDENT RECORDS =====
---------------------------
Student ID: ST001
Name: Mohamed Dumbuya
Program: Diploma in Software Engineering
Course: Web Design and Development
Course Code: DIT1102

===== TOTAL STUDENTS =====
Total students: 3
```

---

## 10. Future Improvements

The system could be expanded in the future to include:

* Student results and grades.
* Attendance management.
* Multiple course registration.
* A graphical user interface.
* Database storage.
* User authentication.
* Exporting reports.

These features are outside the scope of this introductory OOP assignment.

---

## 11. Conclusion

The Student Learning and Results Management System demonstrates how Object-Oriented Programming can be applied to a real-world educational problem.

The project demonstrates classes, objects, attributes, instance methods, class methods, static methods, object interaction, and the use of a Python list.

The project also follows the required Digital Public Goods principles by being open-source, accessible, privacy-conscious, modular, and reusable.
