arrA = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

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
    print(arrB)
    if len(arrB) == 0:
        return arrA
    print(arrA)
    #where the merging magic happens. but its not sorted out.
    merged_arr = []
    index_left = index_right = 0
    # print(index_left)
    # print(index_right)
    while len(merged_arr) < len(arrA) + len(arrB):
        #now your looping over the arr and sorting it by element. hence [] 
        if arrA[index_left] <= arrB[index_right]:
            merged_arr.append(arrA[index_left])
            index_left += 1

        else:
            merged_arr.append(arrB[index_right])
            index_right += 1
#if one arr is larger than the other you can break the loop and re-sort.
        if index_right == len(arrB):
            merged_arr += arrA[index_left:]
            break

        if index_left == len(arrA):
            merged_arr += arrB[index_right:]
            break
    return merged_arr
    #returns the merged arrays
print(merge(arrA,arrB))


# # TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #base case - if the input array contains fewer than two elements,
    #then return it as the result of the function
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

