class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        found = False
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                ind = i-1
                found = True
                break
        l = ind+1
        r = len(nums)-1
        
        if found:
            ind2 = 0 
            maxm = 101
            for i in range(l,len(nums)):
                if nums[i] > nums[l] and nums[i] <= maxm:
                    ind2 = i
                    maxm = nums[ind2]
            nums[l],nums[ind2] = nums[ind2],nums[l]
            l+=1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            r-=1
            l+=1