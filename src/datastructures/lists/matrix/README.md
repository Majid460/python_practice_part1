# Matrix Operations in Python

A comprehensive collection of Python examples demonstrating common matrix operations and algorithms. This repository contains practical implementations for working with 2D arrays (matrices) in Python.

## Table of Contents

- [Overview](#overview)
- [Examples Included](#examples-included)
- [Getting Started](#getting-started)
- [Code Examples](#code-examples)
- [Example Outputs](#example-outputs)
- [Key Concepts](#key-concepts)
- [Contributing](#contributing)

## Overview

This project demonstrates various matrix operations commonly used in programming interviews, data analysis, and algorithm development. Each example includes multiple solution approaches, from basic loops to advanced list comprehensions.

## Examples Included

### 1. Count Element Occurrences
Count how many times each number appears in a matrix.

**Features:**
- Dictionary-based counting
- List comprehension approach
- Efficient element tracking

### 2. Sum of All Elements
Calculate the total sum of all numbers in a 2D array.

**Methods:**
- Nested loop approach
- List comprehension with `sum()`

### 3. Row Sum Calculation
Print the sum of elements in each row.

**Output Format:**
```
Sum of Row 0 = 6
Sum of Row 1 = 15
Sum of Row 2 = 24
```

### 4. Column Sum Calculation
Calculate and display the sum of elements in each column.

**Algorithm:**
- Iterate through column indices
- Sum elements from the same column across all rows

### 5. Find Maximum and Minimum
Identify the largest and smallest elements in the matrix.

**Approach:**
- Initialize with first element
- Compare with all other elements
- Track both max and min simultaneously

### 6. Even/Odd Number Analysis
Count and categorize numbers as even or odd.

**Features:**
- Separate counters for even/odd numbers
- Lists to store actual even/odd values
- Modulo operation for classification

### 7. Matrix Transpose (Advanced)
Convert rows to columns and vice versa.

**Two Solutions:**
1. **Nested Loops:** Traditional approach with explicit row/column creation
2. **List Comprehension:** Pythonic one-liner solution

## Code Examples

### 1. Count Element Occurrences

```python
# Solution 1: Using Dictionary
matrix_two = [
    [1, 2, 3],
    [4, 5, 2],
    [5, 8, 3]
]

count = {}
for row in matrix_two:
    for element in row:
        if element not in count:
            count[element] = 1
        else:
            count[element] += 1

print("Occurrences of elements in matrix:")
for key, val in count.items():
    print(f"{key} → {val}")
```

```python
# Solution 2: Using List Comprehension
list_comp = [item for row in matrix_two for item in row]
count = {}
for element in list_comp:
    count[element] = count.get(element, 0) + 1
```

### 2. Sum of All Elements

```python
# Method 1: Nested loops
sum_of_elements = 0
for row in matrix:
    for element in row:
        sum_of_elements += element

print(f"The sum of all elements: {sum_of_elements}")
```

```python
# Method 2: List comprehension
sum_of_elements = sum([item for row in matrix for item in row])
print(f"The sum using comprehension: {sum_of_elements}")
```

### 3. Row Sum Calculation

```python
for i, row in enumerate(matrix):
    row_sum = sum(row)
    print(f"Sum of Row {i} = {row_sum}")
```

### 4. Column Sum Calculation

```python
num_col = len(matrix_two[0])

for col in range(num_col):
    total_sum = 0
    for row in matrix_two:
        total_sum += row[col]
    print(f"Sum of Column {col} = {total_sum}")
```

### 5. Find Maximum and Minimum

```python
max_element = matrix_two[0][0]
min_element = matrix_two[0][0]

for row in matrix_two:
    for element in row:
        if element > max_element:
            max_element = element
        if element < min_element:
            min_element = element

print(f"Max element: {max_element}")
print(f"Min element: {min_element}")
```

### 6. Even/Odd Number Analysis

```python
even_odd_dict = {"even": 0, "odd": 0}
even_numbers = []
odd_numbers = []

for row in matrix_two:
    for element in row:
        if element % 2 == 0:
            even_odd_dict["even"] += 1
            even_numbers.append(element)
        elif element % 2 == 1:
            even_odd_dict["odd"] += 1
            odd_numbers.append(element)

print(f"Number of Even elements: {even_odd_dict['even']}")
print(f"Number of Odd elements: {even_odd_dict['odd']}")
print(f"Even elements: {even_numbers}")
print(f"Odd elements: {odd_numbers}")
```

### 7. Matrix Transpose

```python
# Solution 1: Using nested loops
transpose_matrix = []
rows = len(matrix_two)
cols = len(matrix_two[0])

for col in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix_two[i][col])
    transpose_matrix.append(new_row)

print("Transpose of matrix:")
for row in transpose_matrix:
    print(row)
```

```python
# Solution 2: Using list comprehension
transpose_matrix = [[matrix_two[i][j] for i in range(rows)] 
                   for j in range(len(matrix_two[0]))]
print("Transpose of matrix:")
for row in transpose_matrix:
    print(row)
```

## Getting Started

### Prerequisites
- Python 3.x
- No external libraries required

### Running the Code

1. Clone or download the code file
2. Run the Python script:
```bash
python matrix_operations.py
```

### Sample Matrix Used
```python
matrix_two = [
    [1, 2, 3],
    [4, 5, 2],
    [5, 8, 3]
]
```

## Example Outputs

### Element Occurrence Count
```
Occurrences of elements in matrix:
1 → 1
2 → 2
3 → 2
4 → 1
5 → 2
8 → 1
```

### Matrix Transpose
**Original Matrix:**
```
[1, 2, 3]
[4, 5, 2]
[5, 8, 3]
```

**Transposed Matrix:**
```
[1, 4, 5]
[2, 5, 8]
[3, 2, 3]
```

### Even/Odd Analysis
```
Number of Even elements: 4
Number of Odd elements: 5
Even elements: [2, 4, 2, 8]
Odd elements: [1, 3, 5, 5, 3]
```

## Key Concepts

### Data Structures Used
- **2D Lists:** For matrix representation
- **Dictionaries:** For counting and key-value storage
- **Lists:** For collecting specific elements

### Programming Techniques
- **Nested Loops:** For matrix traversal
- **List Comprehensions:** For concise, Pythonic solutions
- **Enumerate:** For index tracking
- **Dictionary Methods:** `.get()` for safe key access

### Algorithm Patterns
- **Matrix Traversal:** Row-by-row and column-by-column access
- **Element Counting:** Using dictionaries as counters
- **Matrix Transformation:** Transpose operation
- **Aggregation:** Sum, max, min operations

### Code Structure

Each example follows this pattern:
1. **Problem Statement:** Clear description of the task
2. **Algorithm Explanation:** Step-by-step approach
3. **Implementation:** Working code with comments
4. **Alternative Solutions:** Different approaches when applicable
5. **Sample Output:** Expected results

### Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Element Count | O(m×n) | O(k) where k = unique elements |
| Sum All Elements | O(m×n) | O(1) |
| Row/Column Sums | O(m×n) | O(1) |
| Find Max/Min | O(m×n) | O(1) |
| Matrix Transpose | O(m×n) | O(m×n) |

Where m = number of rows, n = number of columns

### Learning Objectives

After studying this code, you'll understand:
- Matrix manipulation fundamentals
- Dictionary usage for counting
- List comprehension patterns
- Nested loop structures
- Matrix transpose algorithms
- Python best practices for 2D data

### Customization

You can easily modify the examples by:
- Changing the sample matrix values
- Adding new matrix operations
- Implementing different algorithms
- Extending to larger matrices

### Notes

- All solutions handle rectangular matrices (equal row lengths)
- Dictionary approach is efficient for sparse counting
- List comprehensions provide more Pythonic solutions
- Examples include both basic and advanced implementations

### Contributing

Feel free to:
- Add new matrix operations
- Optimize existing solutions
- Improve documentation
- Add error handling
- Extend to 3D arrays

---
