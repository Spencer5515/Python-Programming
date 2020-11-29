# If Statements
print("=== If Statements ===\n")

is_male = True
is_tall = False

if is_male and is_tall:  # if (also works with 'or')
    print("You are male and tall")
elif is_male and not(is_tall):  # else if / and !
    print("You are a short male")
elif not(is_male) and is_tall:  # else if / and !
    print("You are not male but tall")
else:  # else
    print("You are neither male nor tall")

# Advanced If Statements
print("\n=== If Statements && Comparisons ===\n")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


temp = str(max_num(23, 34, 15))
print("Max Number of 23, 34, and 15 = " + temp)

