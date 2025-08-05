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
                return -1001
            
            val = root.val
            rval =  dfs(root.right)
            lval = dfs(root.left)
            m = max(lval,rval)
            maxm = max(m,0)+ val
            ans.append(rval+lval+val)
            if rval> maxm or lval>maxm:
                ans.append(max(rval,lval))
            return maxm 
        ans.append(dfs(root))
        return max(ans)

