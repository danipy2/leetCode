class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        total = 0
        heap1 = []
        for i in range(len(grid)):
            heap = []
            for j in range(len(grid[i])):
                heapq.heappush(heap,-1 *grid[i][j])
            for m in range(limits[i]):
                heapq.heappush(heap1,heapq.heappop(heap))
        for l in range(k):
            total += heapq.heappop(heap1)
        return total * -1
