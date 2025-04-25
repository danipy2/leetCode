# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def search(root,val1):    
            if root:
                if root.val == val1:
                    if self.traverse(root,subRoot) == True:
                        return True
                x =  search(root.left,val1)
                y = search(root.right,val1)
                return  x or y 
            return False
        
        return search(root,subRoot.val)
    def traverse(self,r1,r2):  
        if r1 and r2:
            if r1.val != r2.val:
                return False
            return self.traverse(r1.left,r2.left) and self.traverse(r1.right,r2.right)
        elif r1 or r2:
            return False
        else:
            return True
        
    
        