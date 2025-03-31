class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        nums = [0] + nums
        nums = list(accumulate(nums))
        l1 = 0
        minm = 100000
        for i in range(1,len(nums)):
            for j in range(i+l-1,min(len(nums),i+r)):
                if nums[j]-nums[i-1] >0:
                    minm = min(minm,nums[j]-nums[i-1])
        return minm if minm!= 100000 else -1
        
            

                
        