# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([[root,1]])
        while q:
            curr , level = q.popleft()
            if not curr.left and not curr.right:
                return level
            if curr.left:
                q.append([curr.left,level+1])
            if curr.right:
                q.append([curr.right,level+1])
            
            
