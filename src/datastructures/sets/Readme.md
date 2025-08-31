# Python Sets Tutorial

A comprehensive guide to understanding and working with sets in Python.

## Table of Contents
- [What are Sets?](#what-are-sets)
- [Set Characteristics](#set-characteristics)
- [Creating Sets](#creating-sets)
- [Basic Set Operations](#basic-set-operations)
- [Accessing Set Elements](#accessing-set-elements)
- [Modifying Sets](#modifying-sets)
- [Set Operations (Mathematical)](#set-operations-mathematical)
- [Set Methods Reference](#set-methods-reference)

## What are Sets?

Sets are Python's built-in data structure for storing **multiple unique items** in a single variable. They are the **complete opposite of lists** in terms of ordering and indexing.

### Basic Template
```python
my_set = {"apple", "banana", "cherry"}
```

## Set Characteristics

| Feature | Set | List | Tuple |
|---------|-----|------|-------|
| **Ordered** | ❌ No (Unordered) | ✅ Yes | ✅ Yes |
| **Indexed** | ❌ No | ✅ Yes | ✅ Yes |
| **Mutable** | 🔄 Partially* | ✅ Yes | ❌ No |
| **Duplicates** | ❌ No | ✅ Yes | ✅ Yes |
| **Syntax** | `{}` Curly braces | `[]` Square brackets | `()` Round brackets |

*Items are unchangeable, but you can add/remove items

## Creating Sets

### 1. Basic Set Creation
```python
my_set = {"apple", "banana", "cherry"}
print(f"Set => {my_set}")
# Output: {'banana', 'cherry', 'apple'} (order may vary)
```

### 2. Using Set Constructor
```python
set2 = set(("A", "B", "C"))
print(set2)  # {'A', 'B', 'C'}
```

### 3. Mixed Data Types
```python
set1 = {"abc", 34, True, 40, "male"}
```

## Basic Set Operations

### 1. No Duplicates Allowed
```python
my_set = {"apple", "banana", "cherry", "apple"}
print(f"After adding duplicate: {my_set}")
# Output: {'apple', 'banana', 'cherry'} (duplicate removed)
```

### 2. Special Case: Boolean and Numeric Values
```python
my_set = {"apple", "banana", "cherry", 1, True, 0, False}
print(f"With True/False and 0/1: {my_set}")
# Output: {0, 1, 'cherry', 'banana', 'apple'}
# Note: True=1 and False=0, so duplicates are removed
```

### 3. Length of Set
```python
print(f"Length of set: {len(my_set)}")
```

## Accessing Set Elements

**Important**: Sets are unordered and unindexed, so you **cannot access items by index**.

### 1. Iterate Through Set
```python
set2 = {"A", "B", "C"}

for element in set2:
    print(f"Element in set: {element}")
```

### 2. Check Membership
```python
print("A" in set2)      # True
print("G" not in set2)  # True
```

## Modifying Sets

### Adding Items

#### 1. Add Single Item
```python
set2 = {"A", "B", "C"}
set2.add("D")
print(f"After adding D: {set2}")
# Output: {'A', 'D', 'C', 'B'}
```

#### 2. Add Multiple Items (update)
```python
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

this_set.update(tropical)
print(f"After adding tropical set: {this_set}")
# Output: {'apple', 'papaya', 'cherry', 'pineapple', 'banana', 'mango'}
```

#### 3. Add Any Iterable
```python
this_set = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

this_set.update(mylist)
print(f"After adding list: {this_set}")
# Output: {'banana', 'cherry', 'orange', 'kiwi', 'apple'}
```

### Removing Items

#### 1. `remove()` - Raises Error if Not Found
```python
this_set.remove("apple")
print(f"After removing apple: {this_set}")
# Raises KeyError if "apple" doesn't exist
```

#### 2. `discard()` - Safe Removal (No Error)
```python
this_set.discard("kiwi")
print(f"After discarding kiwi: {this_set}")
# No error even if "kiwi" doesn't exist
```

#### 3. `pop()` - Remove Random Item
```python
removed_item = this_set.pop()
print(f"Removed random item: {removed_item}")
print(f"Set after pop: {this_set}")
# Note: You can't predict which item will be removed
```

#### 4. `del` - Delete Entire Set
```python
del this_set  # Completely deletes the set
```

## Set Operations (Mathematical)

### 1. Union (Combine All Items)
```python
set_a = {"apple", "banana", "cherry"}
set_b = {"pineapple", "apple", "papaya"}

# Method 1: union()
union_result = set_a.union(set_b)
print(f"Union: {union_result}")

# Method 2: | operator
union_result = set_a | set_b
print(f"Union with |: {union_result}")

# Method 3: update() (modifies original)
set_a.update(set_b)
print(f"Union with update: {set_a}")
```

### 2. Intersection (Common Items Only)
```python
set_a = {"apple", "banana", "cherry"}
set_b = {"pineapple", "apple", "papaya"}

# Method 1: intersection()
common = set_a.intersection(set_b)
print(f"Intersection: {common}")  # {'apple'}

# Method 2: & operator
common = set_a & set_b
print(f"Intersection with &: {common}")  # {'apple'}
```

### 3. Difference (Items in First Set Only)
```python
set_a = {"apple", "banana", "cherry"}
set_b = {"pineapple", "apple", "papaya"}

# Method 1: difference()
diff = set_a.difference(set_b)
print(f"Difference: {diff}")  # {'cherry', 'banana'}

# Method 2: - operator
diff = set_a - set_b
print(f"Difference with -: {diff}")  # {'cherry', 'banana'}

# Method 3: difference_update() (modifies original)
set_a.difference_update(set_b)
print(f"After difference_update: {set_a}")  # {'cherry', 'banana'}
```

### 4. Symmetric Difference (Items NOT in Both)
```python
set_a = {"apple", "banana", "cherry"}
set_b = {"pineapple", "apple", "papaya"}

# Method 1: symmetric_difference()
sym_diff = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference: {sym_diff}")
# Output: {'papaya', 'cherry', 'banana', 'pineapple'}

# Method 2: ^ operator
sym_diff = set_a ^ set_b
print(f"Symmetric Difference with ^: {sym_diff}")
```

## Set Methods Reference

| Method | Description | Operator Alternative |
|--------|-------------|---------------------|
| `add(item)` | Add single item | - |
| `update(iterable)` | Add multiple items | - |
| `remove(item)` | Remove item (raises error if not found) | - |
| `discard(item)` | Remove item (no error if not found) | - |
| `pop()` | Remove random item | - |
| `clear()` | Remove all items | - |
| `union(other)` | Combine all items | `\|` |
| `intersection(other)` | Common items only | `&` |
| `difference(other)` | Items in first set only | `-` |
| `symmetric_difference(other)` | Items not in both | `^` |

## Visual Set Operations

```
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}

Union (A ∪ B):           {1, 2, 3, 4, 5, 6}
Intersection (A ∩ B):    {3, 4}
Difference (A - B):      {1, 2}
Symmetric Diff (A △ B):  {1, 2, 5, 6}
```

## When to Use Sets

1. **Remove duplicates** from a list
2. **Membership testing** (very fast)
3. **Mathematical operations** (union, intersection, etc.)
4. **Unique collections** where order doesn't matter

## Common Use Cases

### Remove Duplicates from List
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5]
```

### Fast Membership Testing
```python
valid_users = {"alice", "bob", "charlie"}
user = "alice"

if user in valid_users:  # Very fast operation
    print("Access granted")
```

### Find Common Elements
```python
team_a_skills = {"python", "sql", "excel"}
team_b_skills = {"python", "java", "sql"}

common_skills = team_a_skills & team_b_skills
print(f"Common skills: {common_skills}")  # {'python', 'sql'}
```

## Key Takeaways

1. **Sets eliminate duplicates automatically**
2. **No indexing** - use iteration or membership testing
3. **Unordered** - items may appear in different order each time
4. **Fast membership testing** - much faster than lists for large collections
5. **Mathematical operations** - perfect for set theory operations
6. **Use `discard()` over `remove()`** for safer item removal
7. **Multiple operator shortcuts** available for set operations

## Important Notes

- **True = 1** and **False = 0** in sets (duplicates removed)
- **Cannot access by index** - sets are unordered
- **`pop()` removes random item** - unpredictable in sets
- **Perfect for unique collections** and mathematical set operations

---

**Remember**: Sets are ideal when you need **unique items** and **fast membership testing**, but not when you need **ordered** or **indexed** access to elements!