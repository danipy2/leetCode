class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        group = [-1]*len(graph)
        cond = True
        def dfs(ind,typ):
            nonlocal cond
            if not cond:
                return
            for i in graph[ind]:
                if group[i]==-1:
                    group[i]=typ
                    dfs(i,typ^1)
                else:
                    if group[i] != typ:
                        cond = False
                        return 

        for i in range(len(group)):
            if graph[i] and group[i] ==-1:
                group[i] = 0
                dfs(i,1)
                
                if not cond:
                    return cond
        return cond
        