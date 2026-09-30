students = [
    {"id": "101", "name": "Arun", "department": "CSE"},
    {"id": "102", "name": "Priya", "department": "ECE"},
    {"id": "103", "name": "Rahul", "department": "CSE"}
]

def search_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

result = search_student("102")
print("Student Found:" if result else "Student not found.")
if result:
    print(result)
