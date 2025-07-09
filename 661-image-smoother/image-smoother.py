class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img),len(img[0])
        img1 = [[0] * n  for i in range(m)]
        directions = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
        row = len(img)-3
        for i in range(m):
            for j in range(n):
                total = img[i][j]
                count = 1
                for l,r in directions:
                    x = i+l
                    y = r+j
                    if 0 <= x < m and 0 <= y < n:
                        total += img[x][y]
                        count += 1
                img1[i][j] = total//count

        return img1