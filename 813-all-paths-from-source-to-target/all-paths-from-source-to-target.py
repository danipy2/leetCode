class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(ind,a):
            if ind == len(graph)-1:
                ans.append(a.copy())
                return
            for i in graph[ind]:
                a.append(i)
                dfs(i,a)
                a.pop()

        dfs(0,[0])
        return ans
            