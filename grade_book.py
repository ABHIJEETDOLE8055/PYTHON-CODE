#grade_book.py
#1
def add_course(courses,course_name):
    courses[course_name]=[]
   
#2
def add_grade(courses,course_name,grade):
    if course_name in courses:
        courses[course_name].append(grade)
    else:
        print("Course not found.")

#3
def calculate_overall_grade(courses,course_name):
    if course_name in courses:
        grades=courses[course_name]
        overall_grade=sum(grades)/len(grades)
        return overall_grade
    else:
        print("Course not found.")
        return None

#4
def view_grades(courses,course_name):
    if course_name in courses:
        grades=courses[course_name]
        print(f"Grades for {course_name}: {grades}")
    else:
        print("Course not found")

#5
def view_average_grade(courses,course_name):
    if course_name in courses:
        overall_grade=calculate_overall_grade(courses,course_name)
        if overall_grade is not None:
            print(f"Average grade for {course_name}: {overall_grade:.2f}")
    else:
        print("Course not found.")