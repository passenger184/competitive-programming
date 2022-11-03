class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        half = (len(nums) + 1) // 2
        lis = [0] * len(nums)
        lis[::2] = nums[:half]
        lis[1::2] = nums[half:]
        return lis    
