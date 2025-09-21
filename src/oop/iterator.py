"""
An iterator is an object in Python that lets you traverse through a sequence (like a list, tuple, string) one element at a time.

Any object with:

__iter__() → returns the iterator object itself.

__next__() → returns the next element. Raises StopIteration when no more items.

"""

a = "SBS"
it = iter(a)
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) StopIteration -- EXCEPTION
"""
S
B
S
StopIteration -- EXCEPTION
"""
print("------------------ Iterator in class ----------------\n")
# Iterator in class
class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index-1
        return self.data[self.index]

rev = Reverse('spam')
it = iter(rev)
for i in it:
    print(i)

print("------------------ Generator ----------------\n")
"""
Generators

A generator is a simpler way to create an iterator.
Instead of writing a whole class with __iter__ and __next__, you use a function with yield.
Each yield pauses the function and saves its state, resuming on the next call.

How a Generator Works

Defined like a normal function, but uses yield instead of return.
Each call to yield pauses the function, saving its state.
When resumed, execution continues from where it stopped.
When no yield is left, it raises StopIteration, just like an iterator
"""
# Reverse with string
def rev(s):
    l = len(s)
    while l>0:
        l -=1
        yield s[l]
for i in rev("ABC"):
    print(f"Yield :: {i}")
"""
Yield :: C
Yield :: B
Yield :: A
"""

def value(n):
    while n>0:
        yield n
        n -=1

for i in value(4):
    print(i)


