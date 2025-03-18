class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        majority = None
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
            if frequency[i] > len(nums) / 2:
                majority = i
        return majority   
            
