import os


file = open("employees.txt", "w")
file.write("Aman - 30000\n")
file.write("Rohit - 35000\n")
file.write("Priya - 40000\n")
file.write("Neha - 45000\n")
file.write("Karan - 50000\n")
file.close()


print("Initial Employee Records:")
file = open("employees.txt", "r")
print(file.read())
file.close()


file = open("employees.txt", "a")
file.write("Simran - 55000\n")
file.write("Ankit - 60000\n")
file.close()


print("Updated Employee Records:")
file = open("employees.txt", "r")
print(file.read())
file.close()


if os.path.exists("employees.txt"):
    print("File exists.")
else:
    print("File does not exist.")


os.remove("employees.txt")
print("File deleted successfully.")