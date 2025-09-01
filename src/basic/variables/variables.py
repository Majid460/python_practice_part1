
"""
There are multiple ways to create variables.
1. Global Variables
2. Output Variables
3. Class Variables (will cover later)
"""

# 1. Simple variables

name = "Majid"
age = 25
weight =  78.5 #kg
height = 6 #ft
hasJob = False

# Applied to interpolate on the string
print(f"Name = {name}", f"Age = {age}", f"Weight = {weight}", f"Height = {height}" , f"Has Job = {hasJob}",sep=" , ")
"""
The following code prints:
Name = Majid , Age = 25 , Weight = 78.5 , Height = 6 , Has Job = False
"""

# 2. Datatypes
"""
As we have applied different data types to variables without
specifying the data types so lets check the data types.
"""

print(f" Name datatype -> {type(name)}", end = '\n')
print(f" Age datatype -> {type(age)}", end = '\n')
print(f" Weight datatype -> {type(weight)}", end = '\n')
print(f" Height datatype -> {type(height)}", end = '\n')
print(f" Has Job -> {type(hasJob)}", end = '\n')
"""
The following code prints:
 Name datatype -> <class 'str'>
 Age datatype -> <class 'int'>
 Weight datatype -> <class 'float'>
 Height datatype -> <class 'int'>
 Has Job -> <class 'bool'>
"""

"""
So we have seen python interpreter automatically handled all the datatypes on runtime
Interpreter determines the type when the program is running

Next -> Lets see more on datatypes 
"""
# Assign the integer value to name variable
name = 12

print(f"Name = {name}",end = '\n')

# Prints -> Name = 12
"""
Means python checked on runtime and assign the integer 
to a string variable and changed the value in the memory 
as both were pointing to same value in memory
"""

# We can assign the variable data type when we are initializing it

test : str = "Test"

print(f"Test = {test}", end = '\n')
# Prints  -> Test = Test

# Assign the integer value to the string variable (compiler is giving warning but code runs successfully)
test = 1
print(f"Test = {test}", end = '\n')
# Prints -> Test = 1

"""
This is just a type hint, not a strict rule. 
Because Python is dynamically typed and type annotations are not enforced at runtime
Python reassigns test to an int, and does not enforce the str type hint.
"""

"""
Note:
Rules for Python variables:

    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.

"""

# Multi words variables names

"""
There are many ways to create multiple words variables names.
1. Camel Case (Each word's first character will start with capital letter except first word e.g. hasJob)
2. Pascal Case (Each word's first character will start with capital letter e.g. HasJob)
3. Snake Case (Each word is seperated by under score e.g. has_job)
"""
# Multiple Assignment

a,b,c  = 0,"test",2.3
x = y = z = 10

print(a,b,c)
 # prints -> 0 test 2.3
print(x,y,z)
# prints -> 10 10 10


# Destructuring and Variable initialization

a,b,c = [1,2,3]
print(a,b,c)
#prints -> 1 2 3

# Global Variables

