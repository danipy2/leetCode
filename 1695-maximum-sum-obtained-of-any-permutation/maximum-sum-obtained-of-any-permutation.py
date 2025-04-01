class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0 for i in range(len(nums)+1)]
        for left,right in requests:
            arr[left]+=1
            arr[right+1]-=1
        arr  = list(accumulate(arr))
        nums.sort(reverse=True)
        arr.sort(reverse=True)
        total = 0
        for multi,value in zip(arr,nums):
            if multi==0:
                return total%(10**9+7)
            total += multi*value
        return total%(10**9+7)