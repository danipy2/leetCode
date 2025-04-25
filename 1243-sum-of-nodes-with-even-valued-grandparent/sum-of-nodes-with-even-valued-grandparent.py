# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
    
        def s(r,Gp,p):  
            total = 0
            if r:
                if Gp%2 == 0:
                    total += r.val
                Gp = p
                p = r.val
                total += s(r.left,Gp,p)
                total += s(r.right,Gp,p)
            return total 
        return s(root,1,1)