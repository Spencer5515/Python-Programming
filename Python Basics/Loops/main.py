# While Loops
print("=== While Loops ===\n")

i = 0

while i < 10:  # while loop declaration
    print(i + 1)
    i += 1

print("*Done with While loop*")

# for loops
print("\n=== For Loops ===\n")

friends = ["Stephanie", "Alex", "Jarod"]

print("---")
for j in friends:  # for loop (similar to C++/Java for-each loop)
    print(j)

print("---")
for index in range(10):  # prints all numbers between 0 & 10 non-inclusive
    print(index)

print("---")
for indexx in range(len(friends)):  # same as above but uses len() instead of int
    print(friends[indexx])  # prints elem at given index

print("---")
print("*Done with for loops*")
