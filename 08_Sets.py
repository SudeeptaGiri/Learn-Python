# set = collection which is unordered and unindexed. NO DUPLICATES
# s = {} -> Dictionary
s1 = {"Sudd", "World", 1, 2, 34, 5, 1, "Sudd", 23, 34, 12}
print(s1)  # -> unique data //

lang1 = ["Java", "c++", "python"]
lang2 = ["ruby", "python", "Java", "php"]
# No Duplicates
# Sets -> Getting Unique stuffs
# stuffs = {2,3,4,5}  // 2 in stuffs -> true  // 6 in stuffs -> false
lang = set(lang1 + lang2)

print(lang)
print("php" in lang)
# print(set(lang))


def unique(list1, list2):
    '''
    list1 + list2 -> Add List and become one lIst
    set(list) -> convert list to set
    '''
    return set(list1+list2)


ans = unique(lang1, lang2)
print(ans)

trying = {1, 2, 4, 56, 6}
print(type(trying))
print(trying)
# NO INDEXING in SET
# trying.add(12) -> wont add duplicates,lists ( but can add Tuples )
# trying.remove(2) -> remove element if a member else error
# trying.discard(7)-> remove element if a member else no error
# trying.clear() -> will remove all the elements from the set
# .pop() -> remove arbitary elements
# add to sets -> set1.update(set2)
# join to sets -> set3 = set1.union(set2)
# .set2.difference(set1)
#  intersction -> .intersection()
