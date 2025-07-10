class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        maxm = 1000000009
        minm = 0
        for i in houses:
            ind = bisect_left(heaters,i)-1
            leftlgth = maxm
            rightlgth = maxm 
            if 0<= ind<len(heaters):
                leftlgth = i - heaters[ind]
            if 0<= ind+1<len(heaters):
                rightlgth = heaters[ind+1]- i
            minm = max(minm,min(leftlgth,rightlgth))
        return minm
