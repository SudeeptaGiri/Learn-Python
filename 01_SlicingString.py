'''
# Slcing a subsstring by extracting elements from another String
#        indexing[] or slice()
#        [start:end:step] -> strt included , end -> excluded , step -> increament by that many elements
name = "Ichigo Kuroshaki"
print(name[::-1])
print(name[1:8:-1])

website = "http://www.YouTube.com"

sl = slice(11, -4)
print(website[sl])
'''
s = "B-6,Lodhi Road, Delhi"
print(s[:-12]+s[-12:])
