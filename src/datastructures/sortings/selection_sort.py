"""
Selection Sorting
"""
arr = [12,3,66,4,6]

def selection_sort():
    size = len(arr)

    for i in range(size-1):
        min_index = i
        for j in range(i+1,size):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i] , arr[min_index] = arr[min_index],arr[i]
    print(arr)

selection_sort()

# * Best case: O(n²)
# * WorstCase: O(n²)
# * Space: O(1)

# [3, 4, 6, 12, 66]
