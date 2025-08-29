class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visted = set()
        heap = []
        heapq.heappush(heap,(0,0))
        total = 0
        while heap:
            w,n = heapq.heappop(heap)
            cx,cy = points[n]
            if n in visted:
                continue
            visted.add(n)
            total+=w
            for i in range(len(points)):
                if i in visted:
                    continue
                x,y  = points[i]
                dis = abs(x-cx) + abs(y-cy)
                heapq.heappush(heap,(dis,i))
        return total