class Solution:
    def binaryGap(self, n: int) -> int:
        maxm_dist = 0
        cond = False
        count = 0
        while n>0:
            reminder = n%2
            n = n//2
            count+=1
            if cond and reminder:
                if count >maxm_dist:
                    maxm_dist = count
                count = 0
            elif reminder:
                cond = True
                count = 0
        return maxm_dist