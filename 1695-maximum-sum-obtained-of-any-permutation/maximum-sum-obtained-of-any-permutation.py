class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mydict = {}
        arr = [0] * (len(nums)+1)
        
        for i in range(len(requests)):
            arr[requests[i][0]] += 1
            arr[requests[i][1]+1]-=1
        add = 0
        for i in range(len(arr)):
            arr[i] += add
            add += (arr[i]-add)
        nums.sort(reverse=True)
        arr.sort(reverse=True)
        i = 0
        total = 0
        while i<len(arr) and arr[i]:
            total += arr[i] *nums[i]
            i+=1
        return total%(10**9+7)
        
