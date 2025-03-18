class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        range_set = {x for x in range(0,len(nums) + 1)}
        missing = list(range_set - nums_set)
        return missing[-1]
