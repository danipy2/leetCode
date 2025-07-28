# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        count = 0
        def go(root):
            if not root:
                return [0,0]
            nonlocal count
            val1 , total1 = go(root.right) 
            val2 , total2 = go(root.left)
            total = total1+total2 +1
            v = val1+val2 + root.val

            if v//total==root.val:
                count+=1 
            
            return [v,total]
        go(root)
        return count
    
        


        