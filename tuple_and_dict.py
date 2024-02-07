'''Tuple'''
# immutable ()
'''
tuple = (1,2,3,4,5,6,7,8,9)

# print(tuple)
for element in tuple:
    print(element,end=" ")

print(tuple[2])
print(tuple[4:7])
print(tuple.count(8))
print(tuple.index(5))

# Since tuples are immutable, methods like append(), insert(), remove(),
# and pop() which modify the tuple are not available for tuples.
'''

# Dictionary

# In Python, a dictionary is an unordered collection of key-value pairs.
# It's a versatile data structure that allows you to store and retrieve data efficiently.
# Dictionaries are defined using curly braces {}, with key-value pairs separated by colons :.

new_dict = {'name': 'Rishi', 'age': 19, 'branch': 'CSE', 'regd_no.': 2241013165, 'CGPA': 9.05}
# accessing value
print(new_dict['regd_no.'])
# only prints one key at a time

print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())

print(new_dict.get('name'))
new_dict.update({'package': '25lpa'})
print(new_dict.items())

print(new_dict.pop('age'))  # removes given key
print(new_dict.popitem())  # removes last key
print(new_dict.items())

new_dict.clear()  # clears dict
