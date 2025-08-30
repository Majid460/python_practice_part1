# Python Dictionary Tutorial

A comprehensive guide to understanding and working with dictionaries in Python.

## Table of Contents
- [What are Dictionaries?](#what-are-dictionaries)
- [Dictionary Characteristics](#dictionary-characteristics)
- [Creating Dictionaries](#creating-dictionaries)
- [Accessing Dictionary Elements](#accessing-dictionary-elements)
- [Dictionary Ordering](#dictionary-ordering)
- [Modifying Dictionaries](#modifying-dictionaries)
- [Removing Elements](#removing-elements)
- [Copying Dictionaries](#copying-dictionaries)
- [Nested Dictionaries](#nested-dictionaries)
- [Interactive Dictionary Creation](#interactive-dictionary-creation)

## What are Dictionaries?

Dictionaries are Python's built-in data structure for storing **key-value pairs**. They are one of the most versatile and commonly used data types in Python.

### Basic Template
```python
dict = {
    "key1": "value1",
    "key2": "value2",
    1: "numeric_key_example"
}
```

## Dictionary Characteristics

- **Changeable (Mutable)**: You can modify dictionaries after creation
- **Ordered**: As of Python 3.7+, dictionaries maintain insertion order
- **No Duplicates**: Keys must be unique
- **Key Requirements**: Keys must be immutable (strings, numbers, tuples)
- **Value Flexibility**: Values can be any data type

## Creating Dictionaries

### 1. Empty Dictionary
```python
dictionary = {}
```

### 2. Dictionary with Elements
```python
d = {"A": "AA", "B": "BB"}
```

### 3. Using Constructor
```python
d_con = dict([("A", "AA"), ("C", "BB")])
```

## Accessing Dictionary Elements

### 1. Direct Key Access
```python
print(d['A'])  # Output: AA
```

### 2. Get All Elements
```python
print(d)  # Output: {'A': 'AA', 'B': 'BB'}
```

### 3. Get All Keys as List
```python
print(list(d))  # Output: ['A', 'B']
```

### 4. Get Sorted Keys
```python
print(sorted(d))  # Output: ['A', 'B']
```

### 5. Loop Through Dictionary

#### Basic Key Iteration
```python
for key in d:
    print(f"{key} => {d[key]}")
```

#### Key-Value Iteration
```python
for k, v in d.items():
    print(f"{k} => {v}")
```

#### Enumerated Iteration (with Index)
```python
for i, k in enumerate(d):
    print(f"{i} => {k}")
```

#### Zip Multiple Dictionaries
```python
for a, b in zip(d, d_con):
    print(f"Zip of two dictionaries => {a} => {b}")
```

### 6. Dictionary Comprehension
```python
di = {x: x*2 for x in (2, 4, 6)}
# Output: {2: 4, 4: 8, 6: 12}
```

## Dictionary Ordering

Dictionaries maintain insertion order since Python 3.7:

### Order Rules
- Order is based on when a key was **first inserted**
- Updating an existing key's value **does not** change its position
- Deleting and reinserting a key moves it to the **end**

### Examples
```python
d = {"x": 1, "y": 2, "z": 3}
print(list(d.keys()))  # ['x', 'y', 'z']

# Updating value doesn't change order
d["y"] = 100
print(list(d.keys()))  # ['x', 'y', 'z']

# Delete and reinsert moves to end
del d["y"]
d["y"] = 200
print(list(d.keys()))  # ['x', 'z', 'y']
```

## Modifying Dictionaries

### Update Method
Add new key-value pairs to the end of the dictionary:
```python
d.update({"a": 12})
```

## Removing Elements

### 1. Remove Specific Element
```python
d.pop("key_name")  # Removes and returns the value
```

### 2. Remove Last Element
```python
d.popitem()  # Removes and returns the last key-value pair
```

### 3. Delete Using `del`
```python
del d["key_name"]  # Removes the key-value pair
```

### 4. Clear All Elements
```python
d.clear()  # Makes dictionary empty
```

### 5. Delete Dictionary Completely
```python
del d  # Removes the dictionary object entirely
```

## Copying Dictionaries

### ⚠️ Shallow Copy Problem
```python
d = {"a": 1, "b": 2, "c": 3}
d_copy = d  # This creates a reference, NOT a copy!

# Both variables point to the same memory location
print(id(d))       # Same address
print(id(d_copy))  # Same address
```

### ✅ Proper Deep Copy Methods

#### Method 1: Using `.copy()`
```python
d_copy = d.copy()
print(id(d))       # Different address
print(id(d_copy))  # Different address
```

#### Method 2: Using `dict()` Constructor
```python
d_copy = dict(d)
print(id(d))       # Different address
print(id(d_copy))  # Different address
```

## Nested Dictionaries

Dictionaries can contain other dictionaries as values:

```python
s1 = {"name": "Alice", "age": 19}
s2 = {"name": "Bob", "age": 20}
s3 = {"name": "John", "age": 21}

students = {
    "student_one": s1,
    "student_two": s2,
    "student_three": s3
}
```

### Accessing Nested Elements
```python
print(students["student_one"]["name"])  # Output: Alice
```

### Looping Through Nested Dictionaries
```python
for k, v in students.items():
    print(f"Complete object: {k} => {v}")
    for i in v:
        print(f"Detail about each object: {i} => {v[i]}")
```

## Interactive Dictionary Creation

You can create dictionaries dynamically using user input:

```python
new_dict = {}
size_dict = int(input("Enter the size of the dictionary: "))

for i in range(size_dict):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    new_dict[key] = value

print(f"Dictionary after insertion: {new_dict}")
```

## Key Takeaways

1. **Dictionaries are mutable** - you can change them after creation
2. **Keys must be unique and immutable** - use strings, numbers, or tuples
3. **Values can be anything** - including other dictionaries, lists, or objects
4. **Order matters** - dictionaries maintain insertion order (Python 3.7+)
5. **Use proper copying methods** - avoid shallow copy issues with `=`
6. **Powerful iteration options** - multiple ways to loop through data
7. **Dictionary comprehension** - create dictionaries efficiently with expressions

## Common Use Cases

- **Data mapping**: Associate related information
- **Caching**: Store computed results with keys
- **Configuration**: Store application settings
- **Counting**: Count occurrences of items
- **Grouping**: Organize data by categories
- **Database-like operations**: Store records with unique identifiers

---

**Note**: This tutorial covers Python dictionaries from basic creation to advanced nested structures. Practice with these examples to master dictionary manipulation in Python!