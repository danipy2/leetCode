# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(r,pr):
            maxm = 0
            if not r:
                return 0
            if (r,pr) not in memo:
                if pr==1:
                    memo[(r,pr)] = dp(r.left,0) + dp(r.right,0)
                else:
                    l1 = dp(r.left,0)
                    l2 = dp(r.left,1)
                    r1 = dp(r.right,0)
                    r2 = dp(r.right,1) 

                    memo[(r,pr)] = max(l1+r1,l2+r2+r.val)
            return memo[(r,pr)]
        return dp(root,0)