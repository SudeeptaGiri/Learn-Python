# Theory
# + plus - minus * multiplicative ** power & modulus
# 123/10 = 12.3  123//10=12

bill = float(input("Bill : "))
tip = float(input("Tip : "))
tip_amount = bill*(tip/100)
total_amount = bill+tip_amount
print("Total amount = $", total_amount)  # it is not concatination
num = int(input("Number of Friends : "))
each_friend = total_amount/num
# it is concatination, String only concatinate with String
print("per head = $"+str(each_friend))
print("\n")  # New line
print("\n\n\n")  # Multiple Newlines

# F-String

print(f"per head = ${each_friend}")

# This way of formating you use embedded python expressions inside string concats
