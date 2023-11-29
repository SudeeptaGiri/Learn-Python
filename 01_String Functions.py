###### Finding Substrings####
'''
find(substring)
find(substring,start,end)

rfind(substring) --> reverse searching 
rfind(substring,start,end)

index(substring)
index(substring,start,end)
//////// index method is same as find it give error when value not found but find return -1

rindex(substring)
rindex(substring,start,end)

count(substring) --> count the occurrences of substring in the string
count(substring,start,end)

Replacing a string with another string
---------------------------------------
s.replace("present in substring","youwant to replace") 
s.strip() --> starting and ending blank space is removed

Splitting
----------
list=s.split("separator")
s=separator.join(list)

changing case
-------------
upper() -> every letter will converted to upper case
lower() -> every letter will converted to lower case
swapcase() 
title() -> first letter of the every word will be upper case
capitalize() -> only first letter will be upper case


to check of characters present in the given string
---------------------------------------------------
1.isalnum() -> a to z , A to Z , 0 to 9
2.isalpha() -> a to z , A to Z 
3.isdigit() -> 0 to 9

checking starting and ending of the string 
-------------------------------------------
s.startswith(substring)
s.endswith(substring)

'''
s = "twinkle is as beautiful as Moon"
ans = s.capitalize()
print(ans)
