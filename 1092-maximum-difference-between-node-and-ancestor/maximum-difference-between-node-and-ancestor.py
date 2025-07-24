# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(r):
            val = r.val
            change = 0
            maxm,minm = val,val
            if r.left:
                lval ,rval,ch = dfs(r.left)
                change = max(ch,change)
                maxm = max(rval,maxm)
                minm = min(lval,minm)
            if r.right:
                lval ,rval ,ch= dfs(r.right)
                change = max(ch,change)
                maxm = max(rval,maxm)
                minm = min(lval,minm)
            change = max(max(abs(val-maxm),abs(val-minm)),change)
            return [minm,maxm,change]
        if root:
            return dfs(root)[-1]