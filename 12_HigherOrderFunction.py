######### MAP ##########
######## FILTER ########
# map() is a function that takes another function and returns
# 1st parameter-> function->do what you want to
# 2nd parameter-> arrat

def double(number):
    print(number*2)


ans = list(map(double, [1, 2, 3, 4]))
print(ans)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def even(num):
    return (num*2) == 10


result = list(filter(even, numbers))
print(result)

# List comprehension
# Fuck List comprehension
