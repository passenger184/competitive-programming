class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        for i in nums:
            rep = 0
            for j in range(len(nums)):
                if i > nums[j]:
                    rep += 1
            count.append(rep) 
        return count 
