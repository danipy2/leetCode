class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = {}
        for i in range(97,123):
            root[chr(i)] = chr(i)
        def find(X):
            if X == root[X]:
                return root[X]
            root[X] = find(root[X])
            return root[X]
        def union( X, Y):
            rootX, rootY = find(X), find(Y)
            if rootX != rootY:
                rankX = ord(rootY)
                rankY = ord(rootX)
                if rankX >= rankY:
                    root[rootY] = rootX
                else:
                    root[rootX] = rootY
        for i,j in zip(s1,s2):
            union(i,j)
        arr = []
        for i in baseStr:
            arr.append(find(i))

        return "".join(arr)