class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target and (mid==0 or  nums[mid-1] < target):
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid+1
        return len(nums)
                