class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.larg = k
        self.heap = []
        nums.sort()
        while nums and len(self.heap) < k:
            heapq.heappush(self.heap,nums.pop())
    def add(self, val: int) -> int:
        x = -inf
        heapq.heappush(self.heap,val)
        y = heapq.heappop(self.heap)
        if len(self.heap)==self.larg:
            x = heapq.heappop(self.heap)

        y = max(y,x)
        heapq.heappush(self.heap,y)
 
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)