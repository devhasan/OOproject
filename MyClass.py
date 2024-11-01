"""
-Student Management System by Hasan Mahmud
-Ostad Full Stack Web Development with Python, Django and React
-Assignment Covering Object Oriented Programming
"""
#Section A: Class Design and Implementation
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_person_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)

class Student(Person):
    def __init__(self, id, name, age, address):
        super().__init__(name, age, address)
        self.student_id = id
        self.grades = {}
        self.courses = []
    
    def add_grade(self, subject, grades):
        self.grades[subject] = grades
    
    def enroll_course(self, course):
        self.courses.append(course)
    
    def display_student_info(self):
        print("Student Information:")
        print("Name: ", self.name)
        print("ID: ", self.student_id)
        print("Age: ", self.age)
        print("Address: ", self.address)
        print("Enrolled Courses: ", self.courses)
        for i in self.courses:
            i.display_course_info()
        print("Grades: ", self.grades)

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []
    
    def add_student(self, student):
         self.students.append(student)

    def display_course_info(self):
        print("Course Information:")
        print("Course Name:", self.course_name)
        print("Code:", self.course_code)
        print("Instructor:", self.instructor)
        print("Enrolled Students:", self.students)
    
# objCourse = Course("Physics","PHY101","Rabbil")
# objCourse.add_student("Hasan")
# objCourse.display_course_info()