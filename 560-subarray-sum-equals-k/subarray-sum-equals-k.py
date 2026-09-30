class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict = {0:1}
        count = 0
        nums = accumulate(nums)
        for i in nums:
            if i-k in mydict:
                count += mydict[i-k]
            mydict[i] = mydict.get(i,0)+1
        return count 
