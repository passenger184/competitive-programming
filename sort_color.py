class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        for i in range(len(nums)):
            if nums[temp] == 0:
                nums.pop(temp)
                nums.insert(0,0)
                temp += 1
            elif nums[temp] == 2:
                nums.pop(temp)
                nums.append(2)
            else:
                temp += 1
