class Solution:
    def addDigits(self, num: int) -> int:
        def sums(num):
            prv = 0
            for i in str(num):
                prv+= int(i)
                while len(str(prv)) >1:
                    prv = sums(prv)
            return int(prv)
        
        

        return sums(num)

        