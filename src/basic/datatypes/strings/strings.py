"""
DATA TYPES Continued

STRINGS
A string is a sequence of characters, enclosed in:
"double quotes" or 'single quotes'

1. Strings are part of every language
2. Strings are immutable
3. It has alot of methods

Methods:
1. lower()	"HELLO".lower()	'hello'
2. upper()	"hello".upper()	'HELLO'
3. strip()	" test ".strip()	'test'
4. replace()	"hi".replace("i", "ello")	'hello'
5. split()	"a,b,c".split(",")	['a','b','c']
6. join()	' '.join(['a','b'])	'a b'
7. startswith()	"apple".startswith("a")	True
8. endswith()	"file.txt".endswith(".txt")	True
9. find()	"test".find("s")	2
10. count()	"banana".count("a")	3
"""

# 1. Creating a String
name = "Alice"
multiline = """She is a 
software engineer"""
special_characters_in_strings = "She doesn\'t \n need it"    # Escape character with backslash \

"""
prints:
She doesn't 
 need it
"""
print(special_characters_in_strings)

"""
 A    l    i    c    e
[0]  [1]  [2]  [3]  [4]
     [-4] [-3] [-2] [-1]
     
 l     i     c     e      A     l    i    c    e
[-4]  [-3]  [-2]  [-1]   [0]   [1]  [2]  [3]  [4]
                   - <--- 0 ---> +
     
"""
# 2. Accessing Characters & Slicing
print("# 2. Accessing Characters \n")

print(name[0]) # Prints first character of name

print(name[:2])    #Prints the string from start to 1st index (excludes the 2nd index)
#Prints -> Al

print(name[2:])    # Prints from 2nd index till end
#prints -> ice

print(name[2:3])   #Prints from 2nd index till 2nd (excludes the 3rd)
#prints -> i

print(name[:-1])   #Prints from start to last 0 till second last excludes the last -1 index ( it counts 0,-4,-3,-2)
#prints -> Alic

print(name[1:-1]) # Prints from 1st index till second last
#prints -> lic


"""
sequence[start : stop : step]
Reverse a string
Start from the end and grab every letter one by one until the beginning.

[None:None:-1]
So what does step = -1 mean?
It means:
Move one step backward each time.
i.e., go in reverse order, from right to left.
"""
print(name[::-1])
#print -> ecilA

#3. String Immutability
print("#3. String Immutability\n")
#name[0] = 'E' # Class 'str' does not define '__setitem__', so the '[]' operator cannot be used on its instances
#print(name[0]) #  ❌ Error: 'str' object does not support item assignment
"""
Because:

Strings in Python are immutable, meaning you cannot modify them in-place.
"""
#But you can re-assign the whole new value to it.
# Variable just points to new string

name = "Mlice"
print(name)
# Prints -> Mlice

"""
Note:
After the re-assignment it is pointing to new object in memory and left "Alice" as Garbage.
Alice still exists in memory (until garbage collected), but your variable has moved on
"""

"""
So what if you want to change the character of string
1. We should convert the string into list
2. Then reassign the character to new
"""
name = "Alice"
new_name = list(name)
new_name[0] = 'M'
name = "".join(new_name)
print(name)

#Prints -> Mlice

#4. String Formatting
print("#4. String Formatting \n")
age = 25

# Two ways to format a string
print(f"{name} is {age} old")
print("{0} is {1} old".format(name, age))
print("\n")
#4. String Looping

#1. First option
print("#4. String Looping \n")
for char in name:
    print(char,end=" ")
print("\n")

#2. Second Option (Using list comprehension
[print(x,end= " ") for x in name]

# Prints -> M l i c e
print("\n")

#5. Sub String Checking
print("#4. Sub String Checking \n")
print('t' not in name)
# Prints -> True
print("Al" in name)
# Prints -> False
print("\n")

#6. String Comparisons
print("#6. String Comparisons \n")
a = "Alice"
print(a==name)
# Prints -> False
print(a < name) # Compare based on the alphabetical order
# Prints -> True
print("\n")

#7. String Concatenation
print("#7. String Concatenation \n")
second_name = "Jhon"
print(name,"",second_name)
# Prints -> False

# Prints -> True
print("\n")

