"""
Hash Maps

- A Hash Map is a form of Hash Table data structure that usually holds a large number of entries.
- Using a Hash Map we can search, add, modify, and remove entries really fast.
- Hash Maps are used to find detailed information about something.
A person can be looked up using a person's unique social security number (the Hash Map key), and then we can see that person's name (the Hash Map value).

- We will store hash maps in the key value pair
- With tuple
[("123-4672", "Adele"),()]
In the above list we have a tuple in the format of key, value pair and by accessing each key we can access the values.
- If let's say we need to store more detail in hash map for one id.
[("123-4672", {"name": "Adele", "age": 28, "email": "adele@mail.com"})]
Then we need to have dictionary inside for every key.

And let's say we have to improve it then we can have class
[("123-4672", User("Adele", 28, "adele@mail.com")),]

"""
from dataclasses import dataclass

from src.datastructures.dict.dict import value


# _ use for protected members
# __ use for private members

@dataclass
class User:
    name: str
    age: int
    email: str


class HashMap:
    def __init__(self):
        self.hash_map = [None] * 10

    def hash_function(self, key):
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10

    def is_empty(self):
        return all(slot is None for slot in self.hash_map)

    def add(self, key, val):
        index = self.hash_function(key)
        if not key and not val:
            return "Key and value is empty"
        # Case 1: If key and value is empty at index
        if self.hash_map[index] is None:
            self.hash_map[index] = [(key, val)]
            return
        # Add or update a key-value pair
        else:
            bucket = self.hash_map[index]
            for i, (k, v) in enumerate(bucket):
                if key == k:
                    bucket[i] = (key, val)  # Update existing key
                    return
            bucket.append((key, val))
    # Get a data based on key
    def get(self,key):
        index = self.hash_function(key)
        bucket = self.hash_map[index]
        if isinstance(bucket,list):
            for i,(k,v) in enumerate(bucket):
                print(f"Bucket {k}: {v}")

    def display(self):
        for i,bucket in enumerate(self.hash_map):
            print(f"Bucket {i}: {bucket}")



if __name__ == '__main__':
    hash_map = HashMap()
    users = [
        User("Adele", 28, "adele@mail.com"),
        User("Charlotte", 29, "charlotte@mail.com"),
        User("Thomas", 25, "thomas@mail.com"),
        User("Jens", 24, "jens@mail.com"),
        User("Peter", 23, "peter@mail.com"),
        User("Lisa", 22, "lisa@mail.com"),
        User("Michaela", 21, "michaela@mail.com"),
        User("Bob", 20, "bob@mail.com")
    ]
    keys = ["123-4568", "123-4569", "123-4570", "123-4571", "123-4672", "123-4573", "123-6574", "123-65749"]

    for k, u in zip(keys, users):
        hash_map.add(k, u)

    hash_map.display()
    print("------------------ Get Value of certain bucket--------------\n")
    hash_map.get(keys[0])
