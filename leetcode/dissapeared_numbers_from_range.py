class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        range_set = {x for x in range(1,len(nums) + 1)}
        nums_set = set(nums)
        disappeared = range_set - nums_set
        return list(disappeared)
