class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        total = 0
        for n,val in c.items():
            # if n == 0:
            #     total += val
            #     continue
            num = n+1
            # total += num
            # if val-1 > n:
            total += (((val-1)//(num)+1)) * num


        return total
