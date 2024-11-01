from MyClass import Person, Student, Course
students = []
courses = []

def menu():
    print(""" ==== Student Management System ====
            1. Add New Student
            2. Add New Course
            3. Enroll Student in Course
            4. Add Grade for Student
            5. Display Student Details
            6. Display Course Details
            7. Save Data to File
            8. Load Data from File
            0. Exit
         """)
#menu()

def choice():
    loopcontrol = True
    while loopcontrol:
        try:
            menu()
            print("Input:")
            userchoice = int(input("Select Option: "))
            if 0 <= userchoice <= 8:
                if userchoice == 1:
                    name = input("Enter Name: ")
                    age = int(input("Enter Age: "))
                    address = input("Enter Address: ")
                    id = input("Enter Student ID: ")
                    objStudent = Student(id, name, age, address)
                    students.append(objStudent)

                    print("Output:")
                    print("Student", objStudent.name,"(ID:", objStudent.student_id, ")","added successfully.")
                    #objStudent.display_person_info()
                    
                
                elif userchoice == 2:
                    course_name = input("Enter Course Name: ")
                    course_code = input("Enter Course Code: ")
                    instructor = input("Enter Instructor Name: ")
                    objCourse = Course(course_name, course_code, instructor)
                    courses.append(objCourse)
                    
                    print("Output:")
                    print("Course", objCourse.course_name, "(Code:", objCourse.course_code,")", "created with instructor", objCourse.instructor)

                elif userchoice == 3:
                    if students == []:
                        print("Student list is empty. please enter student")
                        continue
                    id = input("Enter Student ID: ")
                    for i in students:
                        if id == i.student_id:
                            course_code = input("Enter Course Code: ")
                            for j in courses:
                                if course_code == j.course_code:
                                    j.add_student(i) #parameter problem
                                    i.enroll_course(j)
                                    print("Output:")
                                    print("Student", i.name, "(ID:", i.student_id, ") enrolled in", j.course_name, "(Code:", j.course_code,").")
                                else:
                                    print("No Such course available")
                                    continue
                        else:
                            print("No Student ID Exist")
                            continue

                
                elif userchoice == 4:
                    if students == []:
                        print("Student list is empty. please enter student")
                        continue
                    id = input("Enter Student ID: ")
                    for i in students:
                        if id == i.student_id:
                            course_code = input("Enter Course Code: ")
                            for j in courses:
                                if course_code == j.course_code:
                                    grade = input("Enter Grade: ")
                                    i.add_grade(course_code, grade)
                                    print("Output:")
                                    print("Grade", grade, "added for", i.name, "in", j.course_name, ".")
                                else:
                                    print("No Course Code Exist. Please try again.")
                                    continue
                        else:
                            print("No Student ID Exist")
                            continue

                elif userchoice == 5:
                    if students == []:
                        print("No such student exist. please enter student")
                        continue
                    id = input("Enter Student ID: ")
                    print("Output:")
                    for i in students:
                        if id == i.student_id:
                            i.display_student_info()
                        else:
                            print("No Such Student Exist")

                elif userchoice == 6:
                    course_code = input("Enter Course Code: ")
                    for i in courses:
                        if course_code == i.course_code:
                            print("Output:")
                            i.display_course_info()
                        else:
                            print("No such course exist")
                            continue

                elif userchoice == 7:
                    pass
                elif userchoice == 8:
                    pass
                
                elif userchoice == 0:
                    loopcontrol = False
                else:
                    pass

            else:
                print("Wrong Input! Please enter the number between 0 to 8")


        except Exception as e:
            print(e)

choice()