class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        nums = [0 for i in range(n-2)]
        i = 2
        while(i*i<=n):
            if nums[i-2] == 0:
                j = (i-2)+i
                while j<len(nums):
                    nums[j] = 1
                    j+=i
            i+=1
        count = 0
        for i in nums:
            if i==0:
                count+=1
        return count
        


            
        return len(o)