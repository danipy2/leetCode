class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        right = len(nums)-1
        for i in range(len(nums)):
            targ = target - (nums[i])
            left = i
            while(left<=right):
                mid  = (left+right)//2
                if nums[mid] < targ and (mid == right or nums[mid+1]>=targ):
                    right = mid 
                    count += (mid-i)
                    break
                elif nums[mid] < targ:
                    left = mid +1
                else:
                    right = mid -1
            else:
                break
            
        return count