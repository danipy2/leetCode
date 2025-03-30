class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        myd = {0:1}
        count = 0
        nums = accumulate(nums)
        for i in nums:
            if i-k in myd:
                count+=myd[i-k]
            myd[i] = myd.get(i,0)+1
        return count