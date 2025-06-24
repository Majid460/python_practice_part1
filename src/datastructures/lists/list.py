# LISTS
"""
To check the detail about list please refer to README.md in the same list folder
"""
# Create an empty list

empty_list = []

# Create a non-empty list
non_empty_list = [1,2,3]

# Print a list

print(non_empty_list)
# [1, 2, 3]

# Add a element in the predefined list using append

non_empty_list.append(4)
empty_list.append(5)
print(empty_list)
# prints -> [5]
print(non_empty_list)
# [1, 2, 3, 4]

# Add elements of empty list to non_empty list using extend
non_empty_list.extend(empty_list)
print(non_empty_list)
# prints -> [1, 2, 3, 4, 5]

# insert a element at specific index
non_empty_list.insert(0,0)
print(non_empty_list)
# prints -> [0, 1, 2, 3, 4, 5]

# Remove a element from list (Remove first element from list that will be searched)
non_empty_list.remove(5)
print(non_empty_list)
# prints -> [0, 1, 2, 3, 4]

# Pop the last element from the list
non_empty_list.pop()
print(non_empty_list)
# Prints -> [0, 1, 2, 3]

