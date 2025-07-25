# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        count = 0 
        while q:
            temp = []
            temp2 = []
            while q:
                curr = q.popleft()
                if curr.left:
                    temp2.append(curr.left)
                if curr.right:
                    temp2.append(curr.right)
                temp.append(curr.val)
            q = deque(temp2)
            temp2 = []
            if count % 2:
                temp = temp[::-1]
            ans.append(temp)
            count += 1
        return ans
