class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            j = nums2.index(i)
            if (j == len(nums2) - 1):
                ans.append(-1)
            else:
                p = 0
                for k in nums2[j+1:]:
                    if k > nums2[j]:
                        ans.append(k)
                        break
                    else:        
                        p +=1
                if p == len(nums2[j+1:]):
                    ans.append(-1)  
        return ans                    
                    
                    
