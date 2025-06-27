## This is the documentation about list in python.

### * What is a List?
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

### 1. List Detail
Lists are created using square brackets:
list = []

Properties of List:
1. List items are ordered
2. List is a mutable collection
3. Lists can have duplicate items
4. List items can be accessed using the index e.g. list[0]

### 1.1. Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
E.g.
```python
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)  # Output: [10, 20, 30, 40]
```
### 1.2. Mutable (Changeable)  
    1.2.1. We can add new items in list
    1.2.2. We can remove items from list
    1.2.3. We can change items in list
    1.2.4. We can delete items from list

**1.2.1. Adding Elements**  
```python
a = [1, 2, 3]
a.extend([4, 5])      # [1, 2, 3, 4, 5]
a.insert(0, 0)        # [0, 1, 2, 3, 4, 5]
```

**1.2.2. Removing Elements**  
```python
a = [1, 2, 3]
a.pop()               # removes last element
a.pop(0)              # removes first element
a.remove(3)           # removes first occurrence of 3
del a[1]              # deletes element at index 1
```

**1.2.3. Updating Elements**  
```python
a = [1, 2, 3]
a[0] = 100            # change first element to 100
print(a)              # [100,2,3]
```

**1.2.4. Deleting Slices**  
```python
a = [1, 2, 3]
del a[1:3]            # delete a range
del a[:]              # delete entire list content
```

---

### 2.1. List Methods  

| Method              | Description |
|---------------------|-------------|
| `append(x)`         | Add item `x` to the end |
| `extend(iterable)`  | Add all elements from iterable |
| `insert(i, x)`      | Insert `x` at index `i` |
| `remove(x)`         | Remove first item with value `x` |
| `pop([i])`          | Remove and return item at index `i` |
| `clear()`           | Remove all items |
| `index(x)`          | Return index of first item with value `x` |
| `count(x)`          | Count occurrences of `x` |
| `sort()`            | Sort the list |
| `reverse()`         | Reverse the list |
| `copy()`            | Return a **shallow copy** |

---

📝 **Note on Copying**  
- `list.copy()` and `list[:]` both create a **shallow copy**.  
- Shallow copy means the outer list is copied, but nested objects still refer to the original.

---
### 2. Lists as Stacks
#### LIFO or FILO (Last in First out || First in Last out)

The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). 
To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. 

Example:
```python
_stack = [1,2,3,4]
# append() push an element in the last of stack
_stack.append(5)
print(_stack) 
#[1,2,3,4,5]

# Pop removes the top element of stack
_stack.pop()
print(_stack)
# [1,2,3,4]
```
---
### 3. Lists as Queues

#### FIFO or LILO (First out First out || Last in Last out)

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

Example:
```python
from collections import deque

queue = deque([1,2,3,4])

# add new element in the last of queue.
queue.append(5)
print(queue) 
# [1,2,3,4,5]

#Remove element from start of queue
queue.popleft()
print(queue)
# [2,3,4,5]
```
---

### Python Lists: Advance

