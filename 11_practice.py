# arr = [1, 2, 3, 4]
# print(len(arr))


# def double(arr):
#     for i in range(len(arr)):
#         arr[i] = 2*arr[i]


# print(arr)
# double(arr)
# print(arr)

# Counr Words
# split() method splits a string into a list
# You can specify the separator,default separator is any whitespace


# phrase = "I will be the King of the Pirate"


# def count_wors(phrse):
#     words = phrse.split(' ')
#     return len(words)


# print(count_wors(phrase))

arr = [2, 1, 4, 1, 0, 0, 7, 0, 2, 3]


# def sum_list(arr):
#     sum = 0
#     # for i in range(len(arr)):
#     #     sum += arr[i]
#     # return sum
#     for num in arr:
#         sum += num
#     return sum


# print(sum_list(arr))

def find_max(arr):
    max = arr[0]
    for num in arr:
        if (num > max):
            max = num
    return max


print(find_max(arr))
