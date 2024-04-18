class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        arr = []
        while(left<=right):
            mid = (left+right) //2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target ):
                arr.append(mid)
                break
            elif nums[mid] >=target:
                right = mid-1
            else:
                left = mid + 1
        if len(arr) == 0:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = (left+right) //2
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target  ):
                arr.append(mid)
                break
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid-1
        if len(arr) == 1:
            arr.append(arr[0])
        return arr
        
            