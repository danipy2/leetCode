class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxm = 0
        total = 0
        for i in range(k):
            maxm += cardPoints[i]
        if k==len(cardPoints):
            return maxm
        l = k-1
        r = len(cardPoints)-1
        total = maxm

        while r>=len(cardPoints)-k:
            total += cardPoints[r]-cardPoints[l]
            maxm = max(maxm,total)
            l-=1
            r-=1
        return maxm


