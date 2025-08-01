# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def do(l,r):
            mid = (l+r+1)//2
            n = TreeNode(nums[mid])
            if l==r:
                return n
            if mid-1 >=l:
                n.left= do(l,mid-1)
            if mid+1<=r:
                n.right= do(mid+1,r)
            return n 
        return do(0,len(nums)-1)



