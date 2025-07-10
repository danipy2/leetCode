class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i = 0   
        ans = 0
        for h in houses:
            while i < len(heaters) and heaters[i] < h:
                i += 1
            left_d  = h - heaters[i-1] if i>0  else float('inf')
            right_d = heaters[i] - h if i<len(heaters) else float('inf')
            ans = max(ans, min(left_d, right_d))
        return ans
