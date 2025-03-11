import random
import string

# TODO: Define a merge_sort function that takes data to sort and returns the sorted data
def merge_sort(lst):
    # TODO: If the alphanumeric array has one or no elements, it is already sorted. So, return the array immediately.
    if len(lst) <= 1:
        return lst
    # TODO: Next, divide the array into two equal parts.
    mid = (len(lst)) // 2
    left = lst[:mid]
    right = lst[mid:]
    # TODO: Sort the left and right parts of the array with the merge_sort function.
    left_half = merge_sort(left)
    right_half = merge_sort(right)
    # TODO: After sorting both halves of the array, combine them together using the merge function.
    return merge(left_half, right_half)
    
    
# TODO: In the merge function, take two sorted arrays as inputs
def merge(left, right):
    result = []
    i = j = 0
    # TODO: While both arrays have elements in them, compare the first element of each.
    while i < len(left) and j < len(right):
    # If the first element of the left array is smaller, add it to the result array and remove it from the left array.
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
    # Otherwise, do the same with the right array.
        else:
            result.append(right[j])
            j += 1

    # TODO: If the left or right array still has elements, add them to the result array.
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# TODO: Generate some random data to sort
random_data = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
# TODO: Print the original data
print(f"Unsorted List: {random_data}")
# TODO: Use your merge_sort function to sort the data
sorted_data = merge_sort(random_data)
# TODO: Print the sorted data
print(f"Sorted List: {sorted_data}")
