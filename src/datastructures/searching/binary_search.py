# Binary Search

# It requires sorting array
"""
How it works:

Check the value in the center of the array.
If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
If the value is found, return the target value index. If the target value is not found, return -1.


- To start with, the algorithm has two variables "left" and "right".

"left" is 0 and represents the index of the first value in the array, and "right" is 6 and represents the index of the last value in the array.
"""


def binary_search(array, target_value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2  # the floor division // rounds the result down to the nearest whole number
        if array[mid] == target_value:
            return mid
        if array[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble_sort(array: list[int]) -> list[int]:
    size = len(array)
    for i in range(size):
        swapped = False
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array

"""
Each time Binary Search checks a new value to see if it is the target value, the search area is halved.
Complexity -> O(log2n) 
"""

if __name__ == '__main__':
    array_ = [12, 3, 66, 4, 6]
    arr_1 = bubble_sort(array_)
    print(arr_1)
    target = 12
    result = binary_search(arr_1, target)
    print(result)
    if result != -1:
        print("Value", target, "found at index", result)
    else:
        print("Target not found in array.")
