class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ph = {}
        p = [0 for i in nums]
        p[0] = nums[0]
        for i in range(1,len(nums)):
            p[i] = p[i-1] + nums[i]
        count =0
        for i in range(len(p)):
            r = p[i]%k
            if r in ph:
                count += ph[r]
                ph[r] +=1
            else:
                ph[r]=1
            if r == 0:
                count+=1
            print(count,i,r)
        return count
            