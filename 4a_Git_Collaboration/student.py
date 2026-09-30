students = []

def add_student(student_id, name, department):
    students.append({
        "id": student_id,
        "name": name,
        "department": department
    })
    print("Student added successfully.")

def display_students():
    print("\nStudent Details")
    for student in students:
        print(student)

def search_student(student_id):
    for student in students:
        if student["id"] == student_id:
            print("Student Found:", student)
            return student
    print("Student not found.")
    return None

add_student("101", "Arun", "CSE")
add_student("102", "Priya", "ECE")
display_students()
search_student("101")
