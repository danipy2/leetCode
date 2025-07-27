# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def findsum(r,s):
            total = s*10 + r.val
            if not r.right and not r.left:
                return total
            t = 0 
            if r.left:
                t+= findsum(r.left,total)
            if r.right:
                t+= findsum(r.right,total)
            return  t
        return findsum(root,0)
