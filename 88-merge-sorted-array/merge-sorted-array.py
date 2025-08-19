class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return
        l = m-1
        for i in range(n-1,-1,-1):
            while l>=0  and nums2[i] < nums1[l]:
                nums1[l],nums1[l+1+i] = nums1[l+1+i],nums1[l]
                l-=1
            else:
                nums1[l+1+i] = nums2[i]
        l = 0
        
