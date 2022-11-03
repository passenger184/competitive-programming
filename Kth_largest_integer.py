class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ci = map(int, nums)
        c = sorted(ci, reverse=True)
        x = list(map(str, c))   
        return x[k-1]
