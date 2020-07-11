arrA = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr2 = []
# arr3 = [2]
arrB = [0, 1, 2, 3, 4, 5]

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #combining to make a single array to sort
    elements = len(arrA) + len(arrB)
    # print(elements) #returns len of 16
    merged_arr = [0] * elements
    
    # Your code here


    return merged_arr
    
print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

