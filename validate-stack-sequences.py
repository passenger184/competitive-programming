class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        answer = []
        pointer = 0
        for i in pushed:
            answer.append(i)
            while pointer < len(popped) and answer and popped[pointer] == answer[-1]:
                pointer += 1
                answer.pop()
           
        return answer == []        