# 7. String Methods
"""
1. capitalize()  ->	    Converts the first character to upper case
2. casefold()    ->	    Converts string into lower case
3. center()      ->		Returns a centered string
4. count()  	 ->	    Returns the number of times a specified value occurs in a string
5. encode()      ->		Returns an encoded version of the string
6. endswith()    ->	    Returns true if the string ends with the specified value
7. expandtabs()  ->	    Sets the tab size of the string
8. find()        ->		Searches the string for a specified value and returns the position of where it was found
9. format()      ->		Formats specified values in a string
10. format_map() ->	    Formats specified values in a string
11. index()      ->		Searches the string for a specified value and returns the position of where it was found
12. isalnum()    ->	    Returns True if all characters in the string are alphanumeric
13. isalpha()    ->	    Returns True if all characters in the string are in the alphabet
14. isascii()    ->	    Returns True if all characters in the string are ascii characters
15. isdecimal()  -> 	Returns True if all characters in the string are decimals
16. isdigit()    ->	    Returns True if all characters in the string are digits
17. isidentifier() ->	Returns True if the string is an identifier
18. islower()    ->		Returns True if all characters in the string are lower case
19. isnumeric()  ->		Returns True if all characters in the string are numeric
20. isprintable() ->	Returns True if all characters in the string are printable
21. isspace()    ->		Returns True if all characters in the string are whitespaces
22. istitle()    ->		Returns True if the string follows the rules of a title
23. isupper()    ->		Returns True if all characters in the string are upper case
24. join()       ->	    Joins the elements of an iterable to the end of the string
25. ljust()      ->	    Returns a left justified version of the string
26. lower()      ->		Converts a string into lower case
27. lstrip()     ->		Returns a left trim version of the string
28. maketrans()  ->		Returns a translation table to be used in translations
29. partition()  ->		Returns a tuple where the string is parted into three parts
30. replace()    ->		Returns a string where a specified value is replaced with a specified value
31. rfind()      ->		Searches the string for a specified value and returns the last position of where it was found
32. rindex()     ->		Searches the string for a specified value and returns the last position of where it was found
33. rjust()      ->	    Returns a right justified version of the string
34. rpartition() ->		Returns a tuple where the string is parted into three parts
35. rsplit()     ->		Splits the string at the specified separator, and returns a list
36. rstrip()     ->		Returns a right trim version of the string
37. split()      ->		Splits the string at the specified separator, and returns a list
38. splitlines() ->	    Splits the string at line breaks and returns a list
39. startswith() ->		Returns true if the string starts with the specified value
40. strip()      ->	    Returns a trimmed version of the string
41. swapcase()   ->		Swaps cases, lower case becomes upper case and vice versa
42. title()      ->		Converts the first character of each word to upper case
43. translate()  ->		Returns a translated string
44. upper()      ->		Converts a string into upper case
45. zfill()      ->		Fills the string with a specified number of 0 values at the beginning

"""
# Examples of String Methods
print ("# --------------------Examples of String Methods ------------------")

test_str = "this Is A string"
print (f"Test String for methods = {test_str}")

# 1. capitalize()  ->	    Converts the first character to upper case
print (f" capitalize() on string -> {test_str.capitalize()}",end='\n')
# prints ->  capitalize() on string -> This is a string

# 2. casefold()    ->	    Converts string into lower case
print (f" casefold() on string -> {test_str.casefold()}",end='\n')
# prints ->  casefold() on string -> this is a string

# 3. center()      ->		Returns a centered string (Adds space before and after the string)
print (f" center() on string -> {test_str.center(30)}",end='\n')  # width = 30 means add space after the length of string after and before
# Default character is " ". We can change it to any we want.
print (f" center() on string -> {test_str.center(30,"O")}",end='\n')  # width = 30 means add space after the length of string after and before
# prints ->   center() on string -> OOOOOOOthis Is A stringOOOOOOO

# 4. count()  	 ->	    Returns the number of times a specified value occurs in a string
print (f" count() on string -> {test_str.count("this")}",end='\n')
# prints ->   count() on string -> 1

# 5. encode()  	 ->	    Returns an encoded version of the string
print (f" encode() on string -> {test_str.encode(encoding="ascii",errors="ignore")}",end='\n')
# prints ->   encode() on string -> b'this Is A string'

# 6. endswith()	Returns true if the string ends with the specified value
print (f" endswith() on string -> {test_str.endswith(".")}",end='\n')
# prints ->   endswith() on string -> False
print (f" endswith() on string -> {test_str.endswith("A string")}",end='\n')

