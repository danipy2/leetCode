class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 1
        contain = nums[0]
        sign = 1
        for i in range(1,len(nums)):
            if (nums[i] -nums[i-1]) * sign < 0 or (count==1 and (nums[i]!= nums[i-1])):
                count+=1
                sign = nums[i] -nums[i-1]
            elif (nums[i] -nums[i-1]) * sign ==0 and nums[i-1]!=nums[i]:
                count+=1
                sign = nums[i] -nums[i-1]  
        return count
