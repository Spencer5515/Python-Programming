# Reading Files
print("=== Reading Files ===\n")

# works because txt file is in same directory
employee_file = open("employees.txt", "r")  # "r" -> read / "w" -> write / "a" -> append
print(employee_file.readable())  # bool of if can read file

# sequentially reads/prints every line in file
for employee in employee_file.readlines():
    print(employee)

# print(employee_file.readline())  # reads single line in file
# print(employee_file.readlines()[1])  # puts all lines of file into list / or just line index

# print(employee_file.read())  # reads / prints entire file

# Writing Files
print("\n=== Writing Files ===\n")

employee_file = open("employees.txt", "a")

print("Adding Employee(s) to File...")
employee_file.write("\nToby -> Human Resources")  # writes to file
employee_file.write("\nKelly -> Customer Service")

employee_file.close()  # closes file
