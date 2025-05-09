class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0 for i in range(len(graph))]
        safe = [1 for i in range(len(graph))]
        def dfs(n):
            color[n] = 1
            for i in graph[n]:
                if color[i] == 1 or color[i] == 0 and dfs(i):
                    safe[i] = 0
                    return True
            color[n] = 2
            return False
        for i in range(len(graph)):
            if color[i] == 0 and dfs(i):
                safe[i] = 0
        return [ i for i in range(len(safe)) if safe[i] == 1]
        return sorted(arr) 