class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxm = 0
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1,len(points)):
                x2,y2 = points[j]
                for k in range(j+1,len(points)):
                    x3,y3 = points[k]
                    l1 = math.sqrt(abs(x1-x2)*abs(x1-x2)+abs(y1-y2)*abs(y1-y2))
                    l2 = math.sqrt(abs(x1-x3)*abs(x1-x3)+abs(y1-y3)*abs(y1-y3))
                    l3 = math.sqrt(abs(x3-x2)*abs(x3-x2)+abs(y3-y2)*abs(y3-y2))
                    p = (l1+l2+l3)/2
                    n = (p*(p-l1)*(p-l2)*(p-l3))
                    if n>0:
                        maxm = max(maxm,math.sqrt(n))

            
        return maxm