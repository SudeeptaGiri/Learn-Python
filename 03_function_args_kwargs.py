##### ARGS#########
# parameters that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*num):
    sum = 0
    for i in num:
        sum += i
    return sum


ans = add(1, 2, 3, 41)
print(ans)


########## KWARGS #########
# parametes that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of arguments

def hello(**name):
    pass
