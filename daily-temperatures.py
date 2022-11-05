class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            answer = [0] * len(temperatures)
            stack = []
            
            for i, v in enumerate(temperatures):
                
                while stack and v > stack[-1][1]:
                    index, value = stack.pop()
                    ind = i - index
                    answer[index] = ind
                
                stack.append((i,v))
            return answer
