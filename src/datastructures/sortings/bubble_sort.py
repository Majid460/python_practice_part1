
"""
Bubble Sorting
"""
arr = [12,3,66,4,6]

def bubblesort():
    size = len(arr)
    for i in range(size):
        for j in range(size-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

    print(arr)

bubblesort()
# [3, 4, 6, 12, 66]

#  With swapped flag it is optimized
# * Best case: O(n) (if already sorted with swapped flag)
# * Best case: O(n²)
# * WorstCase: O(n²)
# * Space: O(1)

"""
Right Now its Complexity is O(n^2)
"""
# Optimized Form
def bubble_sort_opt():
    siz = len(arr)
    for i in range(siz):
        swapped = False
        for j in range(siz-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break

    print(arr)

bubble_sort_opt()
# [3, 4, 6, 12, 66]