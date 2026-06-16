# Q4. Create a Student Registration System: (5 Marks) • Create your own exception: InvalidAgeError • Create your own exception: InvalidMarksError • Ask user to enter: name, age, marks • If age < 15 or age > 30 → raise InvalidAgeError • If marks < 0 or marks > 100 → raise InvalidMarksError • If valid → print 'Student registered successfully!'



class InvalidAgeError(Exception):
    pass


class InvalidMarksError(Exception):
    pass

try:
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    if age < 15 or age > 30:
        raise InvalidAgeError("Invalid Age! Age must be between 15 and 30.")

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Invalid Marks! Marks must be between 0 and 100.")

    print("Student registered successfully!")

except InvalidAgeError as e:
    print(e)

except InvalidMarksError as e:
    print(e)

except ValueError:
    print("Please enter valid numeric values.")

finally:
    print("Registration process completed.")