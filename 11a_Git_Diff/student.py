def add_student(name):
    print("Student:", name)

def calculate_average(marks):
    return sum(marks) / len(marks)

add_student("Arun")
print("Average:", calculate_average([80, 90, 85]))
