import os

path = "./file.txt"
if os.path.exists(path):
    print("file exists")
    if os.path.isfile(path):  # os.path.isdir()->check it is a directory or not
        print("it is a file")
    else:
        print("it is not a file")
else:
    print("file does not exist")

try:
    with open(path) as file:
        print(file.read())
except Exception as e:
    print(e)
text = "Robin is the best"
with open(path, "w") as file:
    file.write(text)
try:
    with open(path) as file:
        print(file.read())
except Exception as e:
    print(e)
# "w"-> write , "a"-> append
