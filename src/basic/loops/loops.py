"""
Python Loops
Python has two primitive loop commands:

while loops
for loops
"""
"""
1. The while Loop
- With the while loop we can execute a set of statements as long as a condition is true.
"""
print("\n-----------2. Loops -------------")
# Print i as long as i is less than 6:
print("\n-----------2. While Loop -------------\n")
i = 1
while i < 6:
    print(i)
    i += 1
"""
    1
    2
    3
    4
    5
"""
"""
Notes:
- remember to increment i, or else the loop will continue forever.
- The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
"""
"""
The break Statement
- With the break statement we can stop the loop even if the while condition is true:
"""
print("\n-----------2. Break in while Loop -------------\n")
# Exit the loop when i is 3:
print("Break will break the loop when condition met")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
"""
    1
    2
    3
"""
print("\n-----------2. Continue in while Loop -------------\n")
"""
The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:

Example
Continue to the next iteration if i is 3:
"""
print("Continue skip the current iteration and move to next")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    """
    1
    2
    4
    5
    6
  """
print("\n-----------2. Else in while Loop -------------\n")
"""
The else Statement
With the else statement we can run a block of code once when the condition no longer is true:

Example
Print a message once the condition is false:
"""
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

"""
    1
    2
    3
    4
    5
    i is no longer less than 6
"""

print("\n-----------2. For Loop -------------\n")
"""
Python For Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(f"{item} is a fruit")

"""
apple is a fruit
banana is a fruit
cherry is a fruit
"""
print("\n-----------2. For Loop on string -------------\n")
# Loop through string
text = "A for loop is used for iterating over a sequence, like list:"
# Printing the words in str
for word in text.split():
    print(word)

# Split string based on a separator (,)
for word in text.split(","):
    print(word)

# To print characters in string
for char in text:
    print(char)

# Example find first occurrence of for word
for word in text.split():
    if word == "for":
        print("First occurrence of 'for' is found")
        break

print("\n-----------2. For Loop to check word existence-------------\n")
# Example find the occurrence of word along with position in string

words = text.split()
word_positions = {}  # Empty dict to store the position along with word

for index, word in enumerate(words):
    if word not in word_positions:
        word_positions[word] = []
    word_positions[word].append(index)

for word, positions in word_positions.items():
    print(f"'{word}' occurs {len(positions)} times at positions {positions}")

"""
Why we need the if check?
Without the check, the first time we see a new word, word_positions[word] wouldn’t exist yet — and trying to append would cause an error (KeyError).
So the logic ensures:
If word is new → create an empty list first.
Always append the index to that list.
"""
print("\n-----------2. Nested For Loops -------------\n")
# Nested loops

mat = [[1, 2, 3], [4, 5, 6]]

# First loop always traverse the rows
for row in mat:
    print(row)
    """
    [1, 2, 3]
    [4, 5, 6]
    """

# Nested loop
for row in mat:
    for col in row:
        print(col)
"""
1
2
3
4
5
6
"""
