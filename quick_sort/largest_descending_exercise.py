import random

def find_kth_largest(numbers, k):
    if numbers:
        # implement this
        pos = partition(numbers, 0, len(numbers) - 1)
        if len(numbers) - k == pos:
            return numbers[pos]
        elif len(numbers) - k < pos:
            return find_kth_largest(numbers[:pos], k)
        else:
            return find_kth_largest(numbers[pos+1:], k - (len(numbers) - pos))
        
def partition(nums, l, r):
    # implement this
    ran_ind = random.randint(l, r)
    nums[l], nums[ran_ind] = nums[ran_ind], nums[l]
    piv_ind = l
    for i in range(l + 1, r + 1):
        if nums[i] >= nums[l]:
            piv_ind += 1
            nums[piv_ind], nums[i] = nums[i], nums[piv_ind]
    nums[piv_ind], nums[l] = nums[l], nums[piv_ind]
    return piv_ind


print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Expected output: 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected output: 4
