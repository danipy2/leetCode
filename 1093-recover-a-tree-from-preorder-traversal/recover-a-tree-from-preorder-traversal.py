# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        traversal = traversal.split("-")
        root = TreeNode(int(traversal[0]))
        print(traversal)
        a = [[root]]
        s = ""
        count = 1 
        for i in range(1,len(traversal)):
            if not traversal[i]:
                count+=1
                continue
            else:
                val = int(traversal[i])
                newnode = TreeNode(val)
                parent = a[count-1][-1]
                if parent.left:
                    parent.right = newnode
                    if len(a) >count:
                        a[count].append(newnode)
                    else:
                        a.append([newnode])
                else:
                    parent.left = newnode
                    if len(a) >count:
                        a[count].append(newnode)
                    else:
                        a.append([newnode])
                count = 1
                
        
        
        return root
        
            