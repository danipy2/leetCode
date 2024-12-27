class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        myset = set()
        l = 0
        maxm = 0
        total = 0
        i = 0
        while i<len(nums):                
            while i-l+1 <=k:
                if i >= len(nums):
                    return maxm
                while nums[i] in myset:
                    myset.remove(nums[l])
                    total -= nums[l]
                    l+=1
                total += nums[i]
                myset.add(nums[i])
                i+=1
            maxm  = max(total,maxm)
            total -= nums[l]
            myset.remove(nums[l])
            l+=1
        return maxm
            