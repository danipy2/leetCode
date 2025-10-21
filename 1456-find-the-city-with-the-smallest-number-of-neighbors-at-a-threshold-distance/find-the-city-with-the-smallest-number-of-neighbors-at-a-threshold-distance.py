class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [{} for i in range(n)]
        pq = []


        for s, e, w in edges:
            adj[s][e] = w
            adj[e][s] = w

   
        res = -1
        min_ = float("inf")
        for i in range(n):
            
            dis = [distanceThreshold + 1] * n
            dis[i] = 0
            heapq.heappush(pq,(0, i))

            while pq:
                dist, parent = heapq.heappop(pq)

                for node , w in adj[parent].items():
                    distance = dist + w 
                    if distance < dis[node]:
                        dis[node] = distance
                        heapq.heappush(pq, (distance, node))

            count = dis.count(distanceThreshold + 1)
            count = n - count - 1
            if count <= min_:
                res = i
                min_ = count
            
        
        return res
