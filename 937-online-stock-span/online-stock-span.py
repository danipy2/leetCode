class StockSpanner:

    def __init__(self):
        self.arr = [[10**5+1,-1]]
        self.count = 0

    def next(self, price: int) -> int:
        while self.arr[-1][0] <= price:
            self.arr.pop()
        self.arr.append([price,self.count])
        self.count+=1
        return self.arr[-1][1]-self.arr[-2][1]
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)