class Solution:
    def isUgly(self, n: int) -> bool:
        while n!=0:
            if n%30==0:
                n=n/30
            elif n%10==0:
                n=n/10
            elif n%6==0:
                n=n/6
            elif n%5==0:
                n=n/5
            elif n%3 ==0:
                n=n/3
            elif n%2==0:
                n=n/2
            else:
                break
        if n==1:
            return True
        return False