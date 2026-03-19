# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findlst(r):
            while r.right:
                r = r.right
            return r
        def finddelte(r,k):
            if not r:
                return
            if k> r.val:
                r.right = finddelte(r.right,k)
            elif k<r.val:
                r.left = finddelte(r.left,k)
            else:
                if r.left and r.right:
                    n = findlst(r.left)
                    r.val = n.val
                    r.left = finddelte(r.left,n.val)
                elif r.right:
                    return r.right
                elif r.left:
                    return r.left
                else:
                    return None
            return r
        return finddelte(root,key)
                