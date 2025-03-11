import string
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_half = merge_sort(left)
    right_half = merge_sort(right)

    return merge(left_half, right_half)


def merge(left, right):
    res = []
    left_index, right_index = (0, 0)

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1

    # If we reach the end of either array, append the leftover elements from the other array
    if left:
        res.extend(left[left_index:])
    if right:
        res.extend(right[right_index:])

    return res

# Generate a list of 20 random lowercase alphabets
random_alphabets = [random.choice(string.ascii_lowercase) for _ in range(20)]

print("Original List: \n", random_alphabets)

# Apply merge sort
sorted_alphabets = merge_sort(random_alphabets)

print("\nSorted List: \n", sorted_alphabets)
