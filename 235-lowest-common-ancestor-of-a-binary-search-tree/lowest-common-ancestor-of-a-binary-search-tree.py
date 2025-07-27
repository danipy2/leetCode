# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        myset = set()
        ans = [-1]
        Found = False
        def godeep(r,val):
            nonlocal Found 
            an = False
            if not r or Found :
                return False
            if r.val == val:
                
                Found = True
                if val in myset:
                    ans[0] = r
                    return False
                myset.add(val)
                return True
            if r.left:
                an |= godeep(r.left,val)
            if r.right:
                an |= godeep(r.right,val)
            if an:
                if r.val in myset:
                    ans[0] = r
                    Found = True
                    return False
                myset.add(r.val)
                return True
            return False
        
        godeep(root,p.val)
        print(myset)
        Found = False
        godeep(root,q.val)
        return ans[0]

                