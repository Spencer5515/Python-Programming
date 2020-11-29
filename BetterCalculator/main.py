# Better Calculator
print("=== Calculator ===\n")

num1 = float(input("Enter the first number: "))  # converts user I/O to float
op = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    temp = num1 + num2
    print("Answer = " + str(temp))
elif op == "-":
    temp = num1 - num2
    print("Answer = " + str(temp))
elif op == "/":
    temp = num1 / num2
    print("Answer = " + str(temp))
elif op == "*":
    temp = num1 * num2
    print("Answer = " + str(temp))
elif op == "%":
    temp = num1 % num2
    print("Answer = " + str(temp))
else:
    print("ERROR: Invalid Operator")

