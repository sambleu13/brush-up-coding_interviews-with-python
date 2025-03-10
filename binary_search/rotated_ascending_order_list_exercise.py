def search_dec_rotated(nums, target):
    left, right = 0, len(nums) - 1
    if len(nums) >= 1 and target in nums:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # implement this
            if nums[left] <= nums[mid] and (nums[left] < target < nums[mid]):
                right = mid - 1
            elif nums[mid] <= nums[right] and (nums[mid] < target < nums[right]):
                left = mid + 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: 
                right = mid - 1
        return -1
    else:
        return -1


print(search_dec_rotated([5,6,7,8,1,2], 1))  # Expected output: 4
print(search_dec_rotated([5, 1, 3, 4], 2))  # Expected output: -1
