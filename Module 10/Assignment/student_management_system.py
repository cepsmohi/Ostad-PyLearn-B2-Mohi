import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        self.display_person_info()
        print(f"Student ID: {self.student_id}")
        print("Courses:", ", ".join(self.courses))
        print("Grades:", self.grades)


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Course Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:", ", ".join([student.name for student in self.students]))


def main_menu():
    print("==== Student Management System ====")
    print("1. Add New Student")
    print("2. Add New Course")
    print("3. Enroll Student in Course")
    print("4. Add Grade for Student")
    print("5. Display Student Details")
    print("6. Display Course Details")
    print("7. Save Data to File")
    print("8. Load Data from File")
    print("0. Exit")

students = {}
courses = {}

def input_age():
    age = input("Enter Age: ")
    try:
        return int(age)
    except:
        print("Error: Not integer")
        input_age()

def add_student():
    name = input("Enter Name: ")
    age = input_age()
    address = input("Enter Address: ")
    student_id = input("Enter Student ID: ")
    student = Student(name, age, address, student_id)
    students[student_id] = student
    print(f"Student {name} (ID: {student_id}) added successfully.")

def add_course():
    course_name = input("Enter Course Name: ")
    course_code = input("Enter Course Code: ")
    instructor = input("Enter Instructor Name: ")
    course = Course(course_name, course_code, instructor)
    courses[course_code] = course
    print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

def enroll_student():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    if student_id in students and course_code in courses:
        student = students[student_id]
        course = courses[course_code]
        student.enroll_course(course.course_name)
        course.add_student(student)
        print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
    else:
        print("Invalid Student ID or Course Code.")

def add_grade():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")
    if student_id in students and course_code in courses:
        student = students[student_id]
        student.add_grade(course_code, grade)
        print(f"Grade {grade} added for {student.name} in {course_code}.")
    else:
        print("Invalid Student ID or Course Code.")

def display_student_details():
    student_id = input("Enter Student ID: ")
    student = students.get(student_id)
    if student:
        student.display_student_info()
    else:
        print("Student not found.")

def display_course_details():
    course_code = input("Enter Course Code: ")
    if course_code in courses:
        course = courses[course_code]
        course.display_course_info()
    else:
        print("Course not found.")

def load_data():
    global students, courses
    try:
        with open("data.json", 'r') as file:
            dicData = json.load(file)
            students = dicData['students']
            courses = dicData['courses']
            for sid, student_data in students.items():
                student = Student(
                    name=student_data['name'],
                    age=student_data['age'],
                    address=student_data['address'],
                    student_id=student_data['student_id']
                )
                student.grades = student_data['grades']
                student.courses = student_data['courses']
                students[sid] = student

            # Create Course Objects
            for cid, course_data in courses.items():
                course = Course(
                    course_name=course_data['course_name'],
                    course_code=course_data['course_code'],
                    instructor=course_data['instructor']
                )
                # Add students to the course
                for sid in course_data['students']:
                    student = students.get(sid)
                    if student:
                        course.add_student(student)
                courses[cid] = course
            print("Data loaded successfully.")
    except FileNotFoundError:
        print("The file was not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    return [], []

def student_to_dict(student):
    return {
        "name": student.name,
        "age": student.age,
        "address": student.address,
        "student_id": student.student_id,
        "grades": student.grades,
        "courses": student.courses
    }

def course_to_dict(course):
    return {
        "course_name": course.course_name,
        "course_code": course.course_code,
        "instructor": course.instructor,
        "students": [student.student_id for student in course.students]
    }

def save_data():
    students_dict = {sid: student_to_dict(student) for sid, student in students.items()}
    courses_dict = {cid: course_to_dict(course) for cid, course in courses.items()}

    dicData = {
        "students": students_dict,
        "courses": courses_dict
    }
    with open("data.json", "w") as file:
        json.dump(dicData, file, indent=4)
    print("All student and course data saved successfully.")

def exit_program():
    print("Exiting Student Management System. Goodbye!")
    exit()

def execute_choice(choice):
    choices = {
        1: add_student,
        2: add_course,
        3: enroll_student,
        4: add_grade,
        5: display_student_details,
        6: display_course_details,
        7: save_data,
        8: load_data,
        0: exit_program
    }
    action = choices.get(choice)
    if action:
        action()
    else:
        print("Invalid option. Please try again.")

while True:
    main_menu()
    choice = input("Select Option: ")
    try:
        choice = int(choice)
    except:
        print("Error: Not integer")
        main_menu()
    execute_choice(choice)
