class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        arr = [-1] * n
        arr2 = [[] for i in range(n)]
        for i in range(len(times)):
            u,v,w = times[i]
            arr2[u-1].append((w,v))

        
        heap = []
        heapq.heappush(heap,(0,k))
        count = 0
        maxm = -1
        while heap:
            w,m= heapq.heappop(heap)
            if arr[m-1]!=-1:
                continue
            arr[m-1] = w
            count+=1
            maxm = max(maxm,w)
            if count == n:
                return maxm
            
            for i in range(len(arr2[m-1])):
                w1,nod = arr2[m-1][i]
                if arr[nod-1]==-1:
                    heapq.heappush(heap,(w+w1,nod))
        
        return -1