class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_set = set(nums)
        if target not in nums_set:
            return -1
        left, right = 0, len(nums)
        while right - left > 1:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot
        return left
