class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        minm = 0
        n = len(heaters)
        for i in houses:
            ind = bisect_left(heaters,i)
            leftlgth = i - heaters[ind-1] if 0<= ind-1 <n else inf
            rightlgth = heaters[ind]-i if 0<= ind<n else inf
            minm = max(minm,min(leftlgth,rightlgth))
        return minm
