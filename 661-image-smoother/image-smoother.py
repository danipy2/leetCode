class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        img1 = [[img[i][j] for j in range(len(img[0]))] for i in range(len(img))]
        def inbound(x,y):
            return  0 <= x < len(img) and 0 <= y < len(img[0])
        directions = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
        row = len(img)-3
        for i in range(len(img)):
            for j in range(len(img[0])):
                total = img[i][j]
                count = 1
                for l,r in directions:
                    li = i+l
                    rj = r+j
                    if inbound(li,rj):
                        total += img[li][rj]
                        count += 1
                res = floor(total/count)
                img1[i][j] = res

        return img1