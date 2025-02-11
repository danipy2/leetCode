class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ph = {0:0}
        p = [0 for i in nums]
        p[0] = nums[0]
        r = p[0]%k
        ph[r]=1
        count = 0
        if r == 0:
            count+=1
        for i in range(1,len(nums)):
            p[i] = p[i-1] + nums[i]
            r = p[i]%k
            if r in ph:
                count += ph[r]
                ph[r] +=1
            else:
                ph[r]=1
            if r == 0:
                count+=1
        return count
            