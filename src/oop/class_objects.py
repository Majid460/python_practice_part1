"""
OOP stands for Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

Advantages of OOP
Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)
Allows you to build reusable applications with less code
Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.
"""
# class
"""
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""
class A:
    test = 1223

    def function(self):
        return print("Inside function")

a = A()
a.function()
print(A.test)
"""
Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. For example (assuming the above class):

x = A()
creates a new instance of the class and assigns this object to the local variable x.

The instantiation operation (“calling” a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named __init__(), like this:

def __init__(self):
    self.data = []
"""
class User:
    def __init__(self,name):
        self.name = name
    def display(self):
        return print(f"Name of user is:: {self.name}")

user = User("Test")
user.display()
# Name of user is:: Test

"""
Instance Objects::

Now what can we do with instance objects? The only operations understood by instance objects are attribute references.
There are two kinds of valid attribute names: data attributes and methods.

When you create an instance of a class, that instance can have attributes (variables or methods).
There are two main types:

1. Data attributes (variables attached to the instance).

2. Method attributes (functions that belong to the instance).
"""
#1. Instance Objects
user.age = 23
print(f"Name:{user.name} and age :{user.age}")
# Name:Test and age :23
# So Data attributes are variables that attach to the instance without declaring in class

# Method Attribute (Method Objects)
dis = user.display # # store the method object
dis()
# Name of user is:: Test
"""
Even though you stored it in dis, it remembers user.
That’s why calling dis() still works — user is attached automatically.
"""

# Instance Variables and Class Variables
"""
Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:
"""
class Animal:
    kind = "General"

    def __init__(self,name):
        self.name = name

dog = Animal("German shepherd")
cat = Animal("Cat 1")

# Instance variable
# Create the objects for every animal and access instance variables
print(dog.name)
print(cat.name)
"""
German shepherd
Cat 1
"""
# Class variables
print(dog.kind)
print(cat.kind)
# You can see the kind of every variable accessed by objects is general
"""
General
General
"""
"""
Note:
These shared variables (Class variables) could not be a mutable objects such as lists or dictionaries  
"""
# Let's say Animal class has a list
class Animal:
    kind = "General"
    tricks = []

    def __init__(self,name):
        self.name = name

    def add_trick(self,trick):
        self.tricks.append(trick)

e = Animal("Grm")
d = Animal("Hol")
e.add_trick("t1")
d.add_trick("t2")
print(e.tricks)
print(d.tricks)

"""
You can see clearly both objects added values in single shared list
['t1', 't2']
['t1', 't2']
"""

# To overcome this we need to define the list for every object separately
"""
Abstract Class

A blueprint for classes that can include:
Abstract methods (no implementation, must be overridden).
Concrete methods (with implementation, subclasses can reuse or override).
Attributes/fields (shared state).
Cannot be instantiated directly.

Example in Python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):  # must be overridden
        pass

    def info(self):  # concrete method
        return f"This is {self.name}"

class Dog(Animal):
    def speak(self):
        return "Woof!"


✅ Here:

Animal = abstract class.
It has state (self.name) and a concrete method info().
Dog must implement speak().
🔹 Interface
A pure contract (in strict OOP languages).
Contains only abstract methods (no implementation, no state).
A class must implement all methods from the interface.
⚡ In Python, there’s no dedicated interface keyword.
Instead, interfaces are modeled with abstract base classes (ABCs) that contain only abstract methods.

Example in Python
from abc import ABC, abstractmethod

class Flyable(ABC):  # Interface-like
    @abstractmethod
    def fly(self):
        pass

class Bird(Flyable):
    def fly(self):
        return "Flying with wings!"


✅ Here:

Flyable acts like an interface.

Bird must implement fly().

🔑 Key Differences (General OOP + Python)
Feature	Abstract Class	                                     Interface (Python = pure ABC)
Purpose	Provides a base implementation + contract	         Defines only a contract
Methods	Can have abstract + concrete methods	             Only abstract methods (no implementation)
Attributes/State	Can have fields/constructors	         No fields (pure contract)
Inheritance	Subclass extends one abstract class	             A class can implement multiple interfaces
Python support	class X(ABC) with abstract + normal methods	 class X(ABC) with only abstract methods
✅ Summary

Abstract class → Use when you want to share common code + enforce rules.
Interface → Use when you want to enforce a contract only (no shared implementation).
In Python: both are implemented using abc.ABC, but abstract classes may mix concrete + abstract methods, while interfaces are typically only abstract.
"""