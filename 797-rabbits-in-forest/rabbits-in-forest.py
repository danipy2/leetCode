class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        total = 0
        for n,val in c.items():
            num = n+1
            total += ceil(val/num) * num
        return total
