'''
In Python, the super() function is used to call methods of a superclass (parent class) in a subclass (child class).
It allows you to access the methods and properties of the parent class within the child class. This is particularly
useful when you want to extend the functionality of a parent class without re-implementing its methods.
'''

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        return f"{super().greet()} and I am {self.age} years old"

# Creating an instance of Child
child = Child("Rishi", 19)

# Calling the greet method of the Child class
print(child.greet())  # Output: Hello, my name is Alice and I am 10 years old
