class Solution:
    def punishmentNumber(self, n: int) -> int:
        count = 1
        numb = 2
        found = False
        memo  = {}
        def checkpunishment(num,rem):
            nonlocal found
            nonlocal numb
            nonlocal count
            if found:
                return True
            if num<0:
                return False
            
            if (num,rem) in memo:
                if memo[(num,rem)]:
                    count += numb*numb
                    found = True
                return memo[(num,rem)]
            
            
            if not rem:
                if not num:
                    count += numb*numb
                    found = True
                    return True
                return False
            a = False

            for i in range(len(rem)):
                val = int(rem[:i+1])
                num-= val
                a |=  checkpunishment(num,rem[i+1:])
                num+= val
            memo[(num,rem)] = a
            return a


        for i in range(2,n+1):
            numb = i
            found = False
            checkpunishment(i,str(i*i))
        return count
