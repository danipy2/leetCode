class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = [-1 for i in nums]
        stack = []
        for i in range(2*len(nums)-1 ,-1 ,-1):
            curr =  nums[i%len(nums)]
            while stack and stack[-1] <= curr:
                stack.pop()
            if stack and  i<len(nums):
                arr[i] = stack[-1]
            stack.append(curr)
        return arr
