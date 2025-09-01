"""
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.
"""
#1. Compare value
print(10 > 9)
print(10 == 9)
print(10 < 9)
"""
True
False
False
"""

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# b is not greater than a

print(bool("Hello"))
print(bool(15))

"""
True
True
"""
#2. Which values are ture and which are false
"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
print(bool("abc"))  # True
print(bool(123)) # True
print(bool(["apple", "cherry", "banana"])) # True

#Table
"""
Value	    bool(value)
0	        False
15	        True
-1	        True
""          (empty string)	False
"Hello"	    True
[]          (empty list)	False
[1, 2]	    True
None	    False

In fact, there are not many values that evaluate to False, except empty values, such as (), [], {},
 "", the number 0, and the value None. And of course the value False evaluates to False.
"""
print(bool(False))    #False
print(bool(None))     #False
print(bool(0))        #False
print(bool(""))       #False
print(bool(()))       #False
print(bool([]))       #False
print(bool({}))       #False

"""
One more value, or object in this case, evaluates to False,
 and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
"""
class Myclass:
  def __len__(self):
    return 0

myobj = Myclass()
print(bool(myobj)) # False