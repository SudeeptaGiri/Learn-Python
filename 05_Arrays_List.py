# Lists are used to store multiple items in a single variable
fruits = ["apple", "banana", "strawberry"]

print(fruits)
fruits.append("blueberry")
print(fruits)

# INDEXING
print(fruits[1])

# Get the last item
print(fruits[-1])

# Length of the array
print(len(fruits))

# Slicing
print(fruits[0:2])
print(fruits[0:len(fruits)-1])

length = len(fruits)
print(fruits[0:length:2])
print(fruits[::-1])

arr = [1, 1.2, "hello", False]
print(arr)

# Methods-> append(),insert(ind,"el"),remove("el"),pop()->remove last,reverse(),clear(),index(),count(),sort(),
