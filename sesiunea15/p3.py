import json

class Students:
    id = None
    fname = None
    lName = None
    age = 0
    grade = 0

    def __init__(self, id, fname, lname, age, grade):
        self.id = id
        self.fname = fname
        self.lName = lname
        self.age = age
        self.grade = grade

with open("documents/students.json") as students_json:
    student_data = json.load(students_json)
    students_list = []
    for student_data in student_data:
        student = Students(student_data['id'], student_data['fname'], student_data['lname'], student_data['age'], student_data['grade'])
        students_list.append(student)

        print(students_list)

