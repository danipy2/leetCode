class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr = [0 for i in range(len(nums)+1)]
        for left,right in queries:
            arr[left] += 1 
            arr[right+1] -= 1
        curr = 0
        for i in range(len(nums)):
            curr += arr[i]
            if nums[i] > curr:
                return False
        return True