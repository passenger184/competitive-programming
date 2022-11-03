class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j and nums[i] == nums[j]:
                    good_pair += 1
        return good_pair       
                    
