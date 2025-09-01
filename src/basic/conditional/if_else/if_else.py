"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""
a = 33
b = 200
if b > a:
  print("b is greater than a")
# b is greater than a
"""
Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.
"""
#If statement, without indentation (will raise an error):

a = 33
b = 200
# if b > a:
# print("b is greater than a") # you will get an error
"""
    print("b is greater than a") # you will get an error
    ^
IndentationError: expected an indented block after 'if' statement on line 29
"""
#Elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#a and b are equal
"""
Else
The else keyword catches anything which isn't caught by the preceding conditions.
Example
"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#a is greater than b

# Short Hand if
if a > b: print("a is greater than b")

# Short Hand elif

print("a is greater than b") if a > b  else print("a is less than b")
# a is greater than b
"""
And
The and keyword is a logical operator, and is used to combine conditional statements:

Example
Test if a is greater than b, AND if c is greater than a:

"""
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# Both conditions are True
# Simplify version
if b < a < c:
    print("Both conditions are True")
# Both conditions are True

"""
Or
The or keyword is a logical operator, and is used to combine conditional statements:

Example:
Test if a is greater than b, OR if a is greater than c:
"""
if a > b or a > c:
    print("A is greater than B or A greater than C")
#A is greater than B or A greater than C

"""
Not
The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
"""
if not b>a:
    print("B is not greater than A")
#B is not greater than A

"""
The pass Statement:

if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
"""
a = 33
b = 200

if b > a:
  pass
else:
    pass
