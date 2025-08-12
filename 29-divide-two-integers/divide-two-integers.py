class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        powr = 1
        count = 0
        di = abs(divisor)
        m = abs(divisor)
        d = abs(dividend)
        n =  0
        while True:
            while n+m <= d:
                powr = powr << 1
                m  = m<<1
            n += m>>1
            count += powr>>1
            
            if m == di:
                break
            powr = 1
            m = di
        if dividend*divisor <0:
            return max(-count,-2**31)
        return min(count,2**31-1)