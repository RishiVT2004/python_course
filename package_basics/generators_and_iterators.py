''''''
'''
Iterators

-> An iterator is an object that enables iteration over a sequence of data, such as lists, tuples, or dictionaries.
-> It implements the __iter__() and __next__() methods.
-> The __iter__() method returns the iterator object itself.
-> The __next__() method returns the next item in the sequence.
-> When there are no more items to return, __next__() raises the StopIteration exception.
-> Iterators can be created using iterables (objects that support iteration) by calling the iter() function.
'''

'''
class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1


l = [1, 2, 3, 4, 5]
iterator = Iterator(l)

for i in iterator:
    print(i, end=" ")
'''

'''
Generators 

-> Generators are a simpler way to create iterators using functions.
-> They use the yield keyword to return values one at a time, suspending the
    function's state between each value until it is resumed.
-> Generator functions return a generator object when called, which can be iterated
    over using a loop or other iteration constructs.
-> Generator functions can have multiple yield statements and can maintain their
    local state between calls.
-> Generators are often used to generate large sequences of data lazily, 
    saving memory and improving performance.
'''

'''
def generator(data):
    for x in data:
        yield x

l = [1,2,3,4,5]
gen = generator(l)

for y in gen:
    print(y)
'''