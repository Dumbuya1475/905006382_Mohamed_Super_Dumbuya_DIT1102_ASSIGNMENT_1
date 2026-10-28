# PROG211: Object-Oriented Programming 1
# Student Learning and Results Management System

class Course:
    def __init__(self, course_code, course_name, lecturer):
        self.course_code = course_code
        self.course_name = course_name
        self.lecturer = lecturer

    def display_course(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Lecturer: {self.lecturer}")


class Student:
    student_count = 0

    def __init__(self, student_id, name, program, course):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.course = course
        Student.student_count += 1

    # Instance method
    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Program: {self.program}")
        print(f"Course: {self.course.course_name}")
        print(f"Course Code: {self.course.course_code}")

    # Instance method
    def update_program(self, new_program):
        self.program = new_program

    # Class method
    @classmethod
    def create_student(cls, student_id, name, program, course):
        return cls(student_id, name, program, course)

    # Static method
    @staticmethod
    def validate_student_id(student_id):
        return student_id.startswith("ST") and len(student_id) == 5


# Create Course objects
course1 = Course(
    "DIT1102",
    "Web Design and Development",
    "Mr. Amkam"
)

course2 = Course(
    "PROG211",
    "Object-Oriented Programming 1",
    "Mr. Julius Laggah"
)


# Create Student objects
student1 = Student(
    "ST001",
    "Mohamed Dumbuya",
    "Diploma in Information Technology",
    course1
)

student2 = Student(
    "ST002",
    "Abdulai Kamara",
    "Diploma in Information Technology",
    course2
)

# Create another student using the class method
student3 = Student.create_student(
    "ST003",
    "Fatmata Sesay",
    "Diploma in Information Technology",
    course1
)


# One data structure: a list
students = []

# Add students to the list
students.append(student1)
students.append(student2)
students.append(student3)


# Function to add a student to the list
def add_student(student):
    students.append(student)
    print("Student added successfully.")


# Function to display all students
def display_students():
    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print("---------------------------")
        student.display_info()


# Demonstrate object interaction
print("===== COURSE INFORMATION =====")
course1.display_course()

print("\n===== STUDENT INFORMATION =====")
student1.display_info()

# Update a student's program
print("\n===== UPDATING STUDENT RECORD =====")
student1.update_program("Diploma in Software Engineering")
print("Updated program:")
student1.display_info()


# Demonstrate static method
print("\n===== STUDENT ID VALIDATION =====")

valid_id = Student.validate_student_id("ST001")
invalid_id = Student.validate_student_id("ABC12")

print("ST001 valid:", valid_id)
print("ABC12 valid:", invalid_id)


# Display all records stored in the list
display_students()


# Demonstrate class variable
print("\n===== TOTAL STUDENTS =====")
print("Total students:", Student.student_count)