########### Aliasing ###########
import copy
l1 = [10, 20, 30, 40, 50, 60]
l2 = l1  # l1 -> [10, 20, 30, 40, 50] <- l2
# creating duplicate reference variable
'''
l1[1] = 60
print(f'l1:{l1} l2:{l2}')
'''
# THE PROBLEM WITH ALIASING IS, BY USING IBE REFERENCE IF WE CHANGE ANY ONE REFERENCE , AUTOMATICALLY THOSE CHANGE WILL BE FOR THE REMAINING REFERENCE

# IF WE WANT DUPLICTAE OBJECT INSTEAD OF DUPLICATE REFERENCE VARIABLES THAN WE SHOULD GO FOR CLONNING

############# Cloning ###########
'''
l2 = l1.copy()
print(id(l2))
print(id(l1))
l1[1] = 60
print(f'l1:{l1} l2:{l2}')
'''

####### Deep Cloning and Shallow Cloning ####

# shallow clonning :
'''
l1 = [10, 20, [30, 40], 50]
print(l1[2][0])
l2 = l1.copy()
l1[0] = 77
l1[2][0] = 5230
print(f'l1:{l1} l2:{l2}')
'''
# shallow cloning
'''
l1 = [10, 20, [30, 40], 50]
print(l1[2][0])
l2 = copy.copy(l1)
l1[0] = 77
l1[2][0] = 5230
print(f'l1:{l1} l2:{l2}')
'''
# Deep cloning
l1 = [10, 20, [30, 40], 50]
print(l1[2][0])
l2 = copy.deepcopy(l1)
l1[0] = 77
l1[2][0] = 5230
print(f'l1:{l1} l2:{l2}')


# if we dont have no nested objects there than there are no need of deep cloning
