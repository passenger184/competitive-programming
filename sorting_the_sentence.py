class Solution:
    def sortSentence(self, s: str) -> str:
        str_arr = s.split(' ')
        sor = [''] * len(str_arr)
        for i in str_arr:
            last = int( i[-1]) - 1
            word = i.strip(i[-1])
            sor[last] = word
        return ' '.join(sor)
