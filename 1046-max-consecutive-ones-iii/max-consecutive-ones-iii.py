class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        maxm = 0
        for i in range(len(nums)):
            count += nums[i]
            if i-l+1-count<=k:
                maxm = max(maxm,i-l+1)
                
            else:
                while nums[l]!=0 :
                    l+=1
                    count-=1
                l+=1
        

        return maxm
