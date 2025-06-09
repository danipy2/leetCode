class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        right = len(nums)-1
        while(l<=right):
            mid = (l+right)//2
            if nums[mid] <= nums[mid-1]:
                return nums[mid]
            elif nums[mid] >= nums[l] and nums[l] >nums[l-1]:
                l = mid + 1
            else:
                right = mid -1