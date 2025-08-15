class Solution:
    def punishmentNumber(self, n: int) -> int:
        count = 1
        numb = 2
        found = False
        def checkpunishment(res,rem):
            nonlocal found
            if found:
                return 
            nonlocal numb
            nonlocal count
            if not rem:
                tot = sum(res)
                if tot ==numb:
                    count += numb*numb
                    found = True
                    return 

            for i in range(len(rem)):
                res.append(int(rem[:i+1]))
                checkpunishment(res,rem[i+1:])
                res.pop()


        for i in range(2,n+1):
            numb = i
            found = False
            checkpunishment([],str(i*i))
        return count
