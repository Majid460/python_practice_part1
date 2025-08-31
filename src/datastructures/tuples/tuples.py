import copy

"""
Tuple

- Tuple is used to store multiple items in a single variable
- Tuple is a collection which is:
- Ordered, immutable, and allow duplicates

whereas list is Ordered, mutable, and allow duplicates
so the difference between tuple and list is mutability and immutability

Tuple is created with round brackets. ()
- Tuple is indexed based so we can access it using index and thats why we can have duplicate values in tuple
"""
print("\n----------- Basic Tuple -------------\n")
this_tuple = ("a", "b", "c", 1, 4)
print(f"This is basic tuple: {this_tuple}")
# This is basic tuple: ('a', 'b', 'c', 1, 4)
print(f"Tuple type: {type(this_tuple)}")
# Tuple type: <class 'tuple'>

print("\n----------- Basic Tuple Operations -------------\n")
print(f"Tuple value on index 1:: {this_tuple[1]}")
# Tuple value on index 1:: b

# Negative indexing (-1 Means from last index)
print(f"Tuple value on index -1:: {this_tuple[-1]}")
# Tuple value on index -1:: 4

# Range index (excludes the last index in range)
# this_tuple = ("a","b","c",1,4)
print(f"Tuple value in range of 1 to 3 index:: {this_tuple[1:4]}")
# Tuple value in range of 1 to 3 index:: ('b', 'c', 1)

# Range of negative indexes (-1 means last one and -4 means start one)
"""
- Negative indexing means starting from the end of the tuple.
- This example returns the items from index -4 (included) to index -1 (excluded)
- Remember that the last item has the index -1,
"""
print(f"Range of negative indexes from -4 to -1 :: {this_tuple[-4:-1]}")
# We can't put like that -1:-4 because -1 is greater and -4 is lesser, and we are
# counting from greater to lessor which don't work in range it should be smaller to higher
# Range of negative indexes from -4 to -1 :: ('b', 'c', 1)

# To check the existence of an item in tuple
item = "Apple"
tup = ("Banana", "Apple", "Orange", "Peach")
if item in tup:
    print(f" {item} is in the tuple")
# Apple is in the tuple
"""
Immutability
- Tuple is immutable and we can't change it once it is created
- So to change the tuple there is a workaround which is:
- Convert the tuple to list and then change it and then again convert it to tuple
"""
# 1. Change items from tuple
list_tup = list(tup)
list_tup[1] = "Pear"
tup_list = tuple(list_tup)
print(f"Tuple after changing: {tup_list}")
# Tuple after changing: ('Banana', 'Pear', 'Orange', 'Peach')

"""
To add an item to tuple as it is immutable and it don't has any append method.
- So to add an item we just need to convert it to a list
- Add new item.
"""
# 2. Add new items in tuple

# 1. First method by converting tuple to list
# for deepcopy of nested tuples
# tuple_ad = copy.deepcopy(this_tuple)

tuple_ad = tuple(tup_list)
from_tuple_to_list = list(tuple_ad)
from_tuple_to_list.append("Grapes")
from_list_to_tuple = tuple(from_tuple_to_list)
print(f"Tuple after adding new elements: {from_list_to_tuple}")
# Tuple after adding new elements: ('Banana', 'Pear', 'Orange', 'Peach', 'Grapes')

# 2. Second method by adding a tuple into another tuple
tuple_a = ("q", "s", "d")
tuple_b = ("r", "f", "g")
tuple_a += tuple_b
print(f"Tuples : {tuple_a}")
# Tuples : ('q', 's', 'd', 'r', 'f', 'g')

# 3. Remove items from tuple
"""
Tuples are immutable and that's why we cannot remove any item from tuple.
- To remove an item we need to convert it to list
"""
tuple_ad = tuple(from_list_to_tuple)
from_tuple_to_list = list(tuple_ad)
from_tuple_to_list.remove("Grapes")
from_list_to_tup = tuple(from_tuple_to_list)
print(f"Tuple after removing grapes: {from_list_to_tup}")
# Tuple after removing grapes: ('Banana', 'Pear', 'Orange', 'Peach')

# To delete the tuple completely use del
del from_list_to_tup
# print(f"Tuple after removing grapes: {from_list_to_tup}")
# Error - Name 'from_list_to_tup' can be undefined

# 4. Unpacking a tuple
# We can simply unpack a tuple by just assign it to variables
tup = ("Banana", "Apple", "Orange", "Peach")
(red, green, blue, white) = tup
print(red)
print(green)
print(blue)
print(white)
"""
Banana
Apple
Orange
Peach
"""
# Using asterisk* while unpacking
print("\n----------- Advance Tuple Operations -------------\n")
"""
If the number of variables is less than the number of values then use the *.
"""
(red, *green) = tup
print(red)  # Banana
print(green)  # ['Apple', 'Orange', 'Peach']

print("\n----------- Asterisk Tuple Operations -------------\n")
"""
If the asterisk is added to another variable name than the last, Python will assign values to the variable 
until the number of values left matches the number of variables left.
"""
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green) # apple
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red) # cherry

print("\n----------- Looping Tuple Operations -------------\n")
# 1. Using for loop
# Index based loop
print("Index based for loop::")
for i in range(len(fruits)):
    print(fruits[i])
"""
Index based for loop::
apple
mango
papaya
pineapple
cherry
"""
# 2. Simple loop
print("Simple for loop::")
for i in fruits:
    print(i)
"""
Simple for loop::
apple
mango
papaya
pineapple
cherry
"""

# 3. While loop
print("Loop using while loop::")
i = 0
while i< len(fruits):
    print(fruits[i])
    i+=1
"""
Loop using while loop::
apple
mango
papaya
pineapple
cherry
"""

print("\n----------- Join Tuple Operations -------------\n")
# 1. By plus
fruits+= from_list_to_tuple
print(fruits)
#('apple', 'mango', 'papaya', 'pineapple', 'cherry', 'Banana', 'Pear', 'Orange', 'Peach', 'Grapes')

# 2. By multiply * to a integer
# Multiple tuple
fruits =fruits*2
print(fruits)
# ('apple', 'mango', 'papaya', 'pineapple', 'cherry', 'Banana', 'Pear', 'Orange', 'Peach', 'Grapes', 'apple', 'mango', 'papaya', 'pineapple', 'cherry', 'Banana', 'Pear', 'Orange', 'Peach', 'Grapes')

print("\n----------- Tuple Methods -------------\n")
"""
Tuple Methods
Python has two built-in methods that you can use on tuples.
"""
# 1. Count
#Return the number of times the value 5 appears in the tuple:
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = this_tuple.count(5)
print(f"5 comes {x} times")
# Prints -> 5 comes 2 times

# 2. index
# Search for the first occurrence of the value 8, and return its position
"""
The index() method finds the first occurrence of the specified value.
The index() method raises an exception if the value is not found.
"""

x = this_tuple.index(8)

print(f"The first occurrence of 8 is at {x} index")
# The first occurrence of 8 is at 3 index