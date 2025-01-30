class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        count = 0
        contain = nums[0]
        for i in range(len(nums)):
            if nums[i] == contain :
                count +=1
            else:
                contain = nums[i]
                count = 1
            if count < 3:
                nums[l],nums[i] = nums[i],nums[l]
                l+=1
        return l
            

            


        return 


            
        