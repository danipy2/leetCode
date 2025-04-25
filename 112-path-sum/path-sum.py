# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cond = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(r,total):
            if r:
                total+= r.val
                if r.left:
                    traverse(r.left,total)
                if r.right:
                    traverse(r.right,total)
                if not r.left and not r.right and total==targetSum:
                    self.cond = True
        traverse(root,0)
        return self.cond

                