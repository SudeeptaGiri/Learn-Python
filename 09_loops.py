fruits = ["apple", "banana", "strawberry", "orange"]

for el in fruits:
    print(el)

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object
enFruits = enumerate(fruits)
# print(enFruits)

for i in enFruits:
    print(i)
    print(i[0], i[1])

# tuple unpacking
fruits = (1, "apple")
print(fruits)
index, fruits = (1, "apple")
print(fruits)


for i, item in enFruits:
    print(i)
    print(item)

### RANGE ####

# range() function returns as a subsequence of numbers, starting from 0 by default, and increments by 1 (by default) and steps before a specified number

for i in [1, 2, 3, 4, 5]:
    print(i)


for _ in range(5):
    print("haha")

for i in range(0, 100, 2):
    print(i)


# FOR ELSE
l1 = [2, 3, 4, 56, 7, 78, 8, 9]

for i in l1:
    print(i)
else:
    print("haha")

# -> it will if loop executed successfully (Without Break ) then the else will execute


# for loop in Dictionary
d = {
    "name": "Sudeepta",
    "age": 20,
    "cgpa": 9.8,
    "Anime": ["Onepiece", "Naruto", "Bleach"]
}
for i in d.items():
    print(i)
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
