class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def countSetBit(n):
            c = 0
            while n > 0:
                c+= 1 & n
                n = n>>1
                
            return c 

        
        c1 = countSetBit(num2)
        c2 = countSetBit(num1)
        
        for i in range(abs(c1-c2)):
            x = num1        
            if c1>c2:
                x +=1
                num1 += x & -x
            else:
                num1 -= x & -x

        return num1