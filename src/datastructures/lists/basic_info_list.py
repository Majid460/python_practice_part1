# LISTS
"""
To check the detail about list please refer to README.md in the same list folder
"""
import copy
from collections import deque

# Create an empty list
empty_list = []

# Create a non-empty list
non_empty_list = [1, 2, 3]

# Print a list
print(f"Non empty list initially => {non_empty_list}")
# prints -> [1, 2, 3]
print("\n----------- List Methods -------------\n")
# Add an element using append
non_empty_list.append(4)
empty_list.append(5)
print(f"empty list after appending [5] => {empty_list}")
# prints -> [5]
print(f"Non empty list after appending [4] => {non_empty_list}")
# prints -> [1, 2, 3, 4]

# Extend list
non_empty_list.extend(empty_list)
print(f"Non empty list after extending with empty list => {non_empty_list}")
# prints -> [1, 2, 3, 4, 5]

# Insert at specific index
non_empty_list.insert(0, 0)
print(f"Non empty list after inserting at Position [0] => {non_empty_list}")
# prints -> [0, 1, 2, 3, 4, 5]

# Remove an element
non_empty_list.remove(5)
print(f"List after removing 5 => {non_empty_list}")
# prints -> [0, 1, 2, 3, 4]

# Pop last element
non_empty_list.pop()
print(f"List after popping last element => {non_empty_list}")
# prints -> [0, 1, 2, 3]

# Pop at specific index
non_empty_list.pop(3)
print(f"List after popping element at index 3 => {non_empty_list}")
# prints -> [0, 1, 2]

# Clear list
empty_list.clear()
print(f"Empty list after clear => {empty_list}")
# prints -> []

# Find index
index = non_empty_list.index(1)
print(f"Index of 1 in non_empty_list => {index}")
# prints -> 1

# Count elements
count = non_empty_list.count(1)
print(f"Count of 1 in non_empty_list => {count}")
# prints -> 1

# Insert and Sort
non_empty_list.insert(0, 100)
print(f"List after inserting 100 at front => {non_empty_list}")
# prints -> [100, 0, 1, 2]
non_empty_list.sort()
print(f"List after sorting => {non_empty_list}")
# prints -> [0, 1, 2, 100]

# Reverse
non_empty_list.reverse()
print(f"List after reversing => {non_empty_list}")
# prints -> [100, 2, 1, 0]

print("\n----------- Shallow Copy -------------\n")
# Shallow copy
"""
The shallow copy of list means it only copies the outer list and all inner lists are still referencing the same memory location and 
so it is called a shallow copy.

"""
copy_list = non_empty_list.copy()
print(f"Copied list (shallow) => {copy_list}")
print(f"Original list memory address => {id(non_empty_list)}")
print(f"Copied list memory address => {id(copy_list)}")
# prints different memory addresses
"""
So you can clearly see that the both arrays are on different memory locations.
"""
# Nested list shallow copy
nested_list = [1, [2, 3], 4]
copied_ref = nested_list
print(f"Copied reference of nested list => {copied_ref}")
print(f"Memory address of nested_list => {id(nested_list)}")
print(f"Memory address of copied_ref => {id(copied_ref)}")
# prints same memory address

# Shallow copy of nested list
copied_shallow = nested_list.copy()
print(f"Copied shallow of nested list => {copied_shallow}")
print(f"Memory address of nested_list => {id(nested_list)}")
print(f"Memory address of copied_shallow => {id(copied_shallow)}")
print(f"Memory address of inner list in copied_shallow => {id(copied_shallow[1])}")
print(f"Memory address of inner list in nested_list => {id(nested_list[1])}")
# inner list memory address is same → shallow copy

"""
So as you can see the in the copied list inner list is not copied and it is still pointing to the same location of parent. Means
its just memory address is copied and we call it referencing
"""
print("\n----------- Deep Copy -------------\n")
# Deep copy
"""
Deep copy copies the inner and outer elements of array in new memory locations.
"""
deep_copy = copy.deepcopy(nested_list)
print(f"Deep copied list => {deep_copy}")
print(f"Memory address of deep_copy => {id(deep_copy)}")
print(f"Memory address of deep_copy[1] => {id(deep_copy[1])}")
print(f"Memory address of nested_list[1] => {id(nested_list[1])}")
# inner list memory address is different → deep copy

print("\n----------- Lists As Stacks -------------\n")
# Stacks using list
"""
To check the detail about stacks see the Readme.md file in the lists folder.
"""
_stack = [1, 2, 3, 4]
print(f"Initial stack => {_stack}")
# prints -> [1, 2, 3, 4]

# Push to stack
"""
Add an element in stack 
Means on the last of stack
Append() standard function of list adds a new element in the last of list
"""
_stack.append(5)
print(f"Stack after appending 5 => {_stack}")
# prints -> [1, 2, 3, 4, 5]

# Pop a element from the stack
_stack.pop()
print(f"Stack after popping last element => {_stack}")
# Stack after popping last element => [1, 2, 3, 4]


print("\n----------- Lists As Queues -------------\n")
"""
Add an element in queue (Queues element must be like First in First out) 
Means on the last of queue using append
Append() standard function of list adds a new element in the last of list

We will be using deque library from collections to implement Queues.
To dequeue a element from the front of the queue we will use popLeft().
"""
_queue = deque([1,2,3])
print(f"Queue => {_queue}")

_queue.append(4)
print(f"Queue after enqueue 4 => {_queue}")
# Queue after enqueue 4 => deque([1, 2, 3, 4])

# Dequeue elements of queue
_queue.popleft()
print(f"Queue after dequeue 1 => {_queue}")
# Queue after dequeue 4 => deque([2, 3, 4])

