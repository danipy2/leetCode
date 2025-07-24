# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(r,maxm,minm):
            if not r:
                return maxm - minm
            val = r.val
            maxm = max(maxm,val)
            minm = min(minm,val)
            onemax = dfs(r.left,maxm,minm)
            secondmax = dfs(r.right,maxm,minm)
        
            return max(onemax,secondmax)
        return dfs(root,root.val,root.val)