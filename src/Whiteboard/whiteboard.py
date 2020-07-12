# # Recursion practice.
# # counting down from n
# def print_to_zero(n):
#     if n < 0: 
#         return 
#     print(n)
#     #if not
#     return print_to_zero(n - 1) #calling the fn and decrementing
# print(print_to_zero(5))

# #counting up to n
# def print_to_n(n):
#     if n > 15: #base case. once it hits 15 it stops printing.
#         return
#     print(n)
#     #if not
#     return print_to_n(n + 1)
# print(print_to_n(0))

#merge sort
##MERGING
# # the goal here is to divide an array down by half until one element remains.
a = [7,14,6,8,12,15,2,20]
b = [17,4,16,18,2,5,12,2]
# def merge(left, right):
def merge(left, right):
    
    
     #going to need two places to store the array. left and right
    # if len(left) == 0:
    #     return right
    if len(left) == 0:
        return right
    print(left)
    #if nothing in the second array then return left
    if len(right) == 0:
        return left
    print(right)
    result = []
    index_left = index_right = 0

    #now go throught both arrays until all the elements make it into the resultant array
    while len(result) < len(left) + len(right):
        #the elements need to be sorted to add them to the
        #resultant array, so you need to decide whiter to get
        #the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
            # print(left)
            # print(index_left)
        else:
            result.append(right[index_right])
            index_right += 1
            # print(right)
            # print(index_right)
   
    #if you reach the end of either array then you can add the remaining elements from the other array to 
    #the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
    return result
# print(merge(a,b))

# merge_sort(arr)

# #merge sort
def merge_sort(array):
    if len(array) < 2:
        return array
    
    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])
    )

array = [17,4,16,18,2,5,12,2]
# print(merge_sort(a,b))
print(merge_sort(array))