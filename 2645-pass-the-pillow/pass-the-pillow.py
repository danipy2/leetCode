class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        s = n-1
        x = time%((s)*2)
        if x>s:
            r = x-s
            return n-r
        return x+1