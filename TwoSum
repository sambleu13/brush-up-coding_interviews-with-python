from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            index_i = i
            print("index i first for "+str(i)+", index j first for "+str(i+1)+", number i: "+str(nums[i])+"number j: "+str(nums[i+1]))
            for j in range(i+1, len(nums)):
                index_j = j
                sum_result = nums[i] + nums[j]
                print("index j second for "+str(index_j)+",  and sum result "+str(sum_result))
                if sum_result == target:
                    indexes = [index_i,index_j]
                    return indexes

Sol = Solution ()

Sol.twoSum([3,2,4], 6)
Sol.twoSum([3,2,4], 6)
Sol.twoSum([3,3], 6)