# prints ->   endswith() on string -> True
print (f" endswith() on string -> {test_str.endswith(("string","A"))}",end='\n') # Check if the string ends with either the phrase
# prints ->   endswith() on string -> True

# 6. find()   -> Searches the string for a specified value and returns the position of where it was found
print (f" find() on string -> {test_str.find("A")}",end='\n')
# prints -> find() on string -> 8
print(len(test_str))
# prints -> 16
# Where in the text is the first occurrence of the letter "g" when you only search between position 5 and 10?:
print (f" find() on string -> {test_str.find("A",3,10)}",end='\n')
#  find() on string -> 8


# 11. index()  -> Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."

print (f" find() on string -> {txt.index("welcome")}",end='\n')
# prints ->  find() on string -> 7
print (f" find() on string -> {txt.find("q")}",end='\n')
#prints -> find() on string -> -1
#print (f" index() on string -> {txt.index("q")}",end='\n')
# prints -> ValueError: substring not found

# 12. isalnum()  -> Returns True if all characters in the string are alphanumeric
print (f" isalnum() on string -> {txt.isalnum()}",end='\n')
# prints ->  isalnum() on string -> False

# 13. isascii()  -> Returns True if all characters in the string are ascii characters
print (f" isascii() on string -> {txt.isascii()}",end='\n')
# prints ->  isascii() on string -> True

# 14. isdecimal() -> The isdecimal() method returns True if all the characters are decimals (0-9).
print (f" isdecimal() on string -> {txt.isdecimal()}",end='\n')
# prints ->  isdecimal() on string -> False

"""
Use isdigit() when you're okay with any Unicode digit, like ², ٢, exponents etc
"""
print (f" 123.isdecimal() on string -> {"123".isdecimal()}",end='\n')
print (f" ٢٣.isdecimal() on string -> {"٢٣".isdecimal()}",end='\n')
print (f" ²³.isdecimal() on string -> {"²³".isdecimal()}",end='\n')
print (f"  ²³.isdigit() on string -> {"²³".isdigit()}",end='\n')
"""
 123.isdecimal() on string -> True
 ٢٣.isdecimal() on string -> True
 ²³.isdecimal() on string -> False
  ²³.isdigit() on string -> True
"""
# 15. isIdentifier()
"""
The isidentifier() method returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
A valid identifier cannot start with a number, or contain any spaces.
"""
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
"""
1. Prints -> True
2. Prints -> True
3. Prints -> False
4. Prints -> False
"""

# 16. Printable
"""
 What it does:
Checks if all characters in the string are printable.
A string is printable if it doesn't contain non-printable characters like:
Newlines \n
Tabs \t
Backspaces \b

"""
txt = "Hello! Are you #1?"

x = txt.isprintable()

print (f"isPrintable() on string -> {txt.isprintable()}",end='\n')
# Prints -> isPrintable() on string -> True

# 17. Joins
"""
The join() method takes all items in an iterable and joins them into one string.

A string must be specified as the separator.
"""
myTuple = ("John", "Peter", "Vicky")

x = " ".join(myTuple)
print (f"join() on string -> {x}",end='\n')
# prints -> join() on string -> John Peter Vicky

# 18. Strip -> The strip() method removes any leading, and trailing whitespaces.
txt = "  Hello, welcome to my world.   "
print (f"strip() on string -> {txt.strip()}",end='\n')
# prints -> strip() on string -> Hello, welcome to my world.

# translate()
"""
str.maketrans(from, to, delete)
The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

Use the maketrans() method to create a mapping table.

If a character is not specified in the dictionary/table, the character will not be replaced.

If you use a dictionary, you must use ascii codes instead of characters.
"""
txt = "Good night Sam!"
mydict = {
    109: 101,   # 'm' → 'e'
    83: 74,     # 'S' → 'J'
    97: 111,    # 'a' → 'o'
    111: None,  # 'o' → deleted
    100: None,  # 'd' → deleted
    110: None,  # 'n' → deleted
    103: None,  # 'g' → deleted
    104: None,  # 'h' → deleted
    116: None   # 't' → deleted
}
print (f"translate() on string -> {txt.translate(mydict)}",end='\n')
# Prints -> translate() on string -> G i Joe!
