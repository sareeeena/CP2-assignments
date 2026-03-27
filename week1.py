student1 = {
    "name": "Eshmat",
    "id": "2024001",
    "grades": [85, 90, 78]
}

student2 = {
    "name": "Toshmat",
    "id": "2024002",
    "grades": [92, 88, 95]
}

def calculate_average(student):
    return sum(student["grades"]) / len(student["grades"])

def display_student(student):
    avg = calculate_average(student)
    print(f"Student: {student['name']}, ID: {student['id']}, Average: {avg}")

display_student(student1)
display_student(student2)