import random

def find_kth_largest(numbers, k):
    if numbers:
        # implement this
        pi = partition(numbers, 0, len(numbers) - 1)
        print(pi, k-1 , bool(pi == k-1) )
        if pi == k-1:
            return numbers[pi]
        elif k - 1 < pi:
            return find_kth_largest(numbers[pi+1:], len(numbers)-k+1)
        else:
            return find_kth_largest(numbers[:pi], k)
        
def partition(nums, low, high):
    # implement this
    rand_ind = random.randint(low, high)
    ind = low
    nums[low], nums[rand_ind] = nums[rand_ind], nums[low]
    for i in range(low, high):
        if nums[i] >= nums[low]:
            ind += 1
            nums[ind], nums[i] = nums[i], nums[ind]
    nums[ind], nums[low] = nums[low], nums[ind]
    print(ind)
    return ind


print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Expected output: 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected output: 4
