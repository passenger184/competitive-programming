class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            base = r - l
            if height[l] <= height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            print(max_water)    
            max_water = max(max_water, base * h)
        return max_water     
