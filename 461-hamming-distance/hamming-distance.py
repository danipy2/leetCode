class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = max((x.bit_length()),(y.bit_length()))
        d = 0
        for i in range(n):
            j = 1<<i
            if x & (j) != y &j:
                d+=1
        return d
