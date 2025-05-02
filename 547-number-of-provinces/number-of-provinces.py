class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        self.root = [i for i in range(size)]
        self.rank = [0] * size
        def find(x):
            if x == self.root[x]:
                return x
            while x != self.root[self.root[x]]:
                x  = self.root[self.root[x]]
            return x
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if  self.rank[rootx]!=self.rank[rooty]:
                if  self.rank[rootx] >= self.rank[rooty]:
                    for i in range(len(self.root)):
                        if self.root[i] == rooty:
                            self.root[i] = rootx
                else:
                    for i in range(len(self.root)):
                        if self.root[i] == rootx:
                            self.root[i] = rooty
            else:
                for i in range(len(self.root)):
                    if self.root[i] == rooty:
                        self.root[i] = rootx
                self.rank[rootx] += 1
        for i in range(len(isConnected)):
            for j in range(i+1,len(isConnected[i])):
                if isConnected[i][j]:
                    union(i,j)
        myset = set()
        print(self.root)
        for i in self.root:
            myset.add(i)
        return len(myset)
    