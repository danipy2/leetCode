# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr1 = []
        self.arr2 = []
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def traverse(root,t=1,p=1):
            if root:
                if t==1:
                    self.arr1.append(p*root.val)
                    traverse(root.left,t)
                    self.arr1.append("aa")
                    traverse(root.right,t,-1)
                else:
                    self.arr2.append(p*root.val)
                    traverse(root.right,t)
                    self.arr2.append("aa")
                    traverse(root.left,t,-1)
        traverse(root.left,1)
        traverse(root.right,2)
        if self.arr1==self.arr2:
            return True
        return False
        
        
