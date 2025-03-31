class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        maxm = 0
        for i in gain:
            total += i
            maxm = max(maxm,total)
        return maxm