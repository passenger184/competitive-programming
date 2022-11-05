class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num) - k
        stack = []
        if k == len(num):
            return '0'
        for i in num:
            while stack and i < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(i)
                
        return str(int(''.join(stack[:n])))
