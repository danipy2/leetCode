class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        def bsh(tar):
            l = 0
            r = len(heaters)-1
            while l <=r:
                mid =  (l + r)//2
                if heaters[mid] == tar:
                    return mid
                elif heaters[mid] > tar:
                    r = mid -1
                else:
                    l = mid +1
            return l-1
        maxm = inf
        minm = 0
        for i in houses:
            ind = bsh(i)
            leftlgth = maxm
            rightlgth = maxm 
            if 0<= ind<len(heaters):
                leftlgth = i - heaters[ind]
            if 0<= ind+1<len(heaters):
                rightlgth = heaters[ind+1]- i
            minm = max(minm,min(leftlgth,rightlgth))
        return minm
