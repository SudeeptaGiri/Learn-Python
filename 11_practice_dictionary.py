phrase = "I love Batman because I am Batman"
# obj = {}
# for i in obj:
#     print("HEllo")


# def frequency_dict(phrase):
#     words = phrase.split(" ")
#     uniWords = set(words)
#     frequency = {}
#     for i in uniWords:
#         frequency[i] = 0
#     for word in words:
#         for key in frequency:
#             if (key == word):
#                 frequency[key] += 1
#     print(frequency)


# frequency_dict(phrase)

words = phrase.split(" ")
freq = {}
for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
