class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = []
        for val ,freq in d.items():
            heapq.heappush(heap,(-freq,val))
        arr = []
        while k:
            k-=1
            l,r = heapq.heappop(heap)
            arr.append(r)

        return arr