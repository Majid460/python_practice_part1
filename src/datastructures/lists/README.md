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

t is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
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