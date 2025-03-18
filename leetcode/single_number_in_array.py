class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set()
        for i in nums:
            if i not in nums_set:
                nums_set.add(i) # add number to the set when it appears the first time
            else:
                nums_set.remove(i) # remove from set when it appears the second time
        return list(nums_set)[0] # return the single number at positioin 0 of the array
