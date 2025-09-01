# Operators are used to perform operations on variables and values.

"""
Python divides the operators in the following groups:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators

Note: For Arithmetic operators and Operator Precedence
See README.md 2.1.1. Basic Arithmetic Operations for explanation on operators
"""
"""
1. Assignment Operators
Assignment operators are used to assign values to variables
"""
# 1.1. Equal operator (=)
x = 3
print(f"Value of x = 3 -> {x}",end='\n')
# Prints -> Value of x = 3 -> 3

# 1.2. Add and equal (+=)
x += 3
print(f"Value of x += 3 -> {x}",end='\n')
# Prints -> Value of x += 3 -> 6

# 1.3. Subtract and equal (-=)
x -= 3
print(f"Value of x -= 3 -> {x}",end='\n')
# Prints -> Value of x -= 3 -> 3

# 1.4. Multiply and equal (*=)
x *= 3
print(f"Value of x *= 3 -> {x}",end='\n')
# Prints -> Value of x *= 3 -> 9

# 1.5. Divide and equal (/=)
x /= 3
print(f"Value of x/=3 -> {x}",end='\n')
# Prints -> Value of x/=3 -> 3.0

# 1.6. Mod and equal (%=)
x %= 3
print(f"Value of x%=3 -> {x}",end='\n')
# Prints -> Value of x%=3 -> 0.0

# 1.6. Floor and equal (//=)
x = 9
x //= 3  # equals -> x = x//3
print(f"Value of x //= 3 -> {x}",end='\n')
# Prints -> Value of x //= 3 -> 3

#1.7. Power Operator (**=)
x **=3
print(f"Value of x **=3 -> {x}",end='\n')
#prints -> Value of x **=3 -> 27

#1.8. And and Equal &=
"""
It compares by bitwise
like x and 3 are applied using AND operator
lets say x = 6
  6 -> 110
  3 -> 011
------------
AND  -> 010 -> 2

it only keeps that both has
"""
x &=3
print(f"Value of x &=3 -> {x}",end='\n')
#prints -> Value of x &=3 -> 3

#1.9. OR and Equal |=
"""
It compares by bitwise
like x OR 3 are applied using OR operator
lets say x = 3
  3 -> 011
  3 -> 011
------------
OR  -> 011 -> 3

it only keeps that is present in any of them like x or 3
"""
x |=3
print(f"Value of x |=3 -> {x}",end='\n')
# prints -> Value of x |=3 -> 3

#1.10. This is a bitwise XOR assignment operation. ^=

"""
XOR (^) — "Exclusive OR"
Compares each bit of two numbers

If the bits are different, the result is 1
If the bits are the same, the result is 0

  x = 0   → 000
      3   → 011
----------------
Result    → 011 = 3

 5 → 101
 3 → 011
----------
      110 → 6
"""
x = 5
x ^= 3

print(f"Value of x ^=3 -> {x}",end='\n')

#1.11. Bitwise right shift assignment operator by n bits (>>=)
x = 8        # binary: 1000
x >>= 2      # shift 2 bits to the right 0010 -> 2
print(f"Value of x >>=3 -> {x}",end='\n')
# Value of x >>=3 -> 2

#1.12. Left shift by n bits (<<=)
x = 5       # binary: 0000 0101
x <<= 2      # shift 2 bits to the right  0001 0100 -> 20
print(f"Value of x <<=2 -> {x}",end='\n')

#1.13. := (Walrus Operator)
# It allows you to assign a value to a variable as part of an expression.
n = len("hello")
if n > 3:
    print(n)
# Output: 5
if (n := len("hello")) > 3:
    print(n)  # Output: 5
# It assigned on same line and compared values also

#2. Logical Operators
"""
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	    Returns True if one of the statements is true	x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true
"""
#2.1. AND, OR and NOT
x,y = 3,2
if x>3 and y>3:
    print(f"Value of x and y greater than 3 ", end='\n')  # Didn't Execute
elif not(x<3 or y<3):
    print(f"Not x less than 3 or y less than 3 ", end='\n') #Didn't Execute
elif x>=3 or y<3:
    print(f"x greater or equal to 3 or y less than 3 ", end='\n') # x greater or equal to 3 or y less than 3
else:
    print(f"x less than 3 or y less than 3 ", end='\n')

# 3. Python Identity Operators (IS or IS NOT)
print(f"Check x is y {x is y}", end='\n')
# Check x is y False
print(f"Check x is y {x is not y}", end='\n')
# Check x is y True

#4. Python Membership Operators (in or not in)
x = "This is a member"
y = "This is a member of Company"
print(f"Check x in y {x in y}", end='\n')
# Check x in y True
print(f"Check x not in y {x not in y}", end='\n')
# Check x not in y False

