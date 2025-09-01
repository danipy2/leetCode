"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}
        def dfs(nod):
            if nod:
                newNode = Node(nod.val)
                d[nod.val] = newNode
                arr = []
                for n in nod.neighbors:
                    if n.val not in d:
                        arr.append(dfs(n))
                    else:
                        arr.append(d[n.val])
                newNode.neighbors = arr
                return newNode
        return dfs(node)
        
            