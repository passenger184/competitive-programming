class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = pre = 0
        for pos, spe in sorted(zip(position, speed), reverse=True): 
            tim = (target - pos)/spe 
            if pre < tim: 
                result += 1
                pre = tim
        return result 
