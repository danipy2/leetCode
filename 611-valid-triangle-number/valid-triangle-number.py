class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        
        for i in range(len(nums)-1,1,-1):
            l = 0
            r = i-1

            while l<r:
                if nums[i]>= nums[l]+nums[r]:
                    l+=1
                else:
                    total += r-l
                    r -=1
        return total
            

                    

