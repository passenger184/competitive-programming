class Solution:
    def isValid(self, s: str) -> bool:
        
        opened = ['(', '{', '[']
        closed = [')', '}', ']']
        stack = []

        for i in s:
            if i in closed and stack == []:
                return False 

            if i in opened:
                stack.append(i)

            else:
                if opened.index(stack[-1]) == closed.index(i):
                    stack.pop()
                else:
                    return False
        return stack == []            
            
        
