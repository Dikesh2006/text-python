import json


students = [
    {
        "name": "Aman",
        "age": 20,
        "city": "Bhopal",
        "course": "B.Tech",
        "marks": 85
    },
    {
        "name": "Rohit",
        "age": 21,
        "city": "Indore",
        "course": "BCA",
        "marks": 65
    },
    {
        "name": "Priya",
        "age": 19,
        "city": "Delhi",
        "course": "B.Sc",
        "marks": 78
    },
    {
        "name": "Neha",
        "age": 22,
        "city": "Mumbai",
        "course": "B.Com",
        "marks": 90
    }
]


with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Data saved successfully!")


with open("students.json", "r") as file:
    data = json.load(file)

print("\nStudents with marks > 70:")
for student in data:
    if student["marks"] > 70:
        print(student["name"], "-", student["marks"])

print("\nTotal Students:", len(data))