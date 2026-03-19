# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findlst(r):
            while r.left:
                r = r.left
            return r
        def finddelte(r,k):
            if not r:
                return
            if k> r.val:
                r.right = finddelte(r.right,k)
            elif k<r.val:
                r.left = finddelte(r.left,k)
            else: 
                if not r.right:
                    return r.left
                if not r.left:
                    return r.right
                n = findlst(r.right)
                r.val = n.val
                r.right = finddelte(r.right,n.val)
            return r
        return finddelte(root,key)
                