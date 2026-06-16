try:
    filename = input("Enter filename: ")

    file = open(filename, "r")
    lines = file.readlines()

    if len(lines) == 0:
        print("File is empty!")
    else:
        print("Total number of lines in file:", len(lines))

    file.close()

except FileNotFoundError:
    print("File does not exist!")

finally:
    print("Operation complete!")
    