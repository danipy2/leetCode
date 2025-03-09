class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 1
        contain = nums[0]
        sign = 1
        for i in range(1,len(nums)):
            if (nums[i] -contain) * sign < 0 or (count==1 and (nums[i]!= contain)):
                count+=1
                contain = nums[i]
                sign = nums[i] -nums[i-1]
            elif (nums[i] -contain) * sign ==0 and contain!=nums[i]:
                count+=1
                contain = nums[i]
                sign = nums[i] -nums[i-1]
            else:
                if  sign>0:
                    contain = max(nums[i],contain)
                else:
                    contain = min(nums[i],contain)   
        return count
