class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ord = sorted(nums)
        indices_target = []
        for i in range(len(ord)):
            if ord[i] == target:
                indices_target.append(i)
        return indices_target        
                
                
