# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        arr = []
        arr1 = deque()
        while q:
            while q:
                r = q.popleft()
                
                if r and r.left:
                    arr1.append(r)
                    arr.append([r.left,r.left.val])
                    arr.append([r.right,r.right.val])
            while arr1:
                ro = arr1.popleft()
                l ,lval = arr.pop()
                r ,rval = arr.pop()
                if r.left:
                    q.append(l.left)
                    q.append(l.right)
                    q.append(r.left)
                    q.append(r.right)

                ro.left.val ,ro.right.val = lval,rval
        return root

            
