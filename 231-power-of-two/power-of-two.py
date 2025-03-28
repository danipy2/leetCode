class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.check(2,n)
    def check(self,z,x):
        if x == 1:
            return True
        if  x>z:
            boo = self.check(z*2,x)
            return boo
        elif z>x:
            return False
        else:
            return True