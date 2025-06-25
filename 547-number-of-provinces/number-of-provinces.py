class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = UnionFind(n)
        numberOfComponents = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] and dsu.find(i) != dsu.find(j):
                    numberOfComponents -= 1
                    dsu.union(i, j)
        return numberOfComponents
class UnionFind:
    def __init__(self, size):
        # Write your code here
        self.rank = [0] * size
        self.root = [i for i in range(size)]
    def find(self, x):
        # Write your code here
        if x == self.root[x]:
            return x
        return self.find(self.root[self.root[x]])
    def union(self, x, y):
        # Write your code here'
        xp = self.find(x)
        yp = self.find(y)
        if xp!= yp:
            if self.rank[xp] > self.root[yp]:
                self.root[yp]= xp
            elif self.rank[xp] < self.root[yp]:
                self.root[xp] = yp
            else:
                self.root[xp] = yp
                self.rank[yp] += 1
