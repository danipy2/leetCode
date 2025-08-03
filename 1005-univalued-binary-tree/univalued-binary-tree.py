# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        s = set()
        def trav(r):
            if not r:
                return 
            s.add(r.val)
            trav(r.left)
            trav(r.right)
        trav(root)
        return len(s)==1
            