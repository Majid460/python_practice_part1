"""
Hash Table

A Hash Table is a data structure designed to be fast to work with.

The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for, adding, and deleting data can be done really quickly, even for large amounts of data.

In a Linked List, finding a person "Bob" takes time because we would have to go from one node to the next, checking each node, until the node with "Bob" is found.

And finding "Bob" in an Array could be fast if we knew the index, but when we only know the name "Bob", we need to compare each element (like with Linked Lists), and that takes time.

With a Hash Table however, finding "Bob" is done really fast because there is a way to go directly to where "Bob" is stored, using something called a hash function.
"""
from unicodedata import numeric

"""
Building A Hash Table from Scratch
To get the idea of what a Hash Table is, let's try to build one from scratch, to store unique first names inside it.

We will build the Hash Set in 5 steps:

- Starting with an array.
- Storing names using a hash function.
- Looking up an element using a hash function.
- Handling collisions.
- The basic Hash Set code example and simulation.
"""


# 1. Starting with an Array
# Using an array, we could store names like this:
class HashTables:
    """
    To keep it simple, let's assume there is at most 10 names in the list, so the array must be a fixed size of 10 elements.
    When talking about Hash Tables, each of these elements is called a bucket.
    """

    def __init__(self, hash_arr=None):
        if hash_arr is None:
            hash_arr = []
        self.hash_arr = hash_arr
        self.hash_table = [None] * 10  # Empty list with size 10 and filled with None

    # Insert in hashtable
    def insert_in_hashtable(self, val):
        index = self.hash_function(val)
        # Case 1: Slot is empty
        if self.hash_table[index] is None:
            self.hash_table[index] = val
        else:
            # Case 2: Slot already has a single value
            if isinstance(self.hash_table[index], str) or not isinstance(self.hash_table[index], list):
                self.hash_table[index] = [self.hash_table[index], val]
            # Case 3: Slot already has a list
            if isinstance(self.hash_table[index], list):
                if val not in self.hash_table[index]:
                    self.hash_table[index].append(val)

    def is_empty(self):
        return len(self.hash_arr) == 0

    def get_size_arr(self):
        return len(self.hash_arr)

    # Find bob in array
    def find_in_arr(self, element):
        if not self.is_empty():
            for i in range(self.get_size_arr()):
                if self.hash_arr[i] == element:
                    return {self.hash_arr[i]: i}
        else:
            return None

    # Define a hash function
    def hash_function(self, val):
        if isinstance(val, str):
            return sum(ord(char) for char in val) % 10
        elif isinstance(val, int):
            return val % 10
        else:
            return None

    def find_item_in_hashtable(self, val):
        index = self.hash_function(val)
        if isinstance(self.hash_table[index], list):
            bucket = self.hash_table[index]
            if val in bucket:
                return val
        elif self.hash_table[index] == val:
            return val
        else:
            return None


if __name__ == '__main__':
    hashTable = HashTables()
    my_array = ['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']
    hashTable.hash_arr = my_array

    # Find name from array
    name = hashTable.find_in_arr("Bob")
    if name is not None and isinstance(name, dict):
        key, value = next(iter(name.items()))
        print(f"{key} found at index : {value}")
        # Bob found at index : 3
    # With Hash function
    print(hashTable.hash_table)
    for i in my_array:
        hashTable.insert_in_hashtable(i)
    # [None, 'Jones', None, 'Lisa', None, 'Bob', None, 'Siri', None, None, None, None, 'Pete', None, None]
    print(hashTable.hash_table)
    hashTable.insert_in_hashtable("Alice")
    hashTable.insert_in_hashtable("Stuart")
    print(hashTable.hash_table)
    # [None, 'Jones', None, ['Lisa', 'Stuart'], None, 'Bob', None, 'Siri', ['Pete', 'Alice'], None]
    # Find element in hashtable
    item = hashTable.find_item_in_hashtable("Bob")
    item1 = hashTable.find_item_in_hashtable("Stuart")
    if item1 is not None:
        print(f"Item is found:: {item1}")
    if item is not None:
        print(f"Item is found:: {item}")

"""
The most important reason why Hash Tables are great for these things is that Hash Tables are very fast compared Arrays and Linked Lists, especially for large sets. Arrays and Linked Lists have time complexity 
O(n) for search and delete, while Hash Tables have just O(1) on average! 

When deleting a name from our Hash Set, 
we can also use the hash function to go straight to where the name is, and set that element value to None.
"""

"""
If the array was sorted alphabetically, we could use Binary Search to find a name quickly, 
but inserting or deleting names in the array would mean a big operation of shifting elements in memory.

-- To make interacting with the list of names really fast, let's use a Hash Table for this instead, or a Hash Set, which is a simplified version of a Hash Table.
"""
