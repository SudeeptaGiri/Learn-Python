# ()
# Immutable -> at a particular index you cant change the Entity
# Similar as LIST (Mutable)
# duplicates are alllowed
# heterogenous entities are allowed
# hashable

numbers = (1, 2, 3, 4, 5, "Sudd", True, 5.6)
print(numbers)
print(type(numbers))
print(numbers[5])
# It doesn't support Item Assignment(Basically IMMUTABLE)

l = list(numbers)  # -> It convert tuples to list


# .count(val)->how manny time that val avilable // Same as List
# .index(val)->where that val is avilable - return the index of the first occurrence
# .max(numbers), .min(numbers) -> same as list
