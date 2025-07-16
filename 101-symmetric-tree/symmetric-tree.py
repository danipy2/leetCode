# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr = []
        arr1 = []
        def pre(t,p):
            val = t.val if t else -101
            if p:
                arr.append(val)
            else:
                arr1.append(val)
            if t:
                if p:
                    pre(t.left,p)
                    pre(t.right,p)
                else:
                    pre(t.right,p)
                    pre(t.left,p)
                    
        if root:
            pre(root.left,0)
            pre(root.right,1)
        print(arr,arr1)
        return arr == arr1
    
                