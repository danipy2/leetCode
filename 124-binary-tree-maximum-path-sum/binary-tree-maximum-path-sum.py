# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float('-inf')
        def dfs(root):
            if not root:
                return 0
            val = root.val
            rval = max(0,dfs(root.right))
            lval = max(0,dfs(root.left))
            self.max = max(self.max,rval+lval+val)
            return val+ max(lval,rval)
        dfs(root)
        return self.max

