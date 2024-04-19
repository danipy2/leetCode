class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        arr = []
        while(left<=right):
            mid = (left+right) //2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target ):
                arr.append(mid)
                if mid < len(nums)-1:
                    if nums[mid+1] == target:
                        while(mid<len(nums)-1 and nums[mid+1]==target):
                            mid +=1
                        arr.append(mid)
                        return arr
                    else:
                        arr.append(arr[0])
                    return arr
                else:
                    arr.append(arr[0])
                    return arr
            elif nums[mid] >=target:
                right = mid-1
            else:
                left = mid + 1
        return [-1,-1]
        
            