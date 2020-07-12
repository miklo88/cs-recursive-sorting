arrA = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# # arr2 = []
# # arr3 = [2]
arrB = [0, 1, 2, 3, 4, 5]

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #combining to make a single array to sort
    # elements = len(arrA) + len(arrB)
    # # print(elements) #returns len of 16
    # merged_arr = [0] * elements
    
    # Your code here
    if len(arrA) == 0:
        return arrB
    # print(arrA)
    if len(arrB) == 0:
        return arrA
    # print(arrB)
    merged_arr = []
    index_left = index_right = 0

    while len(merged_arr) < len(arrA) + len(arrB):
        if arrA[index_left] <= arrB[index_right]:
            merged_arr.append(arrA[index_left])
            index_left += 1

        else:
            merged_arr.append(arrB[index_right])
            index_right += 1

        if index_right == len(arrB):
            merged_arr += arrA[index_left:]
            break

        if index_left == len(arrA):
            merged_arr += arrB[index_right:]
            break
    return merged_arr
# print(merge(arrA,arrB))


# # TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr

    midpoint = len(arr) // 2
    

    return merge(
        arrA = merge_sort(arr[:midpoint]),
        arrB = merge_sort(arr[midpoint:])
    )
    
print(merge_sort(merge(arrA,arrB)))
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

