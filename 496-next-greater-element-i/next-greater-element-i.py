class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = defaultdict(lambda:-1)
        for num in nums2:
            while stack and stack[-1] < num:
                res[stack[-1]] = num
                stack.pop()
            stack.append(num)
        ans = []
        for i in nums1:
            ans.append(res[i])
        return ans