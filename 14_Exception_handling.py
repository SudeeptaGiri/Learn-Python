try:
    num = int(input("enter a number You want ot divide "))
    div = int(input("enter a number to divide with "))
    res = num/div
    print(res)
except Exception as e:
    print(e)
    print("Something went wrong")
finally:
    print("Final Block")
