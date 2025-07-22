# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(r,level):

            if not r.left and not r.right:
                print(r.val)
                return level
            l = 0
            if r.left and r.right:
                l = min(dfs(r.left,level+1),dfs(r.right,level+1))
            elif r.left:
                l = dfs(r.left,level+1)
            else:
                l = dfs(r.right,level+1)
            return l
        if root:
            return dfs(root,1)
        return 0
            
            
