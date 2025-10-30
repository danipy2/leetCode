class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = abs(n)
        total = 1
        while num:
            print(num,num&1)
            if num & 1:
                total *= x
            x*=x
            num = num >>1
        if n<0:
            return 1/total
        return total
