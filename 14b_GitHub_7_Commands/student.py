students = []

def add_student(student_id, name):
    students.append({"id": student_id, "name": name})

def display_students():
    for student in students:
        print(student)

add_student(101, "Arun")
display_students()
