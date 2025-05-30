class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        arr = [[1,6,5],[4,2,3],[6,1],[5],[1,3,2,4,6],[3,5,2,4]]
        arr2 = [[1,3,4],[5,2,6],[6,5,4,2],[5,3,1,2,6],[4],[3,1]]
        d1 = [(0,1),(1,0),(1,0),(1,0),(0,-1),(0,1)]
        d2 = [(0,-1),(-1,0),(-1,0),(0,1),(-1,0),(-1,0)]
        visted = set()
        cond = False
        dirc = {5:[6],6:[5],3:[4],4:[3,1],1:[4,5]}
        def inbound(x,y):
            return 0<=x<len(grid) and 0<=y<len(grid[0])
        def dfs(x,y,d):
            if ((x,y,d)) in visted or not inbound(x,y):
                print((x,y,d) in visted)
                
                return 
            if x == len(grid)-1 and y==len(grid[0])-1:
                nonlocal cond
                cond = True
                return 
            visted.add((x,y,d))
            l,r= d1[grid[x][y]-1]
            x1,y1 = x,y
            val = grid[x][y]
            
            
            if d == -1:
                l,r= d2[grid[x][y]-1]
            x1 += l
            y1 += r
            if not inbound(x1,y1):
                return 
            c = False
            if d==1 and val in arr[grid[x1][y1]-1]:
                c = True
            elif d==-1 and val in arr2[grid[x1][y1]-1]:
                c = True

            if c:
                val2 = grid[x1][y1]
                if val2 in dirc and val in dirc[val2]:
                    d *= -1

                dfs(x1,y1,d)
        
        dfs(0,0,1)
        dfs(0,0,-1)
        return cond

        
