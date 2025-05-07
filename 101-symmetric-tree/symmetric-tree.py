# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def traverse(root,n,e):
            
            if root:
                if e==1:
                    arr1.append(root.val)
                else:
                    arr2.append(root.val)
                if n%2:
                    traverse(root.right,n+1,e)
                    traverse(root.left,n+1,e)
                else:
                    traverse(root.left,n+1,e)
                    traverse(root.right,n+1,e)
            else:
                if e==1:
                    arr1.append(None)
                else:
                    arr2.append(None)
        traverse(root.right,0,1)
        traverse(root.left,1,2)
        if arr1 == arr2:
            return True
        return False
            