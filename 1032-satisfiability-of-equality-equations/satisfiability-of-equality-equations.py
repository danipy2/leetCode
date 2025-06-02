class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        size = 26
        root = [i for i in range(size)]
        rank = [0] * size
        def find(X):
            if X == abs(root[X]):
                return root[X]
            root[X] = find(root[X])
            return root[X]
        def union(X, Y):
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
                    
        for i in range(len(equations)):
            eq = equations[i]
            ind1 = ord(eq[0])-ord("a")
            ind2 = ord(eq[3])-ord("a")
            if eq[1] == "=":
                union(ind1,ind2)
        for i in range(len(equations)):
            eq = equations[i]
            if eq[1] == "!":
                if find(ord(eq[0]) - ord('a')) == find(ord(eq[3]) - ord('a')):
                    return False
        return True
 
