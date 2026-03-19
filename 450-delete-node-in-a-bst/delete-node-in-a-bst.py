# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def indsucc(r):
            while r.left:
                r = r.left
            return r
        def finddelete(r,k):
            if not r:
                return None
            if k < r.val:
                r.left = finddelete(r.left,k)
            elif k > r.val:
                r.right = finddelete(r.right,k)
            else:
                if r.right and r.left:
                    n = indsucc(r.right)
                    r.val = n.val
                    r.right = finddelete(r.right,n.val)
                elif r.right:
                    return r.right
                elif r.left:
                    return r.left
                else:
                    return None
            return r
        return finddelete(root,key)
                
                



