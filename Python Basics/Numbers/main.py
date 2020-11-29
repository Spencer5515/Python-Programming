# Arithmetic and Numerical functions
from math import*  # importing Python math functions

temp1 = 3 * 4 + 5
temp2 = 10 % 3
temp3 = -2
temp4 = 3
temp5 = 3.589452
temp6 = 36

print("Printing Numbers...")
print("Int: \t\t\t\t" + str(2))  # prints numbers
print("Negative Int:     \t" + str(-34.5))
print("Floating Point: \t" + str(2.0987))

print("\nArithmetics...")
print("3 * 4 + 5 = " + str(temp1))
print("10 % 3 = " + str(temp2))

print("2^" + str(temp4) + " = " + str(pow(2, temp4)))  # power function
print("SQRT of " + str(temp6) + " = " + str(sqrt(36)))  # sqrt function
print("Absolute Value of " + str(temp3) + " = " + str(abs(temp3)))  # absolute value function
print("Largest of " + str(temp3) + " & " + str(temp4) + " = " + str(max(temp3, temp4)))  # max function
print("Round function: round(" + str(temp5) + ") --> " + str(round(temp5)))  # rounding function

print("Floor of " + str(temp5) + " = " + str(floor(temp5)))  # gets numerical floor
print("Ceiling of " + str(temp5) + " = " + str(ceil(temp5)))  # gets numerical ceiling
