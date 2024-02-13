'''
Lambda function
syntax -: lambda arguments: expression

addition = lambda x, y, z: x + y + z
multiplication = lambda x, y, z: x * y * z

print(addition(10, 15, 20))
print(multiplication(3, 5, 7))


addition = lambda x, y, z: x + y + z
multiplication = lambda x, y, z: x * y * z

print(addition(10, 15, 20))
print(multiplication(3, 5, 7))

'''
'''
1.map()


The map() function applies the specified function to each item in the iterable (such as a list) and returns an iterator that yields the results.
It takes two parameters:
    -> function: The function to apply to each item.
    -> iterable: The iterable containing the items to be operated on.
It is commonly used with lambda functions to apply a transformation to each element of a list.
'''

'''
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))

cubic_numbers = map(lambda x: x ** 3, numbers)
print(list(cubic_numbers))
'''

'''
2. filter()'
The filter() function constructs an iterator from elements of 
the iterable for which the specified function returns true.
'''

'''
list_num = []
for i in range(0,10):
        list_num.append(i)

print(list_num)

even_num = filter(lambda x:x%2 == 0,list_num)
print(list(even_num))
'''

'''
3.sorted()

The sorted() function returns a new sorted list from the items in the iterable.

It takes three parameters:
-> iterable: The iterable containing the items to be sorted.
-> key (optional): A function that specifies the sorting criteria. If not provided, the items are sorted based on their natural order.
-> reverse (optional): A boolean value that indicates whether the sorting order should be reversed.
It is commonly used with lambda functions to specify custom sorting criteria.
'''

words = ['banana', 'apple', 'cherry']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['apple', 'banana', 'cherry']
