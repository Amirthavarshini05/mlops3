students = []

def add_student(student_id, name):
    students.append({"id": student_id, "name": name})

def display_students():
    for student in students:
        print(student)

def search_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

add_student(101, "Arun")
add_student(102, "Priya")
display_students()
print(search_student(101))
