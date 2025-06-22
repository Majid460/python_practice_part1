# LISTS
"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
list = []

Properties of List:
1. List items are ordered
2. List is a mutable collection
3. Lists can have duplicate items
4. List items can be accessed using the index e.g. list[0]

1.1. ORDERED
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
E.g.
list_a = [1,2,3]
list_a.append(4)
print(list_a) -> [1,2,3,4]

1.2. Changeable (Mutable)
1.2.1. We can add new items in list
1.2.2. We can remove items from list
1.2.3. We can change items in list
1.2.4. We can delete items from list

E.g. list_b = [1,2,3,4]
=> Add new items to list
list_b.append(5)
print(list_b) -> [1,2,3,4,5]

=> Remove items from list
note: list.pop() removes the last item in the list
list_b.pop()
print(list_b) -> [1,2,3,4]
We can provide the position of element to remove
list_b.pop([0]) -> [2,3,4]

=> Change the items in the list
list_c = [1,2,3,4]
list_c[0] = 6
print(list_c) -> [6,2,3,4]

=> Delete items from list
Two ways to delete a item
1. POP
list.pop([i])
 Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
 It raises an IndexError if the list is empty or the index is outside the list range.
2. Remove
list.remove(x)
Remove the first item from the list whose value is equal to x.
It raises a ValueError if there is no such item.

And another way you can delete a item by index
del(list_c[0]) -> it don't return a new list after delete but pop return a list of items.
 The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice)
 Delete a slice of items
 del a[2:4]
 Delete a entire list
 del a[:]
"""
"""
5.1. More on Lists
The list data type has some more methods. Here are all of the methods of list objects:

1. list.append(x)
    Add an item to the end of the list. Similar to a[len(a):] = [x].

2. list.extend(iterable)
    Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.

3. list.insert(i, x)
    Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

4. list.remove(x)
    Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

5. list.pop([i])
    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

6. list.clear()
    Remove all items from the list. Similar to del a[:].

7. list.index(x[, start[, end]])
    Return zero-based index in the list of the first item whose value is equal to x. 
    Raises a ValueError if there is no such item.
   The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

8. list.count(x)
    Return the number of times x appears in the list.

9. list.sort(*, key=None, reverse=False)
   Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

10. list.reverse()
    Reverse the elements of the list in place.

11. list.copy()
    Return a shallow copy of the list. Similar to a[:].
"""