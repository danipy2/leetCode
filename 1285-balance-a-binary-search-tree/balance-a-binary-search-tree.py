# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(r):
            if not r:
                return 
            inorder(r.left)
            arr.append(r.val)
            inorder(r.right)
        def do(l,r):
            mid = (l+r+1)//2
            n = TreeNode(arr[mid])
            if l==r:
                return n
            if l<=mid-1:
                n.left = do(l,mid-1)
            if r >=mid+1:
                n.right = do(mid+1,r)
            return n
        inorder(root)
        return do(0,len(arr)-1)
