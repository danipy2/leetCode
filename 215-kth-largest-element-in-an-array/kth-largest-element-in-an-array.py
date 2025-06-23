class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for i in nums:
            heapq.heappush(heap,-1*i)
        ans = -1
        for i in range(k):
            ans = heapq.heappop(heap)
        return -1*ans