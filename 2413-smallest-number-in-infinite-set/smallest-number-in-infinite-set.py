class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.nums = [i for i in range(1001)]
        for i in range(1001):
            heapq.heappush(self.heap,i+1)

    def popSmallest(self) -> int:
            num = heapq.heappop(self.heap)
            self.nums[num] = 0
            return num

    def addBack(self, num: int) -> None:
            if self.nums[num]  == 0:
                self.nums[num] = num
                heapq.heappush(self.heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)