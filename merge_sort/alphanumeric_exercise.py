# Import necessary modules
import random
import string

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    # TODO: Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # TODO: implement the merging mechanism here
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
    

# Generate a list of 20 random alphanumeric characters.
random_alphanumeric = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]

print("Original List of random alphanumeric characters:\n", random_alphanumeric)

# Apply merge sort
sorted_alphanumeric = merge_sort(random_alphanumeric)

print("\nSorted List of alphanumeric characters:\n", sorted_alphanumeric)
