class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ans = [[10**4]*len(mat[0]) for i in range(len(mat))]
        def inbound(x,y):
            return 0<=x<len(mat) and 0<=y<len(mat[0])
        qu = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    qu.append((i,j))
                    ans[i][j] = 0
        while qu:
            currx,curry = qu.popleft()
            for x ,y in directions:
                cx = currx+x
                cy = curry+y
                if inbound(cx,cy) and ans[cx][cy]> ans[currx][curry]+1:
                    ans[cx][cy] = ans[currx][curry]+1
                    qu.append((cx,cy))
        return ans
                        


        