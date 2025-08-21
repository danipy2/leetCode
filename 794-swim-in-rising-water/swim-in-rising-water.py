class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        arr = [-1] *(n*n)
        heap = []
        heapq.heappush(heap,(grid[0][0],(0,0)))
        dirc = [(1,0),(0,1),(-1,0),(0,-1)]
        count = 0
        while heap:
            w,node = heapq.heappop(heap)
            i,j = node
            print(node)
            ind = i * n + j
            if arr[ind] != -1:
                continue
            arr[ind] = w
            if ind == len(arr)-1:
                return w
            for e in range(4):
                newi,newj = dirc[e]
                newi+=i
                newj+=j
                cond =  0<= newi < n and 0<= newj <n
                if not cond:
                    continue
                ind = newi * n + newj 
                if arr[ind] == -1: 
                    weight = max(grid[newi][newj],w)
                    heapq.heappush(heap,(weight,(newi,newj)))
                


