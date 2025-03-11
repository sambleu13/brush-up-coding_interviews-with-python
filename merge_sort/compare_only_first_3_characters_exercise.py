import random
import string

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    res = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index][:3] < right[right_index][:3]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1

    res.extend(left[left_index:])
    res.extend(right[right_index:])

    return res

# Generate random strings
data = [''.join(random.choices(string.ascii_letters + string.digits, k=6)) for _ in range(20)]

print("\nOriginal list of random strings:")
print(data)

sorted_data = merge_sort(data)

print("\nSorted list of random strings:")
print(sorted_data)
