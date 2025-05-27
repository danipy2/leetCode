class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for i in range(n)]

        visted = set()
        for first , second in edges:
            g[second].append(first)
            g[first ].append(second)
        found = False
        def dfs(current,destination):
            nonlocal found
            if current in visted or found:
                return 
            if current == destination:
                found = True
                return 
            visted.add(current)
            for node in g[current]:
                dfs(node,destination)
        dfs(source,destination)
        return found
        