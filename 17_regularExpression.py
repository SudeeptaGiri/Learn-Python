######### REGULAR EXPRESSIONS #############


# if we wat to represent a group of string according to a particula format/pattern we should go for RE
# RE is a declaration mechanism to represent a group of string according to a particular format or pattern

# phone number => [6-9][0-9]{9} first digit -> 6-9, second digt[0-9] then repeat this(2nd digit[0-9]) pattern 9 time

####### Applications #########
# -> pattern matching appication
# -> validation framework
# -> to develop compiler
# -> to develop communication protocols

# Module name --> re
import re
'''
target string -> abaababba
search patern -> ab


# compiling string into pattern object
pattern = re.compile("ab")
# return iterator to find pattern in target string
matcher = pattern.finditer("abaababba")
count = 0
for match in matcher:
    print(match.start(), "...", match.end(), "...",
          match.group())  # start index of the match
    count += 1
print("Number of occurrences is ", count)
'''

'''
search for any alphabet Symbol 
# compiling string into pattern object
pattern = re.compile("[a-zA-Z0-9]")
# return iterator to find pattern in target string
matcher = pattern.finditer("ab7@ck9za")

# matcher = re.finditer("ab","ababbabbabba")

count = 0
for match in matcher:
    print(match.start(), "...", match.end(), "...",
          match.group())  # start index of the match
    count += 1
print("Number of occurrences is ", count)
'''

'''
character classes
------------------
[abc] -> a or b or c
[^abc] -> except (a or b or c)
[a-z] -> any lowercase alphabet symbol // [b-m]
[A-Z] -> any uppercase alphabet symbol // [D-F]
[a-zA-Z] -> any alphabet symbol both lowercase and uppercase
[0-9] -> Any digit
[0-9a-zA-Z] -> anyAlphaNumneric character 
[^0-9a-zA-Z] ->Except anyAlphaNumneric character -> special characters
 

prefefined charcterclases
--------------------------
\d -> any digit
\D -> accept any digit
\w -> any word any alpha numeric characer
\W -> except alpha numeric characer -> special characters
\s -> accept any space character
\S -> except any space character 
. -> accept any character including special

Quantifiers
------------
we can use quantifiers to specify the number of occurences to match

a-> exactly one 'a'
a+ -> atleat one 'a' -> a,aa,aaa,aaaa,aaaaaa,aaaaaa...
a* -> any number of 'a' -> e,a,aa,aaa,aaaa,aaaa,....
a? -> Atmost one 'a' -> a,e
a{m}-> exactly m number of 'a'
a{m,n}-> minimum m number of 'a' and maximum n number of 'a'

^ Symbol
---------
^ ==> StratsWith
^ab != [^ab]

$ symbol
-----------
& ==> EnndsWith
ab$



'''
# compiling string into pattern object
pattern = re.compile("a*")
# return iterator to find pattern in target string
matcher = pattern.finditer("abaabaaab")

# matcher = re.finditer("ab","ababbabbabba")

count = 0
for match in matcher:
    print(match.start(), "...", match.end(), "...",
          match.group())  # start index of the match
    count += 1
print("Number of occurrences is ", count)

'''
Impoertant function of re Module
-----------------------------------

1.match() -> to check the given pattern is in the start of the target string or not , if match is avilable then we get a match object otherwise none
m=re.match("paatern","targe-String")
if m is not None:
    print(m.group())//m.strt(),m.end()


2.fullmatch()-> to check wheather the given pattern matched with target string or not , if match is avilable then we get a match object otherwise none
m=re.fullmatch("paatern","targe-String")
if m is not None:
    print(m.group())//m.strt(),m.end()

3.search() ->  to check the given pattern present in the target string or not , if match is avilable then we get a match object of the first occurence otherwise none

4.findall() -> to find all occurrences of the match return list object

5.finditer() -> to find all occurrences of the match return
iterator object

6.sub() -> substitute or Replacement
matcher = re.sub(pattern,replacement,target )

7.subn() -> it is exactly same as sub() except thar it can also returns the number of replacements amd returns tuple
t = re.sub(pattern,replacement,target )
t[0]-> the replacemnet string
t[1]-> number of replacements

8.split()->split target string accordding to the paatern

9.compile()


'''
