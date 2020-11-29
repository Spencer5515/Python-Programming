# Lists & List Functions

friends = ["Stephanie", "Alex", "Jarod", "Allie", "Daniel"]  # list declaration / can have mixed dataTypes
nums = [23, 8, 15, 4, 56, 42]
temp1 = 1
temp2 = 4

print("=== Basic Lists ===")
print(friends)  # prints list

print("Elem at index " + str(temp1) + ": " + str(friends[temp1]))  # gets elem at given index
print("Elem in index range " + str(temp1) + " to " + str(temp2) + ": " + str(friends[temp1:temp2]))  # gets elem at given index

print("\n=== List Functions ===")
print(friends)  # prints list
print("Alex is at index: " + str(friends.index("Alex")))  # gets index of specific elem
print()

print("Numbers List: ")
print(nums)
print("\nSorting Nums...")
nums.sort()
print(nums)
print("\nReversing Nums...")
nums.reverse()
print(nums)

# friends.extend(nums)  # adds second list to main list
# friends.count("Alex")  # gets number of times Alex appears in list
print("\nAdding Marissa and Genna at index 2 and the end...")
friends.append("Marissa")  # appends elem to list
friends.insert(2, "Genna")  # inserts elem into list
print(friends)

print("\nRemoving Genna...")
friends.remove("Genna")  # removes elems
print(friends)

print("\nPopping Marissa off the list...")
friends.pop()  # pops last elem off list (like in a stack)
print(friends)

print("\nClearing list...")
friends.clear()
print(friends)





