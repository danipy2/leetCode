class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        t1 = t = l1 = l = 0
        myd1 = {}
        myd= {}
        for i in range(len(nums)):
            myd[nums[i]] = myd.get(nums[i],0) + 1
            while len(myd) >k:
                if myd[nums[l]] == 1:
                    del myd[nums[l]]
                else:
                    myd[nums[l]] -=1
                l+=1
            t += i-l+1
        l1 = 0      
        for i in range(len(nums)):
            myd1[nums[i]] = myd1.get(nums[i],0) + 1
            while len(myd1) >=k and l1<=i:
                if myd1[nums[l1]] == 1:
                    del myd1[nums[l1]]
                else:
                    myd1[nums[l1]] -=1
                l1+=1
            
            t1 += i-l1+1
        return t-t1
        


        
            
        return  