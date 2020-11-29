# Try / Except

try:
    # value = 10 / 0
    num = int(input("Enter a number: "))
    print("You Entered: " + str(num))
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("ERROR: Invalid Input")
