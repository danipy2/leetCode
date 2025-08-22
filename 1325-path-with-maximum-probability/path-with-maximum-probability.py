class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        arr = [[] for i in range(n)]
        visted = [0] * n
        for i in range(len(edges)):
            l,r = edges[i]
            if succProb[i] == 0:   # skip impossible edge
                continue
            arr[l].append((r,-math.log(succProb[i])))
            arr[r].append((l,-math.log(succProb[i])))
        heap = []
        heapq.heappush(heap,(0,start_node))
        while heap:
            prob,node = heapq.heappop(heap)
            if visted[node]:
                continue
            visted[node] = 1
            if node == end_node:
                return math.exp(-prob)
            for n,p in arr[node]:
                if visted[n]==0 and p!=1:
                    heapq.heappush(heap,(p+prob,n))
        return 0