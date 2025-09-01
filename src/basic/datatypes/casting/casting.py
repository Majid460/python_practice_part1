"""
Casting in Python is a very important concept
There may be times when you want to specify a type on to a variable. This can be done with casting.
Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
# Example of casting
name = "Alice"
age = 25
weight = 50.3 #KG
height = "5.3"

#1. Convert age to string
age_str = str(age)
print (f"age to string -> {age_str}",end='\n')
print(f"Type of age -> {type(age_str)}",end='\n')
"""
age to string -> 25
Type of age -> <class 'str'>
"""
#2. Convert float to int
int_num = int(weight)
print (f"weight to int -> {int_num}",end='\n')
print(f"Type of weight -> {type(int_num)}",end='\n')
"""
weight to int -> 50
Type of weight -> <class 'int'>
"""
#3. Convert string to float
float_num = float(height)
print (f"height to float -> {float_num}",end='\n')
print(f"Type of height -> {type(float_num)}",end='\n')
"""
height to float -> 5.3
Type of height -> <class 'float'>
"""
#4. int to float
float_age= float(age)
print (f"Int to float -> {float_age}",end='\n')
print(f"Type of age -> {type(float_age)}",end='\n')
"""
Int to float -> 25.0
Type of age -> <class 'float'>
"""