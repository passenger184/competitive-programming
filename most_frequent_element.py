class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        sum, freq = 0, 0
        l = 0
        nums.sort()
        for r in range(len(nums)):
            sum += nums[r]
            while (r - l + 1) * nums[r] > sum + k:
                sum -= nums[l]
                l += 1
            freq = max(freq, (r - l + 1))
            r += 1
        return freq
                
