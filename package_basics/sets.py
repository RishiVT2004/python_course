'''works in same way as set theory'''
'''
#set1 = {2,2,4,1,5}
#print(set1)
"""
immutable
no duplicate items(dups are eliminated while printing}
unordered
elements are not accessible set{0} -> invalid 
"""

set()
#empty set creation not set = {} -> dict
print(set)
'''

'''set methods'''

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
print(s1.union(s2))  # dosen't update s1
print(s1.intersection(s2))

# s1.update(s2) / s1.intersection_update(s2) also change the value of s1.

s3 = s1.symmetric_difference(s2)
print(s3)

print(s1.issubset(s2))
print((s1.intersection(s2)).issubset(s1))

s1.add(10)
print(s1)

s1.remove(4)
print(s1)

s1.discard(1)
print(s1)  # discard dosen't throw error if we delete an item which is not in set

s2.pop()  # props a random element
print(s2)

del s3  # deletes entire set

s2.clear()  # clears all element in set making it empty
print(s2)

