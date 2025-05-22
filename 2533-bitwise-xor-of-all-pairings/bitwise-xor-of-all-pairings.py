class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x = 0
        if len(nums2) & 1:
            for i in nums1:
                x = x^i
        if len(nums1) & 1:
            for i in nums2:
                x = x^i
        return x