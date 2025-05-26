class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visted = set()
        def isbound(x,y):
            return 0<=y < len(image[0]) and 0<=x<len(image)
        def dfs(x,y,c):
            if (x,y) in visted or image[x][y]!=c:
                return 
            visted.add((x,y))
            image[x][y] = color
            for i ,j in directions:
                cx = x+i
                cy = y+j
                
                if isbound(cx,cy):
                    dfs(cx,cy,c)
        dfs(sr,sc,image[sr][sc])
        return image

        