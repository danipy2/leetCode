class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums.sort()
        myd = {}
        total = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p = nums[j] * nums[i]
                if p in myd:
                    myd[p] +=1
                    total += (myd[p]-1)*8
                else:
                    myd[p]=1
        return total

                


