class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = -10**9
        stack = []

        for n in reversed(nums):
            if n < k:
                return True
            while stack and stack[-1] < n:
                k = stack.pop()
            stack.append(n)
        return False