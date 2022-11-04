class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            stack_1 = []
            st = ''
            if i == ')':
                while st != '(':
                    st = stack.pop()
                    stack_1.append(st)
                stack_1.remove('(')    
                stack.extend(stack_1)    
            else:
                stack.append(i)
                
        return  ''.join(stack).strip('(')               
