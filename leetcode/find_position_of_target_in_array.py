class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize search limits
        left, right = 0, len(nums)
        # while the difference between limits is positive
        # search for the target position in nums
        while right - left >= 1:
            # the pivot is the middle
            pivot = (left + right) // 2
            # if the number at the pivot position is target we return it
            if nums[pivot] == target:
                return pivot
            # otherwise we reduce the limits depending on the target value
            # if its position is bigger than pivot, the left limit is pivot + 1
            if nums[pivot] < target:
                left = pivot + 1
            # if target's position is smaller than pivot, right limit is pivot
            else:
                right = pivot
            #we repeat this reducing of the limits until the pivot is the target position
        
        # if we don-t find the target we return -1
        return -1
