'''
Abstraction in Python is the process of hiding the complex implementation details and showing only
 the necessary features of an object. It allows you to focus on what an object does rather than how
 it does it. This is typically achieved through abstract classes and methods.
'''
from abc import ABC, abstractmethod


# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Creating an instance of Circle
circle = Circle(5)

# Calling area and perimeter methods
print("Area of circle:", circle.area())
print("Perimeter of circle:", circle.perimeter())

'''
In this example, the Shape class is an abstract class that defines two abstract methods: 
area and perimeter. These methods are intended to be implemented by concrete subclasses. 
The Circle class is a concrete subclass of Shape that provides implementations for the area and 
perimeter methods. When you create an instance of Circle and call its area and perimeter methods, 
you're using the abstraction provided by the Shape class to work with shapes without worrying about
their specific implementations.
'''
