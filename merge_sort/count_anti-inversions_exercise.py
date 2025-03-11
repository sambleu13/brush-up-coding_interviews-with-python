def count_anti_inversions(arr):
    # implement this
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = int(len(arr) / 2)
        left, a = count_anti_inversions(arr[:mid])
        right, b = count_anti_inversions(arr[mid:])
        result, c = merge_count_anti_inversions(left, right)
        return result, (a + b + c)

def merge_count_anti_inversions(x, y):
    # implement this
    result = []
    i = j = count = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            result.append(x[i])
            i += 1
            count += len(y) - j
        else:
            result.append(x[j])
            j += 1
    result += x[i:]
    result += y[j:]
    return result, count

# Testing the function
test_array = [2, 4, 1, 3, 5]
sorted_array, inv_count = count_anti_inversions(test_array)
print(f'Number of anti-inversions in {test_array} is {inv_count}, {sorted_array}')  # Expected Output: 7
