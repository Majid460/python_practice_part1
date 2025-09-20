# Linear Search
# The Linear Search algorithm searches through an array and returns the index of the value it searches for.


def linear_search(element:int):
    arr = [12, 3, 66, 4, 6]
    size = len(arr)
    found = False
    for i in range(size):
        if arr[i] == element:
            print(f"Element found at {i} is {arr[i]}")
            found = True
            break
    if not found:
            print("No element found")

linear_search(66)

# Complexity : O(n)