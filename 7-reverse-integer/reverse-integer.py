class Solution:
    def reverse(self, x: int) -> int:
        mod = 2**31
        a = str(x)
        if x<0:
            y = a[1:]
            x = "-"+ y[::-1]
            y = int(x)
            if y < -mod:
                return 0
        else:
            y = int(a[::-1])
            if y>2**31:
                return 0
        return y
        