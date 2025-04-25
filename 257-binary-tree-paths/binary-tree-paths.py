# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: 
        def path(r,s):
            if r:
                s+= f"->{r.val}"
                if r.left:
                    path(r.left,s)
                if r.right:
                    path(r.right,s)
                if not r.right and not r.left:
                    self.output.append(s[2:])
        path(root,"")
        return self.output