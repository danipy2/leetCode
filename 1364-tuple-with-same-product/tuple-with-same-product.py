class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        s = {}
        count = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p  = nums[i]*nums[j]
                if p not in s:
                    s[p] = 0
                count+= 8 * s[p]
                s[p] += 1
        return count
