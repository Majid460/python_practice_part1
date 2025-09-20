"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

lambda arguments : expression
"""
# a represents the arguments

x= lambda a:a+4
print(x(2))

# 6

def add(a):
    return lambda y:y+a

lam = add(2) # It returns the inner lambda function

print(lam(2))
# 4

