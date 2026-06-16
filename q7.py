
students = {"Aman", "Rohit", "Priya", "Neha", "Aman", "Rohit"}


print("Students Set:", students)


students.add("Karan")
students.add("Simran")

print("Updated Set:", students)


marks = {
    "Aman": 85,
    "Rohit": 70,
    "Priya": 55,
    "Neha": 92
}


for name, mark in marks.items():
    if mark >= 75:
        print(name, ":", mark, "- Distinction")
    elif mark >= 60:
        print(name, ":", mark, "- Pass")
    else:
        print(name, ":", mark, "- Fail")