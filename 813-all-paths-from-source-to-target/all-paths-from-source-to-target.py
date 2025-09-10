class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        a = [0]
        def dfs(ind):
            if ind == len(graph)-1:
                ans.append(a.copy())
                return
            for i in graph[ind]:
                a.append(i)
                dfs(i)
                a.pop()

        dfs(0)
        return ans
            