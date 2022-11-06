class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        u = ''
        x = ''
        for i in s:
            if i == ']':
                while stack[-1] != '[':
                    u = stack.pop() + u
                stack.pop()    
                while stack and stack[-1].isnumeric():
                    x = stack.pop() + x 
                if x:
                    x = int(x)    
                    u = u * x
                    x = ''
                stack.append(u)
                u = ''
            else:
                stack.append(i) 
        return ''.join(stack)    
