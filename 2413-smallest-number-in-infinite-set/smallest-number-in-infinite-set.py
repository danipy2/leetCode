class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1001)]

    def popSmallest(self) -> int:
        for i in self.nums:
            if i != 0:
                self.nums[i] = 0
                return i

    def addBack(self, num: int) -> None:
        self.nums[num] = num


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)