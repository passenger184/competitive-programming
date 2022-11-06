class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def remover(winner, pointer):
            if len(winner) == 1:
                return winner[0]
            else:
                pointer = (pointer + k - 1) % len(winner)
                winner.remove(winner[pointer])
                return remover(winner, pointer)
        
       
        win = remover([i + 1 for i in range(n)], 0)
        return  win
