# arr = [-5,-3,-2,-1,6,8,9,7,15,55,56,78]
# arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# target = 15
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    
#base case
    while end >= start:
    # if end >= start:
        middle_index = (start + end) // 2

        if arr[middle_index] == target:
            return middle_index
        else:
            if target < arr[middle_index]:
                end = middle_index -1 
            # print(end)
            if target > arr[middle_index]:
                start = middle_index + 1
            # print(arr[middle_index])
            # print(start)
        #if not in the array. -1 is a no-go.
    return -1
    #closing case 
    return middle_index[0] + binary_search(middle_index[1:])
    # return binary_search(middle_index[1:])
    # return binary_search(middle_index)
    # print(middle_index[0])
    # print(middle_index[1:])

# print(binary_search(arr, -9, 0, len(arr)-1))
# print(middle_index[0])
# print(arr[middle_index])

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

