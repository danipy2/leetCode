# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        false = False
        def checkvalid(root):
            nonlocal false
            val = root.val
            lval = root.val
            rval = root.val
            if root.right and not false:
                rmin , rmax = checkvalid(root.right)
                if rmin <= val:
                    false = True
                lval = min(lval,rmin)
                rval = max(rval,rmax)
                
            if root.left and not false:
                lmin , lmax = checkvalid(root.left)
                if lmax >= val:
                    false = True
                lval = min(lval,lmin)
                rval = max(rval,lmax)
            return [lval,rval]
        if root:
            checkvalid(root)
        return not false

            