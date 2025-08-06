# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        def issame(n1,n2):
            if not self.same:
               return 
            if not(n1 and n2):
                if n1 or  n2:
                    self.same = False
                return 
            if (n1.val!= n2.val):
                self.same = False
                return 
            
            issame(n1.left,n2.left)
            issame(n1.right,n2.right)
        issame(p,q)
        return self.same

