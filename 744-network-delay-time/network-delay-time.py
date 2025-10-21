class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = {node:float("inf") for node in range(1,n+1)}
        d[k] = 0
        graph = {}
        for start,dest,cost in times:
            if start not in graph:
                graph[start] = {}
            graph[start][dest]=cost
        qu = []
        heapq.heappush(qu,(0,k))
        maxm = 0
        while qu:
            cost,curr = heapq.heappop(qu)
            if curr not in graph:
                continue
            for node in graph[curr]:
                cost2 = graph[curr][node]
                val = cost+cost2

                if val < d[node]:
                    d[node] = val
                    heapq.heappush(qu,(val,node))
        for key,value in d.items():
            maxm = max(maxm,value)


        return maxm if maxm!= float(inf) else -1