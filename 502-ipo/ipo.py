class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        mergarr = []
        for i in range(len(profits)):
            mergarr.append([capital[i],profits[i]])
        heap = []
        i = 0
        mergarr.sort(key=lambda x:x[0])
        while i<len(mergarr) and k:
            if mergarr[i][0] <=w:
                heapq.heappush(heap,-1*mergarr[i][1])
                i+=1
            else:
                if heap:
                    w-= heapq.heappop(heap)
                    k-=1
                else:
                    break
        while k>0 and heap:
            w-= heapq.heappop(heap)
            k-=1
        return w

