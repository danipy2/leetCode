class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums)-1
        left = right -1  
        while left>=0  and right>left:
            if nums[left] < nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                break
            else:
                if left+1==right:
                    left-=1
                    right = len(nums)-1
                else:
                    right -=1
        right = len(nums)-1
        left+=1
        while(left<right):
            if nums[left]> nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1
            else:
                left+=1
                
        

        