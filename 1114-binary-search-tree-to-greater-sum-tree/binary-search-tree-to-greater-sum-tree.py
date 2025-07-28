# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def go(r,val=0):
            ans = r.val
            if r.right:
                ans += go(r.right,val)
            r.val = ans
            r.val += val
            if r.left:
                ans += go(r.left,r.val)                        
            return ans 
        go(root,0)
        return root


        