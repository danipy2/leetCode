# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def s(r,Gp,p,c):  
            if r:
                if Gp%2 == 0:
                    self.total += r.val
                Gp = p
                p = r.val
                s(r.left,Gp,p,c+1)
                s(r.right,Gp,p,c+1)
        s(root,1,1,2)
        return self.total