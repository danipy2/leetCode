class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        size = len(accounts)
        root = [i for i in range(size)]
        rank = [0] * size
        def find(X):
            if X == root[X]:
                return root[X]
            root[X] = find(root[X])
            return root[X]
        def union( X, Y):
            rootX, rootY = find(X), find(Y)
            if rootX != rootY:
                rankX = rank[rootX]
                rankY = rank[rootY]
                if rankX > rankY:
                    root[rootY] = rootX
                elif rankX < rankY:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
        d = {}
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                v = accounts[i][j]
                if v in d:
                    union(d[v],i)
                else:
                    d[v] = i
        d = {}
        for i in range(size):
            p = find(i)
            if p not in d and p!=i:
                d[p] = (accounts[p]+ accounts[i][1:])
                
            elif p!=i:
                d[p].extend(accounts[i][1:])
            elif p not in d :
                d[p] = accounts[p]
        arr = []
        for i in d:
            ans = d[i]
            arr.append([ans[0] ]+  sorted(list(set(ans[1:]))))

        return arr 
            
        


