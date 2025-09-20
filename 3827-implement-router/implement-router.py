class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()
        self.v = set()
        self.dict = {}
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.v:
            return False
        
        if len(self.q) == self.limit:
            s,d,t = self.q.popleft()
            self.v.remove((s,d,t))
            idx = bisect_left(self.dict[d], t)
            if idx < len(self.dict[d]) and self.dict[d][idx] == t:
                self.dict[d].pop(idx)

        self.q.append((source,destination,timestamp))
        self.v.add((source,destination,timestamp))
        if destination not in self.dict:
            self.dict[destination] = []
        insort(self.dict[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s,d,t = self.q.popleft()
        self.v.remove((s,d,t))
        idx = bisect_left(self.dict[d], t)
        if idx < len(self.dict[d]) and self.dict[d][idx] == t:
            self.dict[d].pop(idx)
        return (s,d,t)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dict:
            return 0
        arr = self.dict[destination]
        left = bisect_left(arr, startTime)
        right = bisect_right(arr, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)