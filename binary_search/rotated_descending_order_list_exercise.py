def search_dec_rotated(nums, target):
    left, right = 0, len(nums) - 1
    if len(nums) >= 1 and target in nums:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # implement this
            #left
            if nums[left] >= nums[mid] and (nums[left] >= target > nums[mid]):
                right = mid - 1
            #right
            elif nums[mid] >= nums[right] and (nums[mid] > target >= nums[right]):
                left = mid + 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid - 1
        return -1
    else:
        return -1


print(search_dec_rotated([4, 3, 2, 1, 8, 7, 6, 5], 1))  # Expected output: 3
print(search_dec_rotated([9, 8, 7, 6, 5, 4, 3, 2, 1], 4))  # Expected output: 5
print(search_dec_rotated([5, 4, 3, 2, 1], 8))  # Expected output: -1
