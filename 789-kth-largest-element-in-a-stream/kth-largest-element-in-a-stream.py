class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.larg = k
        self.heap = []
        nums.sort()
        while nums and len(self.heap) < k:
            heapq.heappush(self.heap,nums.pop())
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.larg:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)