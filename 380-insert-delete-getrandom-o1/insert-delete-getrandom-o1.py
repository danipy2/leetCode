class RandomizedSet:

    def __init__(self):
        self.s = set()
        self.d = set()
        self.arr = []
        
    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d.add(val)
            self.arr.append(val)
        if val in self.s:
            return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        self.s.remove(val)
        return True
    def getRandom(self) -> int:
        ans = random.choice(self.arr)
        while ans not in self.s:
            ans = random.choice(self.arr)
        return ans

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()