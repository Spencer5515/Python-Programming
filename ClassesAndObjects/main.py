from Student import Student  # from Student.py import Student class

# Classes and Objects (OOP Finally)
print("=== Classes and Objects ===\n")

student1 = Student("Spencer", "Computer Science", 3.64, False)  # creates Student Object
student2 = Student("Stephanie", "Communications", 3.8, False)

print("Student1's Name: " + student1.name)  # prints student1's attributes
print("Student1's Major: " + student1.major)
print("Student1's GPA: " + str(student1.gpa))
print("Student1's Probation: " + str(student1.is_on_probation))
print()

print("Student2's Name: " + student2.name)  # prints student2's attributes
print("Student2's Major: " + student2.major)
print("Student2's GPA: " + str(student2.gpa))
print("Student2's Probation: " + str(student2.is_on_probation))
print()

print(student1.is_on_honorRoll())  # calls non-initializer function
print(student2.is_on_honorRoll())
