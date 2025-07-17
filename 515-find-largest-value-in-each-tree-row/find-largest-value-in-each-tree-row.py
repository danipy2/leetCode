# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        arr = []
        n = len(q)
        while q:
            maxm = -inf
            for _ in range(n):
                cur = q.popleft()
                maxm = max(maxm,cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            arr.append(maxm)
            n = len(q)
        return arr

                


