# Insertion Sort


# Start from second index because it will consider first as sorted and insert in start of array if found
# Brute Force
def insertion_sort():
    arr = [12, 3, 66, 4, 6]
    size = len(arr)
    for i in range(1,size):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i-1,-1,-1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index,current_value)

    print(arr)
# [3, 4, 6, 12, 66]

insertion_sort()

# Optimized Solution
def insertion_sort_opt():
    arr = [12, 3, 66, 4, 6]
    size = len(arr)
    for i in range(1,size):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    print(arr)
# [3, 4, 6, 12, 66]

insertion_sort_opt()