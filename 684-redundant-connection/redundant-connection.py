class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)+1
        root = [i for i in range(size)]
        rank = [0] * size
        def find( X):
            if X == root[X]:
                return root[X]
            root[X] = find(root[X])
            return root[X]
        def union( X, Y):
            ans = 0
            rootX, rootY = find(X), find(Y)
            print(X,Y,rootX,rootY)
            if rootX != rootY:
                rankX = rank[rootX]
                rankY = rank[rootY]
                if rankX > rankY:
                    root[rootY] = rootX
                elif rankX < rankY:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] +=1
            else:
                ans = [X,Y]
                
            return ans
        for x,y in edges:
            t = union(x,y)
            if t:
                ans = t
        return ans