### Table of Contents
1. [Converting Collections to Lists](#converting-collections-to-lists)
2. [Basic List Operations](#basic-list-operations)
3. [List Indexing and Slicing](#list-indexing-and-slicing)
4. [Creating Lists with Loops](#creating-lists-with-loops)
5. [Iterating Through Lists](#iterating-through-lists)
6. [2D Lists (Matrices)](#2d-lists-matrices)

---

### Converting Collections to Lists

Python allows you to convert various data types into lists using the `list()` function.

### From Tuple to List
```python
# Convert tuple to list
from_tuple_to_list = list(("a", "b", "c"))
print(from_tuple_to_list)  # Output: ['a', 'b', 'c']
```

### From Set to List
```python
# Convert set to list
from_set_to_list = list({"a", "b", "c"})
print(from_set_to_list)  # Output: ['a', 'b', 'c'] (order may vary)
```

### From String to List
```python
# Convert string to list (each character becomes an element)
from_string_to_list = list("abc")
print(from_string_to_list)  # Output: ['a', 'b', 'c']
```

---

### Basic List Operations

#### 1. Accessing Elements
```python
thisList = ["a", "b", "c", 1]
print(f"Access Element => {thisList[0]}")  # Output: Access Element => a
```

#### 2. Negative Indexing
Negative indexing allows you to access elements from the end of the list:
- `-1` refers to the last item
- `-2` refers to the second last item, etc.

```python
print(f"Negative indexing -> element at -1 index => {thisList[-1]}")
# Output: Negative indexing -> element at -1 index => 1
```

---

### List Indexing and Slicing

#### Range of Indexes
You can specify a range of indexes to get a subset of the list. The syntax is `list[start:end]` where `end` is exclusive.

```python
thisList = ["a", "b", "c", 1]

# Get elements from index 0 to 1 (excludes index 2)
print(f"Range [0:2] => {thisList[0:2]}")  # Output: ['a', 'b']

# From start to index 2 (excludes index 3)
print(f"Range [:3] => {thisList[:3]}")    # Output: ['a', 'b', 'c']

# From index 2 to end
print(f"Range [2:] => {thisList[2:]}")    # Output: ['c', 1]
```

#### Negative Range Indexing
```python
# Get elements using negative indexing
print(f"Negative Range [-3:-2] => {thisList[-3:-2]}")  # Output: ['b']
```

---

### Creating Lists with Loops

#### Method 1: Traditional For Loop
```python
# Add numbers 0 to 5 to the list
emp_list = []
for i in range(6):
    emp_list.append(i)
print(f"Items in list Method 1: => {emp_list}")
# Output: Items in list Method 1: => [0, 1, 2, 3, 4, 5]
```

#### Method 2: User Input with Loop
```python
# Example of taking user input (commented in original code)
emp_list_two = []
size_of = int(input("Enter the size of list: "))
for i in range(size_of):
    emp_list_two.append(i)
print(f"Items in list Method 2: => {emp_list_two}")
```

#### Method 3: User Input for Elements
```python
# Example of taking elements from user (commented in original code)
emp_list_three = []
size_of = int(input("Enter the size of list: "))
for _ in range(size_of):
    element = input("Enter the element: ")
    emp_list_three.append(element)
print(f"Items in list Method 3: => {emp_list_three}")
# Note: All elements are strings because input() returns strings
```

#### Method 4: List Comprehension (Modern Approach)

**Basic List Comprehension:**
```python
empty_list_comp = [i for i in range(4)]
print(f"Items in list comprehension 1: => {empty_list_comp}")
# Output: Items in list comprehension 1: => [0, 1, 2, 3]
```

**Advanced List Comprehension:**
```python
# Example with user input (commented in original code)
size = int(input("Enter the size of the list: "))
items = [input(f"Enter item {_+1}: ") for _ in range(size)]
print(f"Items in list => {items}")
```

---

### Iterating Through Lists

#### Using For Loop with Range
```python
thisList = ["apple", "banana", "cherry"]
for i in range(len(thisList)):
    print(f"Printing using for loop => {thisList[i]}")

# Output:
# Printing using for loop => apple
# Printing using for loop => banana
# Printing using for loop => cherry
```

#### Using While Loop
```python
i = 0
while i < len(thisList):
    print(f"Printing using while loop => {thisList[i]}")
    i += 1

# Output:
# Printing using while loop => apple
# Printing using while loop => banana
# Printing using while loop => cherry
```

#### Using List Comprehension for Printing
```python
[print(f"Printing using List comprehension loop => {thisList[i]}") 
 for i in range(len(thisList))]

# Output:
# Printing using List comprehension loop => apple
# Printing using List comprehension loop => banana
# Printing using List comprehension loop => cherry
```

---

### 2D Lists (Matrices)

A 2D list is a list of lists, commonly used to represent tables or matrices. The structure follows `[Rows][Columns]` indexing.

#### Matrix Structure Visualization
```
matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]

Visual representation:
         Column0 Column1 Column2
Row0  →    1       2       3
Row1  →    4       5       6
Row2  →    7       8       9
```

#### Accessing Matrix Elements

**Access Single Element:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Element at [0][0] => {matrix[0][0]}")  # Output: 1
```

**Access Entire Row:**
```python
print(f"First Row => {matrix[0][:]}")  # Output: [1, 2, 3]
```

**Access Column Elements:**
```python
# Print first column (index 0 from each row)
for row in matrix:
    print(f"First Column element => {row[0]}")

# Output:
# First Column element => 1
# First Column element => 4
# First Column element => 7
```

#### Iterating Through All Matrix Elements
```python
# Print all elements
for row in matrix:
    for element in row:
        print(f"Matrix element => {element}")

# Output:
# Matrix element => 1
# Matrix element => 2
# Matrix element => 3
# Matrix element => 4
# Matrix element => 5
# Matrix element => 6
# Matrix element => 7
# Matrix element => 8
# Matrix element => 9
```

#### Formatted Matrix Output
```python
# Create a nicely formatted matrix display
print(" " * 8 + "Column0 Column1 Column2")

for row_index, row in enumerate(matrix):
    print(f"Row{row_index}  →", end="    ")
    for item in row:
        print(f"{item:<7}", end="")  # Left-aligned with fixed width
    print()  # New line after each row

# Output:
#         Column0 Column1 Column2
# Row0  →    1      2      3      
# Row1  →    4      5      6      
# Row2  →    7      8      9      
```

---

### Key Takeaways

1. **List Conversion**: Use `list()` to convert tuples, sets, and strings to lists
2. **Indexing**: Python uses 0-based indexing; negative indexing starts from the end
3. **Slicing**: Use `[start:end]` syntax where `end` is exclusive
4. **List Creation**: Multiple methods available, with list comprehension being the most Pythonic
5. **2D Lists**: Think of them as lists containing other lists, accessed with `[row][column]` syntax
6. **Iteration**: Multiple ways to loop through lists, choose based on your needs

This guide covers the fundamental operations and concepts for working with lists in Python, from basic operations to more complex 2D list manipulati