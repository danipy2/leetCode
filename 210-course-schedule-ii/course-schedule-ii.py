class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        color = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        output = []
        for l,r in prerequisites:
            graph[r].append(l)
        def dfs(n):
            color[n] = 1
            for i in graph[n]:
                if color[i] == 1 or  color[i]==0 and not dfs(i):
                    color[n] = 2
                    return False
            output.append(n)
            color[n] = 2
            return True
        for i in range(len(graph)):
            if color[i] == 0:
                if not dfs(i):
                    return []
        return output[::-1]
        
