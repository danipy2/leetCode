# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(root):
            if not root:
                return [-1001,-1001]
            
            val = root.val
            rval,mright =  dfs(root.right)
            lval,mleft = dfs(root.left)
            m = max(lval,rval)
            maxm = max(m,0)+ val
            max2 = max([m,maxm,mright,mleft,rval+lval+val])
            return [maxm,max2] 
        return max(dfs(root))

