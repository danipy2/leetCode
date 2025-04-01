class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = [-1 for i in nums]
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                arr[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                arr[stack.pop()] = nums[i]
            if not stack:
                break
        return arr