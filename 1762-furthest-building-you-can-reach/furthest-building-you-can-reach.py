class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        i = 1

        while( i<len(heights) and (bricks>0 or ladders>0 or  heights[i] -heights[i-1] <=0 )  ):
            diff  = heights[i] -heights[i-1]
            if diff <=0:
                i+=1
                continue
            if bricks >=0:
                heapq.heappush(heap,-1*diff)
                bricks -= diff
                if bricks >=0:
                    i+=1
            if ladders >0 and bricks <0 :
                if heap:
                    bricks -= heapq.heappop(heap)
                i+=1
                ladders-=1
            print(i,ladders,bricks)  
        return min(i-1+ladders,len(heights)-1)