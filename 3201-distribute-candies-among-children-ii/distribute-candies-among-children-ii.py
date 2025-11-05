class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = 0

        for i in range(limit+1):
            rem = n- i
            target = rem 
            lght = 0

            count = limit - ((target+1)//2) +1
            if count <=0:
                continue
            count = min(count,(target+2)//2)
            if count <=0:
                continue
            if rem%2:     
                count = 2* count
            else:
                count  =  2*count -1
            total += count
        return total



        